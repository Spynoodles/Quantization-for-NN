# quantise.pyx

#cython: boundscheck=False
#cython: wraparound=False
#cython: initializedcheck=False
#cython: nonecheck=False
#cython: cdivision=True



def dequantise(list):
    cdef double min_val = list[0]
    cdef double max_val = list[0]
    cdef int j
    cdef int length=len(list)
    for j in range(length):
        if list[j] < min_val:
            min_val = list[j]
        if list[j] > max_val:
            max_val = list[j]
    for j in range(length):
        list[j] = round(((list[j] + (min_val* 255 / (max_val - min_val))) * 255 / (max_val - min_val)),2)
    print(list)
    return list 




def quantise(list):

    cdef double min_val = list[0]
    cdef double max_val = list[0]
    cdef int j
    cdef int length=len(list)
    for j in range(length):
        if list[j] < min_val:
            min_val = list[j]
        if list[j] > max_val:
            max_val = list[j]
    for j in range(length):
        list[j] = ((list[j] - min_val) * 255 / (max_val - min_val))

    return list




def DQI(List):

    cdef list Stack = [List]
    cdef list result = []
    cdef list bool_stack =[]
    cdef list temp_stack =[]    



    cdef int i
    cdef int j
    while((Stack)):
       
            
        current=Stack.pop()
        #Condition for change in dimension
        if isinstance(current,int):
           
            bool_stack.append(current)
        else:
            if bool_stack:
                for i in range(len(bool_stack)):
                    for j in range(bool_stack[i]):
                        temp_stack.append(result.pop())
                    result.append(temp_stack)
                    temp_stack=[]
                i=0
                j=0
                bool_stack=[]
                
            if isinstance(current[0],float):
                current=dequantise(current)
                result.append(current)
            else:
                Stack.append(len(current))
                #One change here (Removed Manual looping)
                Stack.extend(current)
        
    if bool_stack:
        for i in range((len(bool_stack))):
            for j in range(bool_stack[i]):
                temp_stack.append(result.pop())
            result.append(temp_stack)
            temp_stack=[]
        
        bool_stack=[]
    return result






def QI(List):

    cdef list Stack = [List]
    cdef list result = []
    cdef list bool_stack =[]
    cdef list temp_stack =[]    



    cdef int i
    cdef int j
    while((Stack)):
       
            
        current=Stack.pop()
        #Condition for change in dimension
        if isinstance(current,int):
           
            bool_stack.append(current)
        else:
            if bool_stack:
                for i in range(len(bool_stack)):
                    for j in range(bool_stack[i]):
                        temp_stack.append(result.pop())
                    result.append(temp_stack)
                    temp_stack=[]
                i=0
                j=0
                bool_stack=[]
                
            if isinstance(current[0],float):
                current=quantise(current)
                result.append(current)
            else:
                Stack.append(len(current))
                #One change here (Removed Manual looping)
                Stack.extend(current)
        
    if bool_stack:
        for i in range((len(bool_stack))):
            for j in range(bool_stack[i]):
                temp_stack.append(result.pop())
            result.append(temp_stack)
            temp_stack=[]
        
        bool_stack=[]
    return result

