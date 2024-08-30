# Include the configuration file with path definitions
# Paths
SRC_PATH = src
INCLUDE_PATH = include
BUILD_PATH = build
TESTS_PATH = tests

# Output file
OUTPUT_FILE = ${project_name}

# Compiler and flags
CXX = g++
CXXFLAGS = -Wall -Wextra -I$(INCLUDE_PATH) -std=c++17

# Source, object, and executable paths
SRC = $(wildcard $(SRC_PATH)/*.cpp)
OBJ = $(SRC:$(SRC_PATH)/%.cpp=$(BUILD_PATH)/%.o)
TARGET = $(BUILD_PATH)/$(OUTPUT_FILE)
TESTS = $(wildcard $(TESTS_PATH)/*.cpp)
TEST_OBJ = $(TESTS:$(TESTS_PATH)/%.cpp=$(BUILD_PATH)/%.o)

# Default target
all: $(TARGET)

# Build the target executable
$(TARGET): $(OBJ)
	@mkdir -p $(BUILD_PATH)
	$(CXX) $(CXXFLAGS) -o $@ $^

# Build object files
$(BUILD_PATH)/%.o: $(SRC_PATH)/%.cpp
	@mkdir -p $(BUILD_PATH)
	$(CXX) $(CXXFLAGS) -c -o $@ $<

# Command to run the executable
run: $(TARGET)
	./$(TARGET)

# Build tests
tests: $(TEST_OBJ)
	$(CXX) $(CXXFLAGS) -o $(BUILD_PATH)/tests $(TEST_OBJ)

# Build object files for tests
$(BUILD_PATH)/%.o: $(TESTS_PATH)/%.cpp
	@mkdir -p $(BUILD_PATH)
	$(CXX) $(CXXFLAGS) -c -o $@ $<

# Clean build artifacts
clean:
	rm -rf $(BUILD_PATH)/*

.PHONY: all run tests clean
