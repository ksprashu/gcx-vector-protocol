import os
import sys
import re

def lint_state():
    path = '.gemini/STATE.md'
    if not os.path.exists(path):
        return [f"{path} does not exist."]
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    errors = []
    if "# 💾 STATE" not in content:
        errors.append(f"{path} missing main header '# 💾 STATE'")
    if "## 1. Status" not in content:
        errors.append(f"{path} missing '## 1. Status'")
    if not re.search(r'- \*\*Phase:\*\* \[[A-Z]+\]', content):
        errors.append(f"{path} missing or incorrectly formatted '- **Phase:** [PHASE]'")
    if "## 2. Context" not in content:
        errors.append(f"{path} missing '## 2. Context'")
    if "## 3. Scratchpad" not in content:
        errors.append(f"{path} missing '## 3. Scratchpad'")
    if "## 4. Next Steps" not in content:
        errors.append(f"{path} missing '## 4. Next Steps'")
    return errors

def lint_plan():
    path = '.gemini/PLAN.md'
    if not os.path.exists(path):
        return [f"{path} does not exist."]
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    errors = []
    if "# 🗺️ PLAN" not in content and "# 🗺️ DESIGN" not in content:
        errors.append(f"{path} missing main header '# 🗺️ PLAN' or '# 🗺️ DESIGN'")
    return errors

def lint_context():
    path = '.gemini/CONTEXT.md'
    if not os.path.exists(path):
        return [f"{path} does not exist."]
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    errors = []
    if "# 📄 CONTEXT" not in content:
        errors.append(f"{path} missing main header '# 📄 CONTEXT'")
    return errors

def main():
    print("Linting .gemini/ protocol files...")
    
    if not os.path.exists('.gemini'):
        print("Error: .gemini directory not found. Are you in a Vector Protocol initialized repository?")
        sys.exit(1)
        
    all_errors = []
    all_errors.extend(lint_state())
    all_errors.extend(lint_plan())
    all_errors.extend(lint_context())
    
    if all_errors:
        print("Linting Failed with the following errors:")
        for err in all_errors:
            print(f" - {err}")
        sys.exit(1)
    else:
        print("Success: All core protocol files adhere to the 5-File System structural invariants.")
        sys.exit(0)

if __name__ == '__main__':
    main()
