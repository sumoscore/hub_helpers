
import os

def test_file_naming_conventions():
    for root, dirs, files in os.walk("modules"):
        for file in files:
            assert file == file.lower(), f"{file} should be lowercase"
