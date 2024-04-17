CXX = g++
CXXFLAGS = --std=c++11 -O0

impossible.o: impossible.cpp
	$(CXX) $(CXXFLAGS) impossible.cpp -o $@

.PHONY: clean
clean:
	rm -vrf *.o *.exe *.gch *.dSYM *.stackdump *.out