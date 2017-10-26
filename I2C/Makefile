TARGET = ADXL345
OBJECT = ADXL345.o
CC = gcc
LINK_FLAGS = -lwiringPi
C_FLAGS = -Wall -g 

ALL : $(TARGET)
.PHONY : clean

$(TARGET): $(OBJECT)
	$(CC) $^ $(LINK_FLAGS) -o $@

%.o : %.c
	$(CC) $(C_FLAGS) -c $< 
clean:
	-rm -f $(TARGET) $(OBJECT)
