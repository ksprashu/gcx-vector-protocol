import os
import re

files_to_check = [
    "/Users/ksprashanth/code/github/gcx-vector-protocol/.gemini/PLAN_ARCHIVE.md"
]

tasks_dir = "/Users/ksprashanth/code/github/gcx-vector-protocol/.gemini/tasks"
for root, _, files in os.walk(tasks_dir):
    for f in files:
        files_to_check.append(os.path.join(root, f))

replacements = {
    r'(?<!vector-)\bplanner\b': 'vector-planner',
    r'(?<!vector-)\bimplementer\b': 'vector-implementer',
    r'(?<!vector-)\btester\b': 'vector-tester',
    r'(?<!vector-)\bcritic\b': 'vector-critic',
    r'(?<!Vector-)\bPlanner\b': 'Vector-Planner',
    r'(?<!Vector-)\bImplementer\b': 'Vector-Implementer',
    r'(?<!Vector-)\bTester\b': 'Vector-Tester',
    r'(?<!Vector-)\bCritic\b': 'Vector-Critic'
}

for filepath in files_to_check:
    if not os.path.isfile(filepath): continue
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content
        for pattern, replacement in replacements.items():
            new_content = re.sub(pattern, replacement, new_content)
            
        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filepath}")
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
