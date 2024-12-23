# Unused Libraries Checker

This project helps analyze and clean up unused libraries in a Python project. It checks for libraries listed in `requirements.txt` that are not being used in the codebase, and optionally allows you to uninstall them and regenerate a clean `requirements.txt` file.

## Features
- Identify unused libraries from `requirements.txt`.
- Generate a list of unused libraries in a file.
- Optionally uninstall unused libraries.
- Regenerate `requirements.txt` after cleanup.

## Getting Started

### Prerequisites
- Python 3.7+
- pip

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/kolya-trotsko/py-dependency-cleaner.git
   cd unused-libs-checker
   ```

2. Install required libraries (if any):
   ```bash
   pip install -r requirements.txt
   ```

### How to Use

#### 1. Create `requirements.txt`
To create a `requirements.txt` file for your project:
1. Navigate to your project directory.
2. Use `pip freeze` to generate the file:
   ```bash
   pip freeze > requirements.txt
   ```

#### 2. Run the Script
To find unused libraries in your project:
1. Set the paths in the script for:
   - `project_path` (path to your project directory).
   - `requirements_path` (path to your `requirements.txt` file).
   - `output_file_path` (path to save the list of unused libraries, e.g., `unused.txt`).
2. Run the script:
   ```bash
   python script.py
   ```
3. Check the output file (e.g., `unused.txt`) for a list of unused libraries.

#### 3. Uninstall Unused Libraries
To remove unused libraries:
1. Use the generated file (e.g., `unused.txt`) to uninstall them:
   ```bash
   pip uninstall -r unused.txt -y
   ```

#### 4. Regenerate `requirements.txt`
After uninstalling unused libraries, regenerate the `requirements.txt` file:
```bash
pip freeze > requirements.txt
```

### Notes
- Ensure you back up your project or use version control before uninstalling libraries.
- The script may not detect dynamic imports or other less common usage patterns, so double-check the results if necessary.
