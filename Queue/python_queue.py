class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item): #把数据项加在对尾 左边是队尾，右边是队首部 在队尾增加数据项
        self.items.insert(0, item)

    def dequeue(self): #在队首移除
        return self.items.pop()

    def size(self):
        return len(self.items)


