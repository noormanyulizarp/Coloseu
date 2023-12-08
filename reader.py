# Root directory structure:
# .
# ├── main.py
# ├── poetry.lock
# ├── pyproject.toml
# ├── reader.py
# └── replit.nix

# Files:
# root/reader.py

import os


def print_file_contents(startpath):
  for root, dirs, files in os.walk(startpath):
    for file in files:
      path = os.path.join(root, file)
      print(f"\nContents of {path}:\n" + "-" * 50)
      try:
        with open(path, 'r') as f:
          print(f.read())
      except Exception as e:
        print(f"Error reading file {path}: {e}")


print_file_contents('.')
