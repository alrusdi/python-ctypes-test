# hello sample file
hello_program=hello_world.cpp

shared_compliller_flags=-shared

windows:
	g++ -o hello_world.windows.so $(shared_compliller_flags) $(hello_program)

linux:
	g++ -o hello_world.linux.so -fPIC $(shared_compliller_flags) $(hello_program)
