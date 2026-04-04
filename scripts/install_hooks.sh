#!/bin/bash

# Configuration
HOOKS_DIR=".git/hooks"
PRE_COMMIT_FILE="$HOOKS_DIR/pre-commit"

# Ensure hooks directory exists
if [ ! -d "$HOOKS_DIR" ]; then
    echo "❌ Error: Not a git repository (or no .git/hooks directory found)."
    exit 1
fi

# Define the hook payload
read -r -d '' HOOK_SCRIPT << 'EOF'
#!/bin/bash
# GCX Vector Protocol Pre-Commit Hook
# Auto-syncs the .gemini/STATE.md phase to [IDLE] before manual commits.

# Run the python sync script if it exists in this repo
if [ -f "scripts/sync_state.py" ]; then
    python3 scripts/sync_state.py
fi
EOF

# Install or append to the pre-commit file
if [ -f "$PRE_COMMIT_FILE" ]; then
    # Check if we already installed it
    if grep -q "Vector Protocol" "$PRE_COMMIT_FILE"; then
        echo "✅ Vector Protocol pre-commit hook is already installed."
    else
        echo "" >> "$PRE_COMMIT_FILE"
        echo "$HOOK_SCRIPT" >> "$PRE_COMMIT_FILE"
        echo "✅ Appended Vector Protocol sync logic to existing pre-commit hook."
    fi
else
    echo "$HOOK_SCRIPT" > "$PRE_COMMIT_FILE"
    chmod +x "$PRE_COMMIT_FILE"
    echo "✅ Successfully installed Vector Protocol pre-commit hook."
fi
