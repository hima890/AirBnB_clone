import os
import importlib
import inspect


def get_python_files(directory):
    """Recursively get all Python files in a directory."""
    python_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    return python_files


def module_docstring(module):
    """Check if a module has a docstring."""
    return bool(module.__doc__)


def class_docstring(cls):
    """Check if a class has a docstring."""
    return bool(cls.__doc__)


def function_docstring(func):
    """Check if a function has a docstring."""
    return bool(func.__doc__)


def check_documentation(module_name):
    """Check documentation for a module, its classes, and functions."""
    module = importlib.import_module(module_name)
    if not module_docstring(module):
        print(f"Module {module_name} is missing a docstring.")
    
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and obj.__module__ == module_name:
            if not class_docstring(obj):
                print(f"Class {name} in module {module_name} is missing a docstring.")
            for func_name, func in inspect.getmembers(obj, inspect.isfunction):
                if not function_docstring(func):
                    print(f"Function {func_name} in class {name} of module {module_name} is missing a docstring.")
        elif inspect.isfunction(obj):
            if not function_docstring(obj):
                print(f"Function {name} in module {module_name} is missing a docstring.")

if __name__ == "__main__":
    # Assuming this script is in the root of your project directory
    project_root = os.path.dirname(os.path.abspath(__file__))
    python_files = get_python_files(project_root)

    # Convert file paths to module names
    module_names = [os.path.splitext(os.path.relpath(file, project_root))[0].replace(os.sep, '.') for file in python_files]

    # Check documentation for each module
    for module_name in module_names:
        check_documentation(module_name)
