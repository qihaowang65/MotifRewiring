INCLUDES= -I ./lib/
CC=g++
CFLAGS=-c -O3

SOURCES= lib/nestedmap.cpp lib/matrixrewire.cpp lib/homophily.cpp main.cpp
OBJECTS=$(SOURCES:.cpp=.o)
EXECUTABLE=main.exe


all:	$(SOURCES) $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(CC) $(OBJECTS) -o $@

.cpp.o:
	$(CC) $(CFLAGS) $< $(INCLUDES) -o $@  


clean:
	rm main.o
	rm main.exe
	rm lib/*.o
