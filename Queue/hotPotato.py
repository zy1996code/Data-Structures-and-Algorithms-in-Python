from Queue.python_queue import Queue

def hotPotato(namelist, num):
    '''如何实现土豆传递？
       首先有n个人入队，然后通过循环出队入队执行要求次数， 这里要求一轮循环执行7次， 然后让队首拿土豆的人出队，在对剩下n-1个人进行循环7次，这样往复执行最后剩下的人即为最胜出者

    '''
    simqueue = Queue() #模拟一个队列
    for name in namelist:
        simqueue.enqueue(name)
    while simqueue.size()>1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
            '''相当于报数到 num 就离席'''
        simqueue.dequeue()

    return simqueue.dequeue()




print(hotPotato(['Bill','David','Susan','Jave','Kent','Brad'],3))



