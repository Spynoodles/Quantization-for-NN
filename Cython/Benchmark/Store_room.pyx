
cdef extern from "Stack_class.cpp":
    cdef cppclass Stack[T]:
        Stack() except +
        void push(const T& element)
        T pop()
        int getterlen() const
        vector[T] getterArray() const

cdef class PyStack:
    cdef Stack[T]* stack_ptr

    def __cinit__(self):
        self.stack_ptr = new Stack[object]()

    def __dealloc__(self):
        del self.stack_ptr

    def push(self, element):
        self.stack_ptr.push(element)

    def pop(self):
        return self.stack_ptr.pop()

    def getterlen(self):
        return self.stack_ptr.getterlen()

    def getterArray(self):
        cdef vector[object] array = self.stack_ptr.getterArray()
        return list(array)

def main():
    cdef PyStack x=PyStack()
    x.push(10)
    x.push(20)
    while x.getterlen() > 0:
        print("Popped element:", x.pop())



