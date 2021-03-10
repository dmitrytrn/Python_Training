import _ctypes

name = 'Dmitry'
name += '.'
name_ptr = id(name)
print(f'Address of source string : {id(name)}')
name += 'Morozov'
print(f'Address of target string : {id(name)}')
print(_ctypes.PyObj_FromPtr(name_ptr))