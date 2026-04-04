import json
import os
import sys
import tomllib

def main():
    errors = []
    
    # 1. Load manifest
    manifest_path = 'gemini-extension.json'
    if not os.path.exists(manifest_path):
        print(f"Error: {manifest_path} not found.")
        sys.exit(1)
        
    with open(manifest_path, 'r', encoding='utf-8') as f:
        try:
            manifest = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error parsing {manifest_path}: {e}")
            sys.exit(1)

    commands = manifest.get('commands', [])
    if not commands:
        print(f"Warning: No commands found in {manifest_path}")
        
    # Mandatory XML tags expected in all commands
    mandatory_tags = [
        '<context>', '</context>',
        '<role>', '</role>',
        '<goal>', '</goal>',
        '<interaction_standards>', '</interaction_standards>',
        '<protocol>', '</protocol>',
        '<output_format>', '</output_format>'
    ]

    for cmd in commands:
        path = cmd.get('path')
        if not path:
            errors.append("A command in the manifest is missing a 'path' attribute.")
            continue
            
        # 2. Check if file exists
        if not os.path.exists(path):
            errors.append(f"Command file missing: {path}")
            continue
            
        # 3. Parse TOML
        try:
            with open(path, 'rb') as f:
                toml_data = tomllib.load(f)
        except Exception as e:
            errors.append(f"Error parsing TOML in {path}: {e}")
            continue
            
        prompt = toml_data.get('prompt', '')
        if not prompt:
            errors.append(f"Command {path} is missing a 'prompt' string.")
            continue
            
        # 4. Validate XML tags
        missing_tags = [tag for tag in mandatory_tags if tag not in prompt]
        if missing_tags:
            errors.append(f"Command {path} is missing mandatory XML tags: {', '.join(missing_tags)}")

    if errors:
        print("Validation Failed with the following errors:")
        for err in errors:
            print(f" - {err}")
        sys.exit(1)
    else:
        print("Success: All commands validated successfully against the structural schema.")
        sys.exit(0)

if __name__ == '__main__':
    main()
