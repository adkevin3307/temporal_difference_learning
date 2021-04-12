EXE = 2048
OBJ_DIR = obj
TRASH = .cache

SOURCES = $(wildcard *.cpp)
OBJS = $(addprefix $(OBJ_DIR)/, $(addsuffix .o, $(basename $(notdir $(SOURCES)))))

CXXFLAGS = -std=c++11 -Wall -O3 -g

LIBS =

ifeq ($(findstring debug, $(MAKECMDGOALS)), debug)
	CXXFLAGS += -DDEBUG
endif

all debug: create_object_directory $(EXE)
	@echo Compile Success

create_object_directory:
	mkdir -p $(OBJ_DIR)

$(OBJ_DIR)/%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c -o $@ $<

$(EXE): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LIBS)

clean:
	rm -rf $(EXE) $(OBJ_DIR) $(TRASH)
