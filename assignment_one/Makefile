CC = clang++
CFLAGS = -Wall
LDFLAGS =
OBJFILES = factorial.o 
TARGET = factorial
all: $(TARGET)
$(TARGET): $(OBJFILES)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJFILES) $(LDFLAGS)
clean:
	rm -f $(OBJFILES) $(TARGET) *~