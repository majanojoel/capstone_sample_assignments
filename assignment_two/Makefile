CC = clang++
CFLAGS = -Wall
LDFLAGS =
OBJFILES = enoughCharacters.o 
TARGET = enoughCharacters
all: $(TARGET)
$(TARGET): $(OBJFILES)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJFILES) $(LDFLAGS)
clean:
	rm -f $(OBJFILES) $(TARGET) *~