
import os

REQUIRED_FILES = ["README.md", "registry.json", "heartbeat.json", "metadata.json"]
REQUIRED_DIRS = ["modules", "golden", "registry", "unified_cache"]

def test_module_structure():
    for mod in os.listdir("modules"):
        mod_path = os.path.join("modules", mod)
        if os.path.isdir(mod_path):
            for req_file in REQUIRED_FILES:
                file_path = os.path.join(mod_path, req_file)
                assert os.path.exists(file_path), f"{mod}/{req_file} is missing"
