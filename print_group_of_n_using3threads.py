import threading

def print_num(n):
    print(n,threading.current_thread())

class Solution:
    def __init__(self, n):
        self.n = n*5
        self.x = 1
        self.first_lock = threading.Lock()
        self.second_lock = threading.Lock()
        self.third_lock = threading.Lock()
        self.second_lock.acquire()
        self.third_lock.acquire()

    def first(self, print_num):
        self.first_lock.acquire()
        for i in range(self.x,self.n+1):
            if self.x >= self.n+1:
                break
            self.x += 1
            print_num(self.x-1)
            if i%5 == 0:
                self.second_lock.release()
                self.first_lock.acquire()
        if self.second_lock.locked():
            self.second_lock.release()        

    def second(self, print_second):
        self.second_lock.acquire()
        for i in range(self.x,self.n+1):
            if self.x >= self.n+1:
                break
            self.x += 1
            print_num(self.x-1)
            if i%5 == 0:
                self.third_lock.release()
                self.second_lock.acquire()
        if self.third_lock.locked():
            self.third_lock.release()        

    def third(self, print_third):
        self.third_lock.acquire()
        for i in range(self.x,self.n+1):
            if self.x >= self.n+1:
                break
            self.x += 1
            print_num(self.x-1)
            if i%5 == 0:
                self.first_lock.release()
                self.third_lock.acquire()  
        if self.first_lock.locked():
            self.first_lock.release()                 

s = Solution(int(input()))
t1=threading.Thread(target=s.first,args=(print_num,))
t2=threading.Thread(target=s.second,args=(print_num,))
t3=threading.Thread(target=s.third,args=(print_num,)) 
t1.start()
t2.start()
t3.start()       