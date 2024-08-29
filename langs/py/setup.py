try:
    from cx_Freeze import setup, Executable
except Exception:
    print("Module cx_Freeze is missing, please run pip install cv_Freeze to install")
    exit(-1)
import sys
# Define the main script of your application
main_script = "main.py"  # Replace with your main script

# Additional packages required by the application
packages = [
    # List your required packages here, e.g.:
    # "os", "sys", "requests", etc.
]

# Files to be included in the build
include_files = [
    # List additional files or directories to include in the build, e.g.:
    # ("path/to/data", "data"), ("path/to/config.cfg", "config.cfg")
]

# Build options
build_exe_options = {
    "packages": packages,
    "include_files": include_files,
    "include_msvcr": True,  # Include Microsoft Visual C++ Redistributable
}

# Base setup options
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Use this if you're building a GUI application

setup(
    name="MyApplication",  # Replace with your application's name
    version="0.1",
    description="A simple description of your application",
    options={"build_exe": build_exe_options},
    executables=[Executable(main_script, base=base)],
)
