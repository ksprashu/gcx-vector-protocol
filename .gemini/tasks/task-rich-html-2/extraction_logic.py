import re

def parse_plan_md(plan_md_content):
    """
    Parses the content of .gemini/PLAN.md and extracts Intent, Success Criteria, and Roadmap details.
    
    Returns a dictionary with the extracted sections.
    """
    parsed_data = {
        'intent': '',
        'success_criteria': '',
        'dependencies': '',
        'side_effects': '',
        'unknowns_hypotheses': '',
        'roadmap': []
    }
    
    # Simple state machine to parse sections
    current_section = None
    
    lines = plan_md_content.split('\n')
    
    for line in lines:
        stripped_line = line.strip()
        
        # Check for top-level headers
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
            
        # Append content to the current section
        if current_section == 'roadmap':
            if re.match(r'^##+', stripped_line):
                parsed_data['roadmap'].append({'batch': stripped_line, 'tasks': []})
            elif re.match(r'^\s*-\s*\[[ xX]\]\s+(.*)', line) and len(parsed_data['roadmap']) > 0:
                parsed_data['roadmap'][-1]['tasks'].append(stripped_line)
        elif current_section:
            if parsed_data[current_section]:
                parsed_data[current_section] += '\n' + line
            else:
                parsed_data[current_section] = line

    # Clean up leading/trailing whitespaces
    for key in parsed_data:
        if isinstance(parsed_data[key], str):
            parsed_data[key] = parsed_data[key].strip()

    return parsed_data

# Example usage (for testing purposes, to be integrated into sync_state.py)
if __name__ == "__main__":
    import os
    plan_path = '.gemini/PLAN.md'
    if os.path.exists(plan_path):
        with open(plan_path, 'r', encoding='utf-8') as f:
            content = f.read()
            data = parse_plan_md(content)
            print("Extracted Intent:")
            print(data['intent'])
            print("\nExtracted Roadmap:")
            for batch in data['roadmap']:
                print(batch['batch'])
                for task in batch['tasks']:
                    print("  " + task)
