CXX = clang++-15
CFLAGS = -Wall
LDFLAGS =
OBJFILES = fib.o 
TARGET = fib
all: $(TARGET)
$(TARGET): $(OBJFILES)
	$(CXX) $(CFLAGS) -o $(TARGET) $(OBJFILES) $(LDFLAGS)
clean:
	rm -f $(OBJFILES) $(TARGET) *~