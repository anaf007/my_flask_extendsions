#coding=utf-8
"""
创建一个简单的堆栈结构
"""

class PyStack:

    def __init__(self,size=20):
        self.stack = []     #堆栈列表
        self.size = size    #堆栈大小
        self.top = -1       #栈顶位置

    def setSize(self,size):
        self.size = size

    def push(self,element):
        if self.isFull():
            raise StackException('PyStackOverflow') #栈满则引发异常
        else:
            self.stack.append(element)
            self.top = self.top+1

    def pop(self):
        if self.isEmpty():
            raise StackException('PyStackUnderflow') #如果栈空引发异常
        else:
            element = self.stack[-1]
            self.top = self.top -1
            del self.stack[-1]
            return element

    def Top(self):
        return self.top

    def empty(self):
        self.stack = []
        self.top = -1

    def isEmpty(self):   #栈空
        if self.top == -1:
            return True
        else:
            return False

    def isFull(self):   #栈满
        if self.top == self.size -1:
            return True
        else:
            return False


#自定义异常类
class StackException(Exception):

    def __init__(self,data):
        self.data = data
    def __str__(self):
        return self.data


if __name__ == '__main__':

    stack = PyStack()#创建栈
    for i in range(10):
        stack.push(i)

    #栈顶位置
    print(stack.Top())

    #出栈
    for i in range(10):
        print(stack.pop())

    stack.empty()

    try:
        #此处引发异常,size设定20

        for i in range(21):
            stack.push(i)
    except Exception, e:
        print(str(e))
    
        



