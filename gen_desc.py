from pathlib import Path
import toml

# Get the current directory
this_directory = Path(__file__).parent

# Read the contents of your README file
long_description = (this_directory / "README.md").read_text()

# Load the current pyproject.toml file
with open('pyproject.toml', 'r') as f:
    pyproject_dict = toml.load(f)

# Update the long_description field
pyproject_dict['tool']['poetry']['description'] = long_description

# Write the updated pyproject.toml file
with open('pyproject.toml', 'w') as f:
    toml.dump(pyproject_dict, f)