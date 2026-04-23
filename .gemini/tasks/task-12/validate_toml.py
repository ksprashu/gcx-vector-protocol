import sys
import json

try:
    import tomllib
except ImportError:
    try:
        import tomli as tomllib
    except ImportError:
        print("FAILED: Missing TOML parser (tomllib or tomli)")
        sys.exit(1)

try:
    with open("/Users/ksprashanth/code/github/gcx-vector-protocol/policies/autonomous.toml", "rb") as f:
        data = tomllib.load(f)
except Exception as e:
    print(f"FAILED: Invalid TOML: {e}")
    sys.exit(1)

rules = data.get("rule", [])
if not isinstance(rules, list):
    print("FAILED: 'rule' must be an array of tables ([[rule]])")
    sys.exit(1)

valid_decisions = ["allow", "ask_user", "deny", "terminate"]

for i, rule in enumerate(rules):
    if "toolName" not in rule:
        print(f"FAILED: rule {i} missing 'toolName'")
        sys.exit(1)
    if "decision" not in rule:
        print(f"FAILED: rule {i} missing 'decision'")
        sys.exit(1)
    if rule["decision"] not in valid_decisions:
        print(f"FAILED: rule {i} invalid decision '{rule['decision']}'")
        sys.exit(1)
    if "priority" not in rule or not isinstance(rule["priority"], int):
        print(f"FAILED: rule {i} missing or invalid 'priority'")
        sys.exit(1)
    
    if "toolName" in rule and (rule["toolName"] == "run_shell_command" or (isinstance(rule["toolName"], list) and "run_shell_command" in rule["toolName"])):
        if "commandPrefix" in rule:
            if not isinstance(rule["commandPrefix"], (str, list)):
                print(f"FAILED: rule {i} invalid 'commandPrefix' type (must be string or list)")
                sys.exit(1)

print("SUCCESS: policies/autonomous.toml is valid and conforms to schema.")
print(f"Parsed Data: {json.dumps(data, indent=2)}")
