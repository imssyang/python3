import importlib.util
import sys

# For illustrative purposes.
import tokenize

file_path = tokenize.__file__
module_name = tokenize.__name__
print(f"file_path: {file_path} module_name: {module_name}")

spec = importlib.util.spec_from_file_location(module_name, file_path)
print(spec)
module = importlib.util.module_from_spec(spec)
print(module)
sys.modules[module_name] = module
spec.loader.exec_module(module)
