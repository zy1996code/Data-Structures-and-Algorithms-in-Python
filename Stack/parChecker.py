from Stack.python_stack import Stack
def parChecker(symbolString):
    '''通用括号匹配'''
    s = Stack()
    balanced = True #是否匹配
    i = 0
    while i < len(symbolString) and balanced:
        symbol = symbolString[i]
        if symbol in '({[':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop() #匹配成功就带走，非诚勿扰？
                if not matches(top, symbol):
                    balanced = False
        i = i + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    '''如果两个字符串出现位置相等，则匹配成功'''
    opens = '([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)