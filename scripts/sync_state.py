import os
import re
import subprocess
import sys
import json
import glob

def aggregate_tasks():
    tasks = {}
    # Use glob to find all STATUS.json
    status_files = glob.glob('.gemini/tasks/*/STATUS.json')
    for sf in status_files:
        try:
            with open(sf, 'r', encoding='utf-8') as f:
                data = json.load(f)
                task_id = data.get('task_id', 'unknown')
                tasks[task_id] = data
        except Exception as e:
            print(f"Warning: could not parse {sf}: {e}")
    return tasks

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
        check = "x" if status.lower() in ['completed', 'approved', 'done'] else " "
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
        
        # Re-stage the STATE file so the hook modifications are included in the commit
        if os.path.exists('.git'):
            subprocess.run(['git', 'add', state_file], check=False)
                
    except Exception as e:
        print(f"⚠️ Vector Protocol Warning: Failed to auto-sync STATE.md: {e}")
        # We exit 0 so we don't block the user's commit if our hook fails
        sys.exit(0)

if __name__ == '__main__':
    main()
