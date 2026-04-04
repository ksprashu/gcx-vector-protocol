import os
import re
import json
import sys

def analyze_state_file(path):
    if not os.path.exists(path):
        return None
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Count task completion marks
    completed_tasks = len(re.findall(r'- \[x\]', content))
    failed_tasks = len(re.findall(r'- \[!\]', content))
    pending_tasks = len(re.findall(r'- \[ \]', content))
    
    # Extract phase
    phase_match = re.search(r'- \*\*Phase:\*\* \[(.*?)\]', content)
    phase = phase_match.group(1) if phase_match else "Unknown"
    
    return {
        "completed": completed_tasks,
        "failed": failed_tasks,
        "pending": pending_tasks,
        "current_phase": phase
    }

def main():
    print("Generating local Vector Protocol metrics...")
    
    state_metrics = analyze_state_file('.gemini/STATE.md')
    if not state_metrics:
        print("Error: .gemini/STATE.md not found.")
        sys.exit(1)
        
    # Also check evidence count
    evidence_count = 0
    if os.path.exists('.gemini/EVIDENCE.md'):
        with open('.gemini/EVIDENCE.md', 'r', encoding='utf-8') as f:
            evidence_count = len(re.findall(r'^\| E-\d+', f.read(), re.MULTILINE))
            
    metrics_report = {
        "summary": {
            "total_completed_tasks": state_metrics["completed"],
            "total_failed_tasks": state_metrics["failed"],
            "total_evidence_entries": evidence_count,
            "current_workflow_phase": state_metrics["current_phase"]
        }
    }
    
    # Output report
    output_path = '.gemini/METRICS.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(metrics_report, f, indent=2)
        
    print(f"Success: Metrics generated in {output_path}")
    print(json.dumps(metrics_report["summary"], indent=2))

if __name__ == '__main__':
    main()
