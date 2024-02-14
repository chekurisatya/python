'''
Class Excercises
'''
class Clock():
    
    time = "12.00"
    name = "My Name is Clock Class"
    def __init__(self, time, name):
        self.time = time
        self.name = name
    
    def print_time(self):
        print (self.time)
    
    def print_new_time(self, time):
        print (time)

C1 = Clock('5.30',"Hello I am an Class Instance Clock")
C1.print_time()
C1.time
C1.print_new_time('10.30')
Clock.time
Clock.name


boston_clock = Clock('5:30',"Hello")
paris_clock = boston_clock
paris_clock.time = '10.30'
boston_clock.print_time()

#Simulating the Queue Class
class Queue():
    
    def __init__(self, que=[]):
        self.que = que
    
    def insert(self, element):
        self.que.append(element)
    
    def remove(self):
        if len(self.que):
            return self.que.pop(0)
        else:
            return f"The Queue is Empty"

queue = Queue([])
queue.insert(5)
queue.insert(6)
print(queue.remove())
queue.insert(7)
print(queue.remove())
print(queue.remove())
print(queue.remove())
