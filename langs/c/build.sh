#!/bin/bash

# Configuration
CC=gcc
CFLAGS="-Wall -Wextra -std=c11"
CONFIG_FILE="./config.cfg"

SRC_DIR="./src"
BUILD_DIR="./build"
INCLUDE_DIR="./include"
LIBS_DIR="./libs"

# Find all .c files in the source and libraries directories
SRC_FILES=$(find "$SRC_DIR" -name '*.c')
LIB_SRC_FILES=$(find "$LIBS_DIR" -name '*.c')

# Combine source and library .c files
ALL_SRC_FILES="$SRC_FILES $LIB_SRC_FILES"

# Find all include directories and header files
INCLUDE_DIRS=$(find "$SRC_DIR" -type d)
LIB_INCLUDE_DIRS=$(find "$LIBS_DIR" -type d -name 'include')
LIB_INCLUDES=$(for dir in $LIB_INCLUDE_DIRS; do echo -I"$dir"; done)
HEADER_FILES=$(find "$SRC_DIR" -name '*.h'; find "$LIBS_DIR" -name '*.h')

# Find all library files (.a)
LIB_FILES=$(find "$LIBS_DIR" -type f -name '*.a')

# Define the target
TARGET="$BUILD_DIR/main"

# Function to build the project
build() {
    mkdir -p "$BUILD_DIR"
    $CC $CFLAGS $LIB_INCLUDES $(for dir in $INCLUDE_DIRS; do echo -I"$dir"; done) -o "$TARGET" $ALL_SRC_FILES $LIB_FILES
}

# Function to run the program
run() {
    if [ -f "$TARGET" ]; then
        ./"$TARGET"
    else
        echo "Build the project first!"
    fi
}

# Function to clean up
clean() {
    rm -rf "$BUILD_DIR"/*
}

# Check for arguments
case "$1" in
    "build")
        build
        ;;
    "run")
        run
        ;;
    "clean")
        clean
        ;;
    *)
        echo "Usage: $0 {build|run|clean}"
        ;;
esac
