python-ctypes-test
==================

Sample code to use ctypes Python module for both Linux and Windows platforms  

All interesting things is located in leadwerks directory  

Makefile has two targets windows and linux and compiles
sample code into hello_world.windows.so and hello_world.linux.so respective  

__init__.py is wrapper code to make library functions to be available from
python code in crossplatform manner  

To run test.py on linux use:  
export LD_LIBRARY_PATH=./leadwerks  
python3 test.py
