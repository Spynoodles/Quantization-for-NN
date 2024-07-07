def min_max_py(list_data):
    min_val = min(list_data)
    max_val = max(list_data)
    return min_val, max_val

def quantise( list):

    min_val,max_val= min_max_py(list)
    for j in range(len(list)):
        list[j]=((list[j]-min_val)*(255)/(max_val-min_val))
        

    return list


def quantise_py(List):
    Stack=[List]
    result=[]
    bool_stack=[]
    temp_stack=[]
    while(Stack):
      
        current=Stack.pop()
        
        #Condition for change in dimension
        if isinstance(current,int):
                bool_stack.append(current)
        else:
            if bool_stack:
                for i in bool_stack:
                    for j in range(i):
                        temp_stack.append(result.pop())
                    result.append(temp_stack)
                    temp_stack=[]
                
                bool_stack=[]
                
            if isinstance(current[0],float):
                current=quantise(current)
                result.append(current)
            else:
                Stack.append(len(current))
                for i in range(len(current)):
                    Stack.append(current[i])
        
    if bool_stack:
                for i in bool_stack:
                    for j in range(i):
                        temp_stack.append(result.pop())
                    bool_stack=[]
                    result.append(temp_stack)
                    temp_stack=[]
    return result
            




