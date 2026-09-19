import os
import importlib

def load_modules():
    modules = {}
    modules_dir = os.path.join(os.path.dirname(__file__), "..", "modules")
    
    if not os.path.exists(modules_dir):
        return modules

    for file in os.listdir(modules_dir):
        if file.endswith(".py") and file != "__init__.py":
            module_name = file[:-3]
            try:
                mod = importlib.import_module(f"modules.{module_name}")
                if hasattr(mod, "Module"):
                    instance = mod.Module()
                    modules[module_name] = instance
            except Exception as e:
                print(f"[!] Error loading module '{module_name}': {e}")
                
    return modules