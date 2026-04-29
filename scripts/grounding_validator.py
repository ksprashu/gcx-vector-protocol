#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path

# New Schema for EVIDENCE.json items:
# {
#   "id": "E-XYZ", (Optional, for citations)
#   "claim": "The exact technical claim text",
#   "source_output_hash": "hash-or-id",  (or "tool_invocation_id")
#   ...
# }

def load_evidence(evidence_path: Path) -> dict:
    if not evidence_path.exists():
        print(f"Error: Evidence file not found at {evidence_path}", file=sys.stderr)
        sys.exit(1)
    try:
        with open(evidence_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON from {evidence_path}: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Map both ID and Claim text to the evidence object
    evidence_map = {}
    if "evidence" in data:
        for item in data["evidence"]:
            if "id" in item:
                evidence_map[item["id"]] = item
            if "claim" in item:
                evidence_map[item["claim"]] = item
    return evidence_map

def extract_technical_claims(content: str) -> list:
    """Extract claims from a 'Technical Claims' markdown block."""
    claims = []
    in_claims_section = False
    for line in content.splitlines():
        line = line.strip()
        if re.match(r'^#+\s+Technical Claims', line, re.IGNORECASE):
            in_claims_section = True
            continue
        elif in_claims_section and re.match(r'^#+\s+', line):
            # Reached next section
            break
            
        if in_claims_section:
            # Extract list items (bullet points)
            m = re.match(r'^[-\*]\s+(.*)', line)
            if m:
                claims.append(m.group(1).strip())
    return claims

def validate_file(file_path: Path, evidence_map: dict) -> list:
    """Check a file for evidence citations and technical claims, returning a list of errors."""
    errors = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return [f"Could not read file: {e}"]

    # 1. Grounding check: Find all evidence citations like [E-001]
    citations = set(re.findall(r'\[(E-\d{3,})\]', content))
    for citation in citations:
        if citation not in evidence_map:
            errors.append(f"Invalid citation found: [{citation}] is not defined in EVIDENCE.json")
            
    # 2. Claim check: Parse for 'Technical Claims' and validate against evidence ledger
    claims = extract_technical_claims(content)
    for claim in claims:
        # Allow exact match or match ignoring leading citation [E-xxx]
        clean_claim = re.sub(r'^\[E-\d{3,}\]\s*', '', claim).strip()
        
        ev_item = evidence_map.get(claim) or evidence_map.get(clean_claim)
        
        if ev_item:
            if "source_output_hash" not in ev_item and "tool_invocation_id" not in ev_item:
                errors.append(f"Evidence for claim '{claim}' is missing 'source_output_hash' or 'tool_invocation_id'")
        else:
            errors.append(f"Unverified technical claim found: '{claim}'. Not found in evidence ledger.")
            
    return errors

def main():
    parser = argparse.ArgumentParser(description="Vector Protocol Grounding Validator")
    parser.add_argument('--evidence', type=str, default='.gemini/EVIDENCE.json', help='Path to EVIDENCE.json')
    parser.add_argument('--files', nargs='*', help='Files to validate for proper citations')
    parser.add_argument('--dir', type=str, help='Directory to scan recursively for .md and .json files')
    
    args = parser.parse_args()
    
    evidence_path = Path(args.evidence)
    evidence_map = load_evidence(evidence_path)
    
    files_to_check = []
    if args.files:
        files_to_check.extend([Path(f) for f in args.files])
    
    if args.dir:
        dir_path = Path(args.dir)
        if dir_path.exists():
            for ext in ('*.md', '*.json'):
                files_to_check.extend(dir_path.rglob(ext))
        else:
            print(f"Directory not found: {dir_path}", file=sys.stderr)
            sys.exit(1)
    
    if not files_to_check:
        print("No files specified for validation. Use --files or --dir.")
        sys.exit(0)
        
    has_errors = False
    
    for file_path in sorted(set(files_to_check)):
        if not file_path.is_file() or file_path.name == 'EVIDENCE.json':
            continue
            
        errors = validate_file(file_path, evidence_map)
        if errors:
            has_errors = True
            print(f"Validation errors in {file_path}:", file=sys.stderr)
            for error in errors:
                print(f"  - {error}", file=sys.stderr)
                
    if has_errors:
        print("\nGrounding Validation FAILED. Unverified claims detected.", file=sys.stderr)
        sys.exit(1)
    else:
        print("\nGrounding Validation PASSED. All claims are grounded and verified.")
        sys.exit(0)

if __name__ == '__main__':
    main()