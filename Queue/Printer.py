import random
from Queue.python_queue import Queue

class Printer:
    '''param:
    ppm: pagesPerMinute ,每分钟打印多少 '''
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None
    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages()*60/self.pagerate

class Task:
    def __init__(self, time):
        self.timestamp = time#任务生成时间戳
        self.pages = random.randrange(1,21) #初始化打印页数

    def getStamp(self):
        #任务生成时间
        return self.timestamp

    def getPages(self):
        #任务有多少页
        return self.pages

    def waitTime(self, currenttime):
        #当前时间-生成时间=等待时间
        return currenttime - self.timestamp

def newPrintTask():
    '''1/180概率生成作业'''
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

def simulation(numSecond, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSecond):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait = sum(waitingtimes)/len(waitingtimes)

    print('Average Wait %6.2f secs %3d tasks remaining.'%(averageWait, printQueue.size()))

for i in range(10):
    simulation(7200, 5)
