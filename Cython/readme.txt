Steps
1:Write the function in pyx file 
2:->Make a setup file ;command for compilation "python setup.py build_ext --inplace"
  ->cythonize -i solution.pyx
3: import the so file and use the functions 


- Some links for reference to cpp python library bindings : https://chat.openai.com/share/ca65590c-27ac-4b8c-a978-95e3e48fce57




Some sample code for array:
from libc.stdlib cimport malloc, free

  cdef void quantise(int* array, int size):
    cdef int i
    for i in range(size):
        array[i] = (array[i] // 10) * 10  # Quantize each element

def quantise_py(list array):
    cdef int* arr_ptr = <int*>malloc(len(array) * sizeof(int))
    if arr_ptr == NULL:
        raise MemoryError("Failed to allocate memory")
    try:
        for i in range(len(array)):
            arr_ptr[i] = array[i]
        
        quantise(arr_ptr, len(array))
        
        # Convert C array back to Python list
        result = [arr_ptr[i] for i in range(len(array))]
    finally:
        free(arr_ptr)  # Free the allocated memory
    return result