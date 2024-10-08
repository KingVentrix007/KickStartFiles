CC = gcc
CFLAGS = -Wall -Wextra -Werror -std=c11
CONFIG_FILE = ./config.cfg

SRC_DIR = ./src
BUILD_DIR = ./build
INCLUDE_DIR = ./include
LIBS_DIR = ./libs

# Find all .c files in the source directory and libraries directory
SRC_FILES = $(shell find $(SRC_DIR) -name '*.c')
LIB_SRC_FILES = $(shell find $(LIBS_DIR) -name '*.c')

# Combine source and library .c files
ALL_SRC_FILES = $(SRC_FILES) $(LIB_SRC_FILES)

# Find all include directories and header files
INCLUDE_DIRS = $(shell find $(SRC_DIR) -type d)
LIB_INCLUDE_DIRS = $(shell find $(LIBS_DIR) -type d -name 'include')
LIB_INCLUDES = $(foreach dir,$(LIB_INCLUDE_DIRS),-I$(dir))
HEADER_FILES = $(shell find $(SRC_DIR) -name '*.h') $(shell find $(LIBS_DIR) -name '*.h')

# Find all library files (.a)
LIB_FILES = $(wildcard $(LIBS_DIR)/*/lib/*.a)

# Define the target
TARGET = $(BUILD_DIR)/main

# Build rules
all: $(TARGET)

$(TARGET): $(ALL_SRC_FILES)
	@mkdir -p $(BUILD_DIR)
	$(CC) $(CFLAGS) $(LIB_INCLUDES) $(foreach dir,$(INCLUDE_DIRS),-I$(dir)) -o $@ $^ $(LIB_FILES)

# Run the program
run: $(TARGET)
	./$(TARGET)

# Clean up
clean:
	rm -rf $(BUILD_DIR)/*

# Declare phony targets
.PHONY: all clean run
