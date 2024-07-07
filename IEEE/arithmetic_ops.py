from IEEE_FUNCTION import DeQuantize
from IEEE_FUNCTION import toIEEE64


def add(num1,num2):
    return toIEEE64( DeQuantize(num1)+DeQuantize(num2))
def subtract(num1,num2):
    return toIEEE64(DeQuantize(num1)-DeQuantize(num2))

def multiply(num1,num2):
    return toIEEE64(DeQuantize(num1)*DeQuantize(num2))

def divide(num1,num2):
    return toIEEE64(DeQuantize(num1)/DeQuantize(num2) )


