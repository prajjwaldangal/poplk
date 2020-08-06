from pycparser import parse_file

hook = '/home/prajjwal/openPOWERLINK/apps/demo_cn_console/src/main.c'
def dfs(filenamePath):
    ast = parse_file(filenamePath, 
            use_cpp=True, 
            cpp_path='/usr/bin/cpp',
            cpp_args=['-E', r'-I~/cparse/utils/fake_libc_include', r'-I~/openPOWERLINK/stack/'])

dfs(hook)

