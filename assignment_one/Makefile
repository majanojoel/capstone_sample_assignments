CXX = clang++-15
CFLAGS = -Wall
LDFLAGS =
OBJFILES = factorial.o 
TARGET = factorial
all: $(TARGET)
$(TARGET): $(OBJFILES)
	$(CXX) $(CFLAGS) -o $(TARGET) $(OBJFILES) $(LDFLAGS)
clean:
	rm -f $(OBJFILES) $(TARGET) *~