# Installation Instructions

To apply these policies, run the following commands from the workspace root:
```bash
mkdir -p .gemini/archived
mkdir -p ~/.gemini/policies
cp policies/autonomous.toml ~/.gemini/policies/autonomous.toml
```

**Note on Policy Tiers:**
The policy file located in `policies/autonomous.toml` acts at **Tier 2 (Extension)** and is automatically discovered by the Vector Protocol extension. However, `allow` rules require installation at **Tier 4 (User)** (i.e., `~/.gemini/policies/`) to function correctly. Therefore, the above copy command is necessary.

**Manual Merge Instructions:**
Please manually merge the contents of `.gemini/tasks/task-policies/GEMINI_UPDATE.md` into the root `.gemini/GEMINI.md` file to apply the updated behavioral mandates.
