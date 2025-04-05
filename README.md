# absolutely 🔍

**Automatically generate absolute Python imports and relative file paths from a project directory.**

---

## 🚀 What is it?

`absolutely` is a lightweight Python script that walks through your project directory and generates:

- 🐍 Absolute import paths for all Python modules (excluding `__init__.py` and `__pycache__`)
- 📁 Relative paths to all non-Python files (e.g., configs, data, assets)

Perfect for large projects where import statements or file references are hard to track manually.

---

## 📂 Example Use Case

You have a project folder like this:
project/ 
├── utils/ 
│ └── tools.py 
├── data/ 
│ └── sample.json 
├── main.py 
  └── init.py


Running `absolutely` will generate a file like this:

=== ABSOLUTE IMPORTS (Python Modules) ===
from utils.tools import * from main import *

=== RELATIVE FILE PATHS (Non-Python Files) ===
data/sample.json


---
## ⚙️ How to Use
### 1. Set Your Base Path
Edit the script and point `base_path` to the root of your project:
```python
base_path = Path(r"C:\Users\USER\Documents\pythonscripts")
```
---

2. Run the Script
Just run the script with Python:
python absolutely.py
---

3. Output
It creates an absolute_imports.txt file in your project root with two sections:
✅ Absolute Python imports
📄 Relative file links (non-.py)
---

📦 Output Example
# === ABSOLUTE IMPORTS (Python Modules) ===

from shadowbrief.utils.tools import *
from shadowbrief.main import *

# === RELATIVE FILE PATHS (Non-Python Files) ===

data/sample.json
assets/config.yaml


🧠 Why?
Simplify refactoring in large Python codebases
Generate boilerplate imports for tools, scripts, or test runners
Track non-Python assets for packaging or processing


🛠️ Dependencies
Only built-in modules are used:
pathlib


📄 License
MIT — do what you want, just don't blame me if it explodes. 💥



