# Compiler
CC = gcc

# Compiler flags
CFLAGS = -Wall -Wextra -g

# Target executable name
TARGET = myapp

# Source files
SRCS = src/main.c src/utils.c

# Object files
OBJS = $(SRCS:.c=.o)

# Default target
all: $(TARGET)

# Rule to build the target executable
$(TARGET): $(OBJS)
    $(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

# Rule to build the object files and handle header dependencies
src/%.o: src/%.c src/utils.h
    $(CC) $(CFLAGS) -c $< -o $@

# Clean up generated files
clean:
    rm -f $(TARGET) $(OBJS)

# Phony targets
.PHONY: all clean
