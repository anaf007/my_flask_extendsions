#coding=utf-8
"""
简单的队列
"""

class PyQueue:

    def __init__(self,size=20):
        self.queue = []
        self.size = size
        self.end = -1

    def setSize(self,size):
        self.size = size

    #入队
    def In(self,element):   
        if self.end < self.size -1 :
            self.queue.append(element)
            self.end = self.end+1
        else:
            raise QueueException('PyQueueFull') #队满则引发异常

    def Out(self):
        if self.end != -1:
            element = self.queue[0]
            self.queue = self.queue[1:]
            self.end = self.end -1
            return element
        else:
            raise QueueException('PyQueueEmpty') #如果队列为空则引发异常

    def End(self):
        return self.end

    def empty(self):
        self.queue = []
        self.end = -1

class QueueException(Exception):

    def __init__(self,data):
        self.data = data
    def __str__(self):
        return self.data


if __name__ == '__main__':
    queue = PyQueue()

    #元素入队
    for i in range(10):
        queue.In(i)

    #队尾
    print(queue.End())

    #出队
    for i in range(10):
        print(queue.Out())

    queue.empty()

    #此处引发异常
    try:
        for i in range(20):
            print(queue.Out())
    except Exception as e:
        print(str(e))