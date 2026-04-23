import sys

try:
    if sys.version_info >= (3, 11):
        import tomllib as toml
    else:
        import tomli as toml
except ImportError:
    print("Error: Require Python 3.11+ or tomli.")
    sys.exit(1)

def validate(file_path):
    errors = []
    try:
        with open(file_path, "rb") as f:
            data = toml.load(f)
    except Exception as e:
        return [f"Syntactically invalid TOML: {e}"]

    if "rule" not in data:
        errors.append("No [[rule]] blocks found.")
        return errors

    rules = data.get("rule", [])
    if not isinstance(rules, list):
         errors.append("'rule' must be an array of tables ([[rule]]).")
         return errors

    for i, rule in enumerate(rules):
        if "toolName" not in rule:
            errors.append(f"Rule {i+1} missing 'toolName'.")
        
        if "commandPrefix" in rule:
             if not isinstance(rule["commandPrefix"], list) or not all(isinstance(x, str) for x in rule["commandPrefix"]):
                 errors.append(f"Rule {i+1} 'commandPrefix' must be an array of strings.")
        
        if "decision" in rule:
            if rule["decision"] not in ["allow", "ask_user"]:
                errors.append(f"Rule {i+1} 'decision' must be 'allow' or 'ask_user', got '{rule['decision']}'.")
        else:
             errors.append(f"Rule {i+1} missing 'decision'.")

    return errors

if __name__ == "__main__":
    file_path = sys.argv[1]
    errors = validate(file_path)
    
    if not errors:
        print("SUCCESS")
        sys.exit(0)
    else:
        for err in errors:
            print(f"ERROR: {err}")
        sys.exit(1)
