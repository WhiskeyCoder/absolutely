from pathlib import Path

base_path = Path(r"C:\Users\USER\Documents\pythonscripts")

def generate_absolute_imports(base_path):
    imports = []
    for path in base_path.rglob("*.py"):
        if "__pycache__" in path.parts or path.name == "__init__.py":
            continue
        relative_path = path.relative_to(base_path)
        module_path = relative_path.with_suffix('').as_posix().replace('/', '.')
        imports.append(f"from {module_path} import *")
    return imports

def generate_relative_file_links(base_path):
    file_links = []
    for path in base_path.rglob("*"):
        if path.is_file() and not path.suffix == ".py" and "__pycache__" not in path.parts:
            relative_path = path.relative_to(base_path).as_posix()
            file_links.append(relative_path)
    return file_links

absolute_imports = generate_absolute_imports(base_path)
relative_links = generate_relative_file_links(base_path)

output_path = base_path / "absolute_imports.txt"
with open(output_path, "w", encoding="utf-8") as f:
    f.write("# === ABSOLUTE IMPORTS (Python Modules) ===\n\n")
    f.writelines(line + "\n" for line in absolute_imports)
    f.write("\n# === RELATIVE FILE PATHS (Non-Python Files) ===\n\n")
    f.writelines(line + "\n" for line in relative_links)

print(f"Done! File saved to: {output_path}")
