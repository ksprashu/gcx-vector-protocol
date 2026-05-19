import os
import re
import subprocess
import sys
import json
import glob
from datetime import datetime

def aggregate_tasks():
    tasks = {}
    # Use glob to find all STATUS.json
    status_files = glob.glob('.gemini/tasks/*/STATUS.json')
    for sf in status_files:
        try:
            with open(sf, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            task_dir = os.path.dirname(sf)
            task_id = data.get('task_id')
            if not task_id:
                task_id = os.path.basename(task_dir)
                
            # Read all md files in the task directory
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
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vector Protocol - Swarm State Dashboard</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-50 text-gray-800 font-sans p-6 min-h-screen">
    <div class="max-w-7xl mx-auto">
        <header class="mb-8 border-b border-gray-200 pb-6 bg-white p-6 rounded-xl shadow-sm">
            <h1 class="text-3xl font-extrabold text-gray-900 tracking-tight">Vector Protocol Dashboard</h1>
            <p class="text-sm text-gray-500 mt-2 font-medium">Autonomous Swarm State Overview &bull; Generated: {timestamp}</p>
        </header>
        
        <div class="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-6">
            {task_cards}
        </div>
    </div>
    
    <script>
        function toggleDetails(id) {
            const el = document.getElementById('details-' + id);
            const icon = document.getElementById('icon-' + id);
            if (el.classList.contains('hidden')) {
                el.classList.remove('hidden');
                icon.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M14.707 12.707a1 1 0 01-1.414 0L10 9.414l-3.293 3.293a1 1 0 01-1.414-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 010 1.414z" clip-rule="evenodd" /></svg>`;
            } else {
                el.classList.add('hidden');
                icon.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>`;
            }
        }
    </script>
</body>
</html>
"""

    task_cards = []
    for task_id in sorted(tasks.keys()):
        t = tasks[task_id]
        
        # Color mapping based on status
        status_colors = {
            'success': 'bg-emerald-100 text-emerald-800 border-emerald-200',
            'completed': 'bg-emerald-100 text-emerald-800 border-emerald-200',
            'done': 'bg-emerald-100 text-emerald-800 border-emerald-200',
            'approved': 'bg-emerald-100 text-emerald-800 border-emerald-200',
            'in_progress': 'bg-blue-100 text-blue-800 border-blue-200',
            'pending': 'bg-amber-100 text-amber-800 border-amber-200',
            'failed': 'bg-red-100 text-red-800 border-red-200',
            'blocked': 'bg-purple-100 text-purple-800 border-purple-200'
        }
        
        status_lower = t['status'].lower()
        color_class = status_colors.get(status_lower, 'bg-gray-100 text-gray-800 border-gray-200')
        
        artifacts_html = ""
        if t['artifacts']:
            items = ''.join([f"<li class='text-xs font-mono text-gray-600 bg-gray-50 px-2 py-1 rounded'>{a}</li>" for a in t['artifacts']])
            artifacts_html = f"<div class='mb-4'><strong>Artifacts:</strong><ul class='flex flex-wrap gap-2 mt-2'>{items}</ul></div>"
            
        md_files_html = ""
        if t['md_files']:
            for i, (md_name, md_content) in enumerate(t['md_files'].items()):
                escaped_content = md_content.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                md_files_html += f"<div class='mt-4'><h4 class='text-sm font-bold text-gray-700 bg-gray-100 px-3 py-2 rounded-t-md border border-gray-200 border-b-0'>{md_name}</h4><pre class='text-xs bg-white p-3 rounded-b-md overflow-x-auto max-h-60 text-gray-700 border border-gray-200 shadow-inner whitespace-pre-wrap'>{escaped_content}</pre></div>"

        safe_id = re.sub(r'[^a-zA-Z0-9]', '_', task_id)

        card = f"""
        <div class="bg-white rounded-xl shadow-sm hover:shadow-md transition-shadow border border-gray-200 flex flex-col overflow-hidden">
            <div class="p-5 border-b border-gray-100 cursor-pointer bg-gray-50 hover:bg-gray-100 transition-colors" onclick="toggleDetails('{safe_id}')">
                <div class="flex justify-between items-start mb-3">
                    <h2 class="text-xl font-bold text-gray-900 truncate pr-4" title="{task_id}">{task_id}</h2>
                    <span class="px-2.5 py-1 rounded-md text-xs font-bold border {color_class} uppercase tracking-wider flex-shrink-0 shadow-sm">
                        {t['status']}
                    </span>
                </div>
                <div class="flex justify-between items-end">
                    <p class="text-sm text-gray-600 line-clamp-2 leading-relaxed flex-grow pr-4">{t['message'] or 'No message provided.'}</p>
                    <div id="icon-{safe_id}" class="text-gray-400">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
                    </div>
                </div>
            </div>
            
            <div id="details-{safe_id}" class="hidden p-5 bg-white flex-grow border-t border-gray-100">
                {artifacts_html}
                <div class="mt-2">
                    <h3 class="text-sm font-semibold text-gray-800 uppercase tracking-wider mb-2 border-b pb-1">Subagent Logs</h3>
                    {md_files_html if md_files_html else '<p class="text-xs text-gray-500 italic bg-gray-50 p-3 rounded border border-gray-100">No markdown logs found.</p>'}
                </div>
            </div>
        </div>
        """
        task_cards.append(card)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    final_html = html_template.replace("{timestamp}", now).replace("{task_cards}", "\n".join(task_cards))
    
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
    
    # Sort tasks by ID
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
        # Not a Vector initialized repo, silently exit
        sys.exit(0)

    try:
        with open(state_file, 'r', encoding='utf-8') as f:
            content = f.read()

        match = re.search(r'- \*\*Phase:\*\* \[(.*?)\]', content)
        if match:
            phase = match.group(1)
            # If phase is not IDLE, user is committing manually outside of /vector:save
            if phase != 'IDLE':
                # Reset Phase
                content = re.sub(r'- \*\*Phase:\*\* \[.*?\]', '- **Phase:** [IDLE]', content)
                
                # Update Last Action to reflect manual intervention
                content = re.sub(
                    r'- \*\*Last Action:\*\* .*', 
                    '- **Last Action:** Auto-synced phase to [IDLE] via pre-commit git hook.', 
                    content
                )
                print("🔄 Vector Protocol: Auto-synced STATE.md phase to [IDLE] before commit.")

        # Aggregate tasks
        tasks = aggregate_tasks()
        
        # Render new state content
        new_content = render_state(content, tasks)
        
        with open(state_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        # Generate HTML Dashboard
        generate_html_dashboard(tasks)
        
        # Re-stage the STATE file so the hook modifications are included in the commit
        if os.path.exists('.git'):
            subprocess.run(['git', 'add', state_file, '.gemini/VIEW.html'], check=False)
                
    except Exception as e:
        print(f"⚠️ Vector Protocol Warning: Failed to auto-sync STATE.md: {e}")
        # We exit 0 so we don't block the user's commit if our hook fails
        sys.exit(0)

if __name__ == '__main__':
    main()
