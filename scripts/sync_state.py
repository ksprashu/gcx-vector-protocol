import os
import re
import subprocess
import sys
import json
import glob
from datetime import datetime

def parse_plan_md(plan_md_content):
    parsed_data = {
        'intent': '',
        'success_criteria': '',
        'dependencies': '',
        'side_effects': '',
        'unknowns_hypotheses': '',
        'roadmap': []
    }
    
    current_section = None
    lines = plan_md_content.split('\n')
    
    for line in lines:
        stripped_line = line.strip()
        
        if re.match(r'^#+\s*(?:\d+[\.\)])?\s*Intent', stripped_line, re.IGNORECASE):
            current_section = 'intent'
            continue
        elif re.match(r'^#+\s*(?:\d+[\.\)])?\s*Success Criteria', stripped_line, re.IGNORECASE):
            current_section = 'success_criteria'
            continue
        elif re.match(r'^#+\s*(?:\d+[\.\)])?\s*Dependencies', stripped_line, re.IGNORECASE):
            current_section = 'dependencies'
            continue
        elif re.match(r'^#+\s*(?:\d+[\.\)])?\s*Side Effects', stripped_line, re.IGNORECASE):
            current_section = 'side_effects'
            continue
        elif re.match(r'^#+\s*(?:\d+[\.\)])?\s*Unknowns', stripped_line, re.IGNORECASE):
            current_section = 'unknowns_hypotheses'
            continue
        elif re.match(r'^#+\s*(?:\d+[\.\)])?\s*Execution Roadmap', stripped_line, re.IGNORECASE):
            current_section = 'roadmap'
            continue
            
        if current_section == 'roadmap':
            if re.match(r'^##+', stripped_line):
                parsed_data['roadmap'].append({'batch': stripped_line, 'tasks': []})
            elif re.match(r'^\s*-\s*\[([ xX])\]\s+([a-zA-Z0-9_\-]+):\s+(.*)', line):
                match = re.match(r'^\s*-\s*\[([ xX])\]\s+([a-zA-Z0-9_\-]+):\s+(.*)', line)
                if len(parsed_data['roadmap']) > 0:
                    parsed_data['roadmap'][-1]['tasks'].append({
                        'checked': match.group(1).lower() == 'x',
                        'id': match.group(2),
                        'description': match.group(3)
                    })
            elif re.match(r'^\s*-\s*\[([ xX])\]\s+(.*)', line):
                match = re.match(r'^\s*-\s*\[([ xX])\]\s+(.*)', line)
                if len(parsed_data['roadmap']) > 0:
                    parsed_data['roadmap'][-1]['tasks'].append({
                        'checked': match.group(1).lower() == 'x',
                        'id': '',
                        'description': match.group(2)
                    })
        elif current_section:
            if parsed_data[current_section]:
                parsed_data[current_section] += '\n' + line
            else:
                parsed_data[current_section] = line

    for key in parsed_data:
        if isinstance(parsed_data[key], str):
            parsed_data[key] = parsed_data[key].strip()

    return parsed_data

def aggregate_tasks():
    tasks = {}
    status_files = glob.glob('.gemini/tasks/*/STATUS.json')
    for sf in status_files:
        try:
            with open(sf, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            task_dir = os.path.dirname(sf)
            task_id = data.get('task_id')
            if not task_id:
                task_id = os.path.basename(task_dir)
                
            md_files = glob.glob(os.path.join(task_dir, '*.md'))
            md_data = {}
            for md in md_files:
                md_name = os.path.basename(md)
                try:
                    with open(md, 'r', encoding='utf-8') as mdf:
                        md_data[md_name] = mdf.read()
                except Exception:
                    pass
                    
            tasks[task_id] = {
                'id': task_id,
                'status': data.get('status', 'unknown'),
                'message': data.get('message', ''),
                'artifacts': data.get('artifacts', []),
                'dependencies': data.get('dependencies', []),
                'md_files': md_data
            }
        except Exception as e:
            print(f"Warning: could not parse {sf}: {e}")
    return tasks

def generate_html_dashboard(tasks, output_file='.gemini/VIEW.html'):
    plan_path = '.gemini/PLAN.md'
    plan_content = ""
    if os.path.exists(plan_path):
        with open(plan_path, 'r', encoding='utf-8') as f:
            plan_content = f.read()
    
    plan_data = parse_plan_md(plan_content)
    
    def markdown_to_html_list(md_text):
        if not md_text:
            return ""
        items = []
        for line in md_text.split('\n'):
            line = line.strip()
            if line.startswith('- ') or line.startswith('* '):
                items.append(f"<li>{line[2:]}</li>")
            elif line:
                items.append(f"<li>{line}</li>")
        if items:
            return f'<ul class="space-y-2 text-slate-600 list-disc list-inside">{"".join(items)}</ul>'
        else:
            return f'<p class="text-slate-600 leading-relaxed">{md_text}</p>'
            
    intent_html = f'<p class="text-slate-600 leading-relaxed">{plan_data.get("intent", "No Intent found.")}</p>'
    success_criteria_html = markdown_to_html_list(plan_data.get('success_criteria', ''))

    batches_html = ""
    for batch in plan_data.get('roadmap', []):
        batch_title = batch['batch'].lstrip('#').strip()
        tasks_html = ""
        for task in batch['tasks']:
            checked = task.get('checked', False)
            task_id = task.get('id', '')
            desc = task.get('description', '')
            
            status_badge = ""
            status_color = "slate-300"
            if task_id and task_id in tasks:
                t = tasks[task_id]
                status = t['status'].upper()
                if status in ['SUCCESS', 'COMPLETED', 'DONE', 'APPROVED']:
                    badge_bg = 'bg-emerald-100 text-emerald-800 border-emerald-200'
                    checked = True
                elif status in ['FAILED']:
                    badge_bg = 'bg-red-100 text-red-800 border-red-200'
                elif status in ['IN_PROGRESS']:
                    badge_bg = 'bg-blue-100 text-blue-800 border-blue-200'
                else:
                    badge_bg = 'bg-amber-100 text-amber-800 border-amber-200'
                status_badge = f'<span class="ml-2 px-2 py-0.5 rounded text-xs font-bold border {badge_bg}">{status}</span>'
            
            check_icon = '<svg class="w-4 h-4 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>' if checked else ''
            border_color = 'border-emerald-500 bg-emerald-50' if checked else 'border-slate-300 bg-white'
            
            tasks_html += f"""
                <div class="flex items-start">
                    <div class="flex-shrink-0 h-6 w-6 rounded-full border-2 {border_color} flex items-center justify-center mt-0.5">
                        {check_icon}
                    </div>
                    <div class="ml-4">
                        <h4 class="text-md font-medium text-slate-800">{task_id}{status_badge}</h4>
                        <p class="text-slate-500 text-sm mt-1">{desc}</p>
                    </div>
                </div>
            """
            
        batches_html += f"""
            <div class="bg-white p-6 rounded-xl shadow-sm border border-slate-200 mb-6">
                <h3 class="text-sm font-bold text-indigo-500 uppercase tracking-wider mb-4">{batch_title}</h3>
                <div class="space-y-4">
                    {tasks_html}
                </div>
            </div>
        """

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Executive Report - Vector Protocol Plan</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-50 text-slate-900 font-sans p-8 max-w-5xl mx-auto">
    <header class="flex justify-between items-center mb-8 border-b pb-4 border-slate-200">
        <div>
            <h1 class="text-3xl font-bold text-slate-800">Project Executive Report</h1>
            <p class="text-slate-500 mt-1">Vector Protocol Implementation Plan &bull; Generated: {{timestamp}}</p>
        </div>
        <div class="bg-indigo-100 text-indigo-800 px-4 py-2 rounded-full font-semibold text-sm">
            Active
        </div>
    </header>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">
        <section class="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
            <h2 class="text-xl font-semibold mb-4 text-slate-700 flex items-center">
                <svg class="w-5 h-5 mr-2 text-indigo-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                Intent
            </h2>
            {intent_html}
        </section>

        <section class="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
            <h2 class="text-xl font-semibold mb-4 text-slate-700 flex items-center">
                <svg class="w-5 h-5 mr-2 text-emerald-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                Success Criteria
            </h2>
            {success_criteria_html}
        </section>
    </div>

    <section class="mb-8">
        <h2 class="text-2xl font-bold mb-6 text-slate-800">Execution Roadmap</h2>
        <div class="space-y-6">
            {batches_html}
        </div>
    </section>
</body>
</html>
"""

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    final_html = html_template.replace("{timestamp}", now)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_html)

def render_state(content, tasks):
    preamble = ""
    if "## Task DAG / Progress" in content:
        preamble = content.split("## Task DAG / Progress")[0].strip()
    else:
        preamble = content.strip()
    
    lines = [preamble] if preamble else []
    lines.append("\n## Task DAG / Progress")
    
    for tid in sorted(tasks.keys()):
        t = tasks[tid]
        status = t.get('status', 'UNKNOWN')
        check = "x" if status.lower() in ['completed', 'approved', 'done', 'success'] else " "
        deps = t.get('dependencies', [])
        deps_str = f" (deps: {', '.join(deps)})" if deps else ""
        lines.append(f"- [{check}] **{tid}**: {status}{deps_str}")
        
    return "\n".join(lines) + "\n"

def main():
    state_file = '.gemini/STATE.md'
    
    if not os.path.exists(state_file):
        sys.exit(0)

    try:
        with open(state_file, 'r', encoding='utf-8') as f:
            content = f.read()

        match = re.search(r'- \*\*Phase:\*\* \[(.*?)\]', content)
        if match:
            phase = match.group(1)
            if phase != 'IDLE':
                content = re.sub(r'- \*\*Phase:\*\* \[.*?\]', '- **Phase:** [IDLE]', content)
                content = re.sub(
                    r'- \*\*Last Action:\*\* .*', 
                    '- **Last Action:** Auto-synced phase to [IDLE] via pre-commit git hook.', 
                    content
                )
                print("🔄 Vector Protocol: Auto-synced STATE.md phase to [IDLE] before commit.")

        tasks = aggregate_tasks()
        
        new_content = render_state(content, tasks)
        
        with open(state_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        generate_html_dashboard(tasks)
        
        if os.path.exists('.git'):
            subprocess.run(['git', 'add', state_file, '.gemini/VIEW.html'], check=False)
                
    except Exception as e:
        print(f"⚠️ Vector Protocol Warning: Failed to auto-sync STATE.md: {e}")
        sys.exit(0)

if __name__ == '__main__':
    main()
