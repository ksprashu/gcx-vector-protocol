import os
import re
import subprocess
import sys

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
                new_content = re.sub(r'- \*\*Phase:\*\* \[.*?\]', '- **Phase:** [IDLE]', content)
                
                # Update Last Action to reflect manual intervention
                new_content = re.sub(
                    r'- \*\*Last Action:\*\* .*', 
                    '- **Last Action:** Auto-synced phase to [IDLE] via pre-commit git hook.', 
                    new_content
                )
                
                with open(state_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                # Re-stage the STATE file so the hook modifications are included in the commit
                subprocess.run(['git', 'add', state_file], check=True)
                print("🔄 Vector Protocol: Auto-synced STATE.md phase to [IDLE] before commit.")
                
    except Exception as e:
        print(f"⚠️ Vector Protocol Warning: Failed to auto-sync STATE.md: {e}")
        # We exit 0 so we don't block the user's commit if our hook fails
        sys.exit(0)

if __name__ == '__main__':
    main()
