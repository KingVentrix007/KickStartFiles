# Include the configuration file
include config.mk

# Directories
CMD_DIR=cmd/$(PROJECT_NAME)

# Build the Go project
build:
	go build -o $(PROJECT_NAME) ./$(CMD_DIR)

# Run the Go project
run:
	./$(PROJECT_NAME)

# Test the Go project
test:
	go test ./...

# Clean up build artifacts
clean:
	rm -f $(PROJECT_NAME)

# Install dependencies (if needed)
deps:
	go mod tidy

# Build and run the project
all: deps build run
