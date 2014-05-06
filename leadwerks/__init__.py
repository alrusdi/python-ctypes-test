import os
import platform
from ctypes import cdll, c_char_p

def __load_library(lib_name):
    '''
    Loads a library by name (without extension)
    i.e. to load somelibrary.so from current directory use:
    my_lib = __load_lib('somelibrary')
    '''
    platform_name = platform.system().lower()
    lib_name = '%s.%s.so' % (lib_name, platform_name)

    # for windows platform we need an absolute path to library
    if platform_name == 'windows':
        cur_dir = os.path.dirname(__file__)
        lib_name = os.path.join(cur_dir, lib_name)
    return cdll.LoadLibrary(lib_name)

__hello_lib = __load_library('hello_world')
	
# Making binging for all needed functions
hello_world = __hello_lib.hello_world
hello_world.restype = c_char_p # declaring return data type
