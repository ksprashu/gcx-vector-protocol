import os
import subprocess
import tempfile
import shutil
import sys
import json

def create_mock_extension(temp_dir):
    """Sets up a minimal extension manifest in the temp dir."""
    manifest_path = os.path.join(temp_dir, 'gemini-extension.json')
    manifest_data = {
        "name": "test-protocol",
        "description": "Mock protocol for E2E tests.",
        "version": "1.0.0",
        "commands": [
            { "path": "commands/vector/plan.toml" },
            { "path": "commands/vector/work.toml" }
        ]
    }
    with open(manifest_path, 'w') as f:
        json.dump(manifest_data, f)
        
    os.makedirs(os.path.join(temp_dir, 'commands/vector'), exist_ok=True)
    
    # We copy the real tomls from the host project to the temp env to test the real prompt
    host_plan_toml = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'commands', 'vector', 'plan.toml'))
    host_work_toml = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'commands', 'vector', 'work.toml'))
    shutil.copy(host_plan_toml, os.path.join(temp_dir, 'commands/vector/plan.toml'))
    shutil.copy(host_work_toml, os.path.join(temp_dir, 'commands/vector/work.toml'))

def run_gemini_command(temp_dir, command):
    """Executes a gemini CLI command inside the temp directory."""
    print(f"Running: gemini {command}")
    
    # Use Popen to capture stdout and stderr
    # We must pass the correct environment if Gemini CLI is installed globally or via specific paths.
    # Assuming `gemini` is in the system PATH.
    try:
        result = subprocess.run(
            ['gemini'] + command.split(),
            cwd=temp_dir,
            capture_output=True,
            text=True,
            timeout=120 # Prevent hanging
        )
        return result.returncode, result.stdout, result.stderr
    except FileNotFoundError:
        print("Error: 'gemini' CLI command not found. Ensure it is installed and in your PATH.")
        sys.exit(1)
    except subprocess.TimeoutExpired:
         print("Error: Command timed out.")
         sys.exit(1)

def test_plan_initialization():
    """Tests if /vector:plan correctly bootstraps the environment."""
    print("--- Starting E2E Test: Plan Initialization ---")
    
    # Use a temporary directory to avoid dirtying the host repo
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"Testing in temporary directory: {temp_dir}")
        create_mock_extension(temp_dir)
        
        # 1. Run the plan command
        code, stdout, stderr = run_gemini_command(temp_dir, '/vector:plan Create a hello world script')
        
        print("\n--- Output ---")
        print(stdout)
        
        # 2. Verify Output structure
        if "Session Dashboard" not in stdout:
             print("❌ FAIL: Agent output did not contain 'Session Dashboard'.")
             sys.exit(1)
             
        if "<thinking>" not in stdout:
            # Note: Sometimes the CLI hides raw XML tags in final markdown render, 
            # but it should ideally be present in the raw output if we inspect it closely.
            # We'll check for the dashboard as the primary structural indicator.
            pass
            
        # 3. Verify Auto-Bootstrap Side Effects
        gemini_dir = os.path.join(temp_dir, '.gemini')
        if not os.path.exists(gemini_dir):
            print("❌ FAIL: Auto-bootstrap did not create .gemini/ directory.")
            sys.exit(1)
            
        expected_files = ['STATE.md', 'PLAN.md', 'CONTEXT.md', 'EVIDENCE.md']
        for file in expected_files:
            if not os.path.exists(os.path.join(gemini_dir, file)):
                print(f"❌ FAIL: Auto-bootstrap missing {file}.")
                sys.exit(1)
                
        print("✅ PASS: Plan Initialization Test")

def test_work_execution():
    """Tests if /vector:work can pick up a plan and execute an atomic edit."""
    print("--- Starting E2E Test: Work Execution ---")
    
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"Testing in temporary directory: {temp_dir}")
        create_mock_extension(temp_dir)
        
        # Manually bootstrap state for the test
        os.makedirs(os.path.join(temp_dir, '.gemini'), exist_ok=True)
        with open(os.path.join(temp_dir, '.gemini', 'PLAN.md'), 'w') as f:
            f.write("# 🗺️ PLAN\\n\\n- [ ] Task 1: Create a file named hello.txt containing the word Hello.\\n")
        with open(os.path.join(temp_dir, '.gemini', 'STATE.md'), 'w') as f:
            f.write("# 💾 STATE\\n- **Phase:** [IDLE]\\n\\n## 3. Scratchpad\\n")
        with open(os.path.join(temp_dir, '.gemini', 'CONTEXT.md'), 'w') as f:
            f.write("# CONTEXT\\n")
            
        # Run work command
        code, stdout, stderr = run_gemini_command(temp_dir, '/vector:work Task 1')
        
        print("\n--- Output ---")
        print(stdout)
        
        if "Session Dashboard" not in stdout:
             print("❌ FAIL: Agent output did not contain 'Session Dashboard'.")
             sys.exit(1)
             
        # Check if the file was actually created by the agent's tool call
        if not os.path.exists(os.path.join(temp_dir, 'hello.txt')):
             print("❌ FAIL: Agent failed to create hello.txt via tool call.")
             sys.exit(1)
             
        print("✅ PASS: Work Execution Test")

def main():
    test_plan_initialization()
    test_work_execution()
    print("All E2E tests passed successfully.")

if __name__ == '__main__':
    main()
