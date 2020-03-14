from Stack.python_stack import Stack

def baseConverter(decNumber,base):
    #'''十进制转换为十六以下任意进制'''
    digits = '0123456789ABCDEF'

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ''
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

print(baseConverter(123,10))
