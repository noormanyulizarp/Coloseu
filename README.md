## Usage

1. Open `main.py` and replace 'your_username' and 'your_password' with your actual Instagram credentials.
2. Run the script using Replit's "Run" button.

## Additional Script

### reader.py

The `reader.py` script reads and prints the contents of files in the project directory.

```python
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
