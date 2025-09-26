
import json

def test_golden_output_compliance():
    import glob
    files = glob.glob("golden/*.jsonl")
    for f in files:
        with open(f) as fp:
            for i, line in enumerate(fp):
                obj = json.loads(line)
                assert "signal_id" in obj or "setup_id" in obj, f"{f} line {i+1} missing signal_id/setup_id"
