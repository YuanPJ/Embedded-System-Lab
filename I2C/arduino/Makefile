#The following macros should be defined. 
TARGET1=async-i2c
OBJECT1=async-i2c.o
CC=gcc 
CXX=g++ 
LD=gcc
LD_FLAGS =
LD_FLAGS += -lwiringPi
#LD_FLAGS += -lncurses -pthread  
#C_FLAGS= -g -O0 
C_FLAGS= -Wall
# end of user configuration 
#
ALL : $(TARGET1)  $(TARGET2)
$(TARGET1) : $(OBJECT1) 
	$(LD)  $^ $(LD_FLAGS) -o $@ 
%.o : %.c 
	$(CC) $(C_FLAGS) -c $< 
%.o : %.cpp 
	$(CXX) $(C_FLAGS) -c $< 
.PHONY: clean 
clean : 
	-rm -f $(OBJECT1) $(OBJECT2) $(TARGET1) $(TARGET2)
