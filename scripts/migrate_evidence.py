import os
import json
import re

def migrate():
    md_path = '.gemini/EVIDENCE.md'
    json_path = '.gemini/EVIDENCE.json'
    
    if not os.path.exists(md_path):
        print(f"Skipping migration: {md_path} not found.")
        return

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    entries = []
    # Match markdown table rows, ignoring the header and separator
    lines = content.strip().split('\n')
    for line in lines:
        if line.startswith('| ID |') or line.startswith('|---|'):
            continue
        if line.startswith('|'):
            parts = [p.strip() for p in line.split('|')[1:-1]]
            if len(parts) >= 5:
                entry = {
                    "id": parts[0],
                    "topic": parts[1],
                    "source": parts[2],
                    "authoritative": parts[3] == 'Yes',
                    "last_checked": parts[4]
                }
                entries.append(entry)

    data = {
        "schema_version": "1.0",
        "evidence": entries
    }

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
        
    print(f"Successfully migrated {len(entries)} entries to {json_path}")

if __name__ == '__main__':
    migrate()
