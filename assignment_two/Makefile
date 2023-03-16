CXX = clang++-15
CFLAGS = -Wall
LDFLAGS =
OBJFILES = enoughCharacters.o 
TARGET = enoughCharacters
all: $(TARGET)
$(TARGET): $(OBJFILES)
	$(CXX) $(CFLAGS) -o $(TARGET) $(OBJFILES) $(LDFLAGS)
clean:
	rm -f $(OBJFILES) $(TARGET) *~