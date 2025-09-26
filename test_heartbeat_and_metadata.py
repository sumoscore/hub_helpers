
import json
import os

def test_heartbeat_and_metadata():
    for mod in os.listdir("modules"):
        path = os.path.join("modules", mod)
        for fname in ["heartbeat.json", "metadata.json"]:
            fpath = os.path.join(path, f"{fname}")
            assert os.path.exists(fpath), f"{fpath} is missing"
            with open(fpath) as f:
                data = json.load(f)
                assert isinstance(data, dict), f"{fpath} is not valid JSON"
