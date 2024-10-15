import os
import subprocess
import sys

# Configuration
CC = "gcc"
CFLAGS = "-Wall -Wextra -std=c11"
SRC_DIR = "./src"
BUILD_DIR = "./build"
LIBS_DIR = "./libs"
TARGET = os.path.join(BUILD_DIR, "main")

# Helper functions
def find_files(directory, extension):
    return [os.path.join(root, file) for root, _, files in os.walk(directory) for file in files if file.endswith(extension)]

def build():
    os.makedirs(BUILD_DIR, exist_ok=True)
    src_files = find_files(SRC_DIR, ".c") + find_files(LIBS_DIR, ".c")
    lib_files = find_files(LIBS_DIR, ".a")

    includes = ' '.join(f"-I{d}" for d in find_files(SRC_DIR, "") if os.path.isdir(d)) + \
               ' '.join(f"-I{d}" for d in find_files(LIBS_DIR, "include") if os.path.isdir(d))

    command = f"{CC} {CFLAGS} {includes} -o {TARGET} " + ' '.join(src_files) + ' ' + ' '.join(lib_files)
    print("Running:", command)
    subprocess.run(command, shell=True)

def run():
    if os.path.isfile(TARGET):
        subprocess.run([f"./{TARGET}"])
    else:
        print("Please build the project first.")

def clean():
    if os.path.exists(BUILD_DIR):
        for root, dirs, files in os.walk(BUILD_DIR):
            for file in files:
                os.remove(os.path.join(root, file))
        print("Cleaned build directory.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python build.py {build|run|clean}")
    else:
        action = sys.argv[1]
        if action == "build":
            build()
        elif action == "run":
            run()
        elif action == "clean":
            clean()
        else:
            print(f"Unknown action: {action}")
