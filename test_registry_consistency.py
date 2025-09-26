
import json
import os

def test_registry_consistency():
    for reg_file in os.listdir("registry"):
        if reg_file.endswith(".json"):
            path = os.path.join("registry", reg_file)
            with open(path) as f:
                data = json.load(f)
            assert "module" in data and data["module"] in os.listdir("modules"), f"{reg_file} registry mismatch"
