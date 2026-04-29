#!/usr/bin/env python3
import argparse
import json
import os
import re
import sys
from pathlib import Path

# Defined whitelist of approved Gemini models based on repository truth (GEMINI.md)
APPROVED_MODELS = {
    "gemini-3-pro-image-preview",
    "gemini-3.1-flash-image-preview",
    "gemini-2.5-flash-image",
    "gemini-3.1-pro-preview-customtools",
    "gemini-3.1-pro-preview",
    "gemini-3-flash-preview",
    "gemini-3.1-flash-lite-preview",
    "gemini-3.1-flash-live-preview",
    "gemini-3.1-flash-tts-preview",
    "gemini-1.5-pro",
    "gemini-1.5-flash",
    "gemini-2.0-flash",
    "gemini-2.5-pro",
}

# Known hallucinated or deprecated entities that should trigger an explicit failure
HALLUCINATED_MODELS = {
    "gemini-ultra",
    "gemini-pro",
    "gemini-1.0-pro",
    "gemini-1.0-ultra",
    "gemini-1.5-ultra",
}

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
    
    # Map of ID to evidence object
    evidence_map = {}
    if "evidence" in data:
        for item in data["evidence"]:
            if "id" in item:
                evidence_map[item["id"]] = item
    return evidence_map

def extract_models(content: str) -> set:
    """Extract potential gemini model names from text."""
    # Matches strings like gemini-1.5-pro, gemini-3.1-flash-preview, gemini-ultra
    return set(re.findall(r'\bgemini-[a-zA-Z0-9\.\-]+\b', content))

def validate_file(file_path: Path, evidence_map: dict) -> list:
    """Check a file for evidence citations and valid models, returning a list of errors."""
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
            
    # 2. Entity check: Parse for model names and validate against whitelist
    found_models = extract_models(content)
    for model in found_models:
        if model in HALLUCINATED_MODELS:
            errors.append(f"Hallucinated model entity found: '{model}'")
        elif model not in APPROVED_MODELS:
            errors.append(f"Unverified model entity found: '{model}'. Not in approved whitelist.")
            
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
        print("\nGrounding Validation FAILED. Unverified claims or unapproved entities detected.", file=sys.stderr)
        sys.exit(1)
    else:
        print("\nGrounding Validation PASSED. All claims are grounded and entities verified.")
        sys.exit(0)

if __name__ == '__main__':
    main()