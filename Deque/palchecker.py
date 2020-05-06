from Deque.python_deque import Deque

def palchecker(aString):
    '''回文数判断'''
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size()>1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

print(palchecker('radar'))
print(palchecker('lssddw'))


