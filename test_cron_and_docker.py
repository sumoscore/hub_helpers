
import os

def test_cron_and_docker():
    assert os.path.exists("Dockerfile"), "Dockerfile missing"
    cron = [f for f in os.listdir(".") if f.startswith("cron_") and f.endswith(".sh")]
    assert cron, "No cron_*.sh files found"
