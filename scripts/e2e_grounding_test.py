#!/usr/bin/env python3
import os
import subprocess
import tempfile
import json
import unittest

class TestGroundingValidatorE2E(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for tests
        self.test_dir = tempfile.TemporaryDirectory()
        self.evidence_path = os.path.join(self.test_dir.name, "EVIDENCE.json")
        
        # Write a dummy EVIDENCE.json
        evidence_data = {
            "evidence": [
                {
                    "id": "E-001", 
                    "claim": "Dummy evidence",
                    "source_output_hash": "123"
                },
                {
                    "id": "E-002",
                    "claim": "The `gemini-cli` uses the `--verified-flag`.",
                    "source_output_hash": "abc"
                }
            ]
        }
        with open(self.evidence_path, 'w') as f:
            json.dump(evidence_data, f)
            
        self.validator_script = os.path.abspath(os.path.join(os.path.dirname(__file__), "grounding_validator.py"))

    def tearDown(self):
        self.test_dir.cleanup()
        
    def run_validator(self, test_file_path):
        result = subprocess.run(
            ["python3", self.validator_script, "--evidence", self.evidence_path, "--files", test_file_path],
            capture_output=True,
            text=True
        )
        return result

    def test_1_valid_citations(self):
        """Test 1: A file with valid citations passes."""
        test_file = os.path.join(self.test_dir.name, "test1.md")
        with open(test_file, 'w') as f:
            f.write("This is a valid file citing [E-001].")
            
        result = self.run_validator(test_file)
        self.assertEqual(result.returncode, 0, f"Expected pass, but failed. Stderr: {result.stderr}")
        self.assertIn("Grounding Validation PASSED", result.stdout + result.stderr)

    def test_2_unverified_claim(self):
        """Test 2: A file with an unverified technical claim fails."""
        test_file = os.path.join(self.test_dir.name, "test2.md")
        with open(test_file, 'w') as f:
            f.write("## Technical Claims\n* The `--unverified-flag` is very fast.\n")
            
        result = self.run_validator(test_file)
        self.assertNotEqual(result.returncode, 0, "Expected failure, but passed.")
        self.assertIn("Unverified technical claim found", result.stderr)

    def test_3_verified_claim(self):
        """Test 3: A file with a verified technical claim passes."""
        test_file = os.path.join(self.test_dir.name, "test3.md")
        with open(test_file, 'w') as f:
            f.write("## Technical Claims\n* [E-002] The `gemini-cli` uses the `--verified-flag`.\n")
            
        result = self.run_validator(test_file)
        self.assertEqual(result.returncode, 0, f"Expected pass, but failed. Stderr: {result.stderr}")

    def test_4_missing_citation(self):
        """Test 4: A file with a missing citation [E-999] fails."""
        test_file = os.path.join(self.test_dir.name, "test4.md")
        with open(test_file, 'w') as f:
            f.write("This file makes a claim with an invalid citation [E-999].")
            
        result = self.run_validator(test_file)
        self.assertNotEqual(result.returncode, 0, "Expected failure, but passed.")
        self.assertIn("Invalid citation found: [E-999] is not defined in EVIDENCE.json", result.stderr)

if __name__ == '__main__':
    unittest.main()
