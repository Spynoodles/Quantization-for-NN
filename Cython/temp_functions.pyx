
cdef void min_max(list[float] list, int n, float* min_val, float* max_val):
    cdef int i
    min_val[0] = list[0]
    max_val[0] = list[0]
    for i in range(n):
        if list[i] < min_val[0]:
            min_val[0] = list[i]
        if list[i] > max_val[0]:
            max_val[0] = list[i]
    return









cdef list[int] quantise2(list[float] list):

    cdef int* n=<int*> malloc(sizeof(int))
    n[0]=len(list)
    cdef float* min_val=<float*>malloc(sizeof(float))
    cdef float* max_val=<float*>malloc(sizeof(float))
    cdef int j
    min_max(list,n[0],min_val,max_val)
    for j in range(n[0]):
        list[j]=<int>((list[j]-min_val[0])*(255)/(max_val[0]-min_val[0]))
        
    free(n)
    free(min_val)
    free(max_val)
    return list

