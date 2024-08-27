CC = gcc
CFLAGS = -Wall -Wextra -Werror -std=c11
CONFIG_FILE = ./config.cfg

include $(CONFIG_FILE)

# Find all .c files in the source directory
SRC_FILES = $(shell find $(SRC_DIR) -name '*.c')

# Find all include directories and header files
INCLUDE_DIRS = $(shell find $(SRC_DIR) -type d)
LIB_INCLUDE_DIRS = $(shell find $(LIBS_DIR) -name 'include' -type d)
LIB_INCLUDES = $(foreach dir,$(LIB_INCLUDE_DIRS),-I$(dir))
HEADER_FILES = $(shell find $(SRC_DIR) -name '*.h')

# Find all library files
LIB_FILES = $(wildcard $(LIBS_DIR)/*/lib/*.a)

# Define the target
TARGET = $(BUILD_DIR)/main

# Build rules
all: $(TARGET)

$(TARGET): $(SRC_FILES)
	$(CC) $(CFLAGS) $(LIB_INCLUDES) $(foreach dir,$(INCLUDE_DIRS),-I$(dir)) -o $@ $^ $(LIB_FILES)

# Run the program
run: $(TARGET)
	./$(TARGET)

# Clean up
clean:
	rm -rf $(BUILD_DIR)/*

# Declare phony targets
.PHONY: all clean run
