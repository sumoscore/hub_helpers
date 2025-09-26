
import os

def test_readme_and_docs():
    for mod in os.listdir("modules"):
        path = os.path.join("modules", mod, "README.md")
        assert os.path.exists(path), f"{mod}/README.md is missing"
