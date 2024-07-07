








#Returns the indexes with the first occurence of 1 and the decimal in the input number
def locate(number):
    index1=0
    index_dot=0
    flag_dot=False
    flag_1=False
    
    for i in range (len(number)):
        if i==0:
            continue
        if number[i]=='1' and flag_1==False:
            index1=i
            flag_1=True
        if number[i]=='.':
            index_dot=i
            flag_dot=True
        if flag_1 and flag_dot:
            return index1,index_dot

#Adds 0's in the front until the length of the number becomes n
def Add_Zero(number,n):
    if len(str(number))>=n:
        return str(number)
    #Remove this if things stop working :(
    flagzero=False
    if float(number)<0:
        flagzero=True

    number=list(str(number))[::-1]
    number=''.join(number)
    while(len(number)!=n):
        number=number+'0'
    number=list(str(number))[::-1]
    number=''.join(number)
    if flagzero:
        number="1"+number[1::]
    return number 

def BinarytoDecimal(number):
    number=round(float(number),4)
    number=str(number)
    whole_part, fractional_part = number.split('.')
    decimal_whole_part = int(whole_part, 2)
    decimal_fractional_part = sum(int(bit)*2**(-i - 1) for i, bit in enumerate(fractional_part))
    if float(number)<0:
        return decimal_whole_part-decimal_fractional_part
    return decimal_whole_part + decimal_fractional_part


#Quantizes the number
#Sign-1Bit Exponent-3Bits Mantissa-4Bits

def toIEEE64(number):
    if(float(number)==0.0):
        return '01110000'
    number=number+"00000000"
    index1,index_dot=locate(number)
    temp=0
    if index1-index_dot>0:
        temp=0
    else:
        temp=1
    if(index1-index_dot+temp+1>7):
        exponent=bin(8)[2:]
        # print(temp2)
        #Remove this if you dont want this logic for denormal numbers
        return "01110000"
    else:
        exponent=(index1-index_dot+temp)+1
        exponent=bin(exponent)[2::]

    exponent=Add_Zero(exponent,3)
    sign=(number[0])
    mantissa=""
    
        # print(temp)
    for i in range(index1+1,index1+6):
        if number[i]!='.':
                mantissa=mantissa+number[i]

    return (sign+exponent+mantissa[0:4])

def DeQuantize(number):
    number=Add_Zero(str(number),8)
    Sign=number[0]
    exponent=int(number[1:4],2)-1

    if Sign=="0":
        mantissa="1."+number[4::]
    else:
        mantissa="-1."+number[4::]
    mantissa=float(mantissa)*10**-exponent
    mantissa=BinarytoDecimal(str(mantissa))
    
    return mantissa




def float_to_binary(num):

    if num < 0:
        sign = '1'
        num = abs(num)
    else:
        sign = '0'

    integer_part = bin(int(num))[2:]
    fractional_part = ''
    
    if '.' in str(num):
        fractional_part = '.'
        num -= int(num)
        while num > 0:
            num *= 2
            fractional_part += str(int(num))
            num -= int(num)

    binary_representation = sign + integer_part + fractional_part
    
    return binary_representation
    

def conversionPlug(num):
    if num[0]==0:
        
        return '-'+num[1::] 
    return num[1::]

def error_calculation():
    error=[]
    avg_error=[]
    temp=[]
    for k in range (2,500,10):
        temp=[]

        for i in range (-3,4):
            for j in range(1,k,1):
                num=i/j
            
                # print(i,j,num ,end=": ")
                floating=float_to_binary(num)
                Quantised=toIEEE64(floating)
                # print(Quantised)
                DeQuantized=DeQuantize(Quantised)
                error.append(abs(num-DeQuantized))
                temp.append(abs(num-DeQuantized))
                # if j>90 and i==1:

                #     print(num-DeQuantized)
                # print(DeQuantized)
        avg_error.append(avg(temp))
    return (error,avg_error)

def avg(list):
    sum=0
    for i in list:
        sum=sum+i
    if(len(list)==0):
        return 0
    return sum/len(list)

error=error_calculation()
# num=float_to_binary(-0.015384615384615385)
# print(num)
# num=DeQuantize(toIEEE64("00.0000001011000000101100000010110000001011000000101100000011"))
# print(num)
# print(0.01075268817204301161-num)



# x = torch.tensor(int(conversionPlug(Quantised),2), dtype=torch.int8)
# print(Add_Zero(bin(x.item())[2::],8))

#_____PLOT___
# print(avg(error[0]))
import matplotlib.pyplot as plot
plot.plot((error[1]))
plot.show()