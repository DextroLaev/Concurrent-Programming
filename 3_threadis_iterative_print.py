
import threading

def print_number(n):
    print(n,threading.current_thread())

class Solution:

    def __init__(self, n):
        self.n = n
        self.x = n
        self.zero = threading.Lock()
        self.one = threading.Lock()
        self.two = threading.Lock()
        self.one.acquire()
        self.two.acquire()

    def remainder_zero(self, print_number):
        for i in range(self.n,0,-1):
            self.zero.acquire()
            if self.x%3 == 0:
                print_number(self.x)
                self.x -= 1
                self.zero.release()
            elif self.x%3 == 1:
                self.one.release()
            elif self.x%3 == 2:
                self.two.release()          

    def remainder_one(self, print_number):
        while self.x >= 1:
            self.one.acquire()
            if self.x >= 1:
                print_number(self.x)
                self.x -= 1
                self.zero.release()   

    def remainder_two(self, print_number):
        while self.x > 1:
            self.two.acquire()
            if self.x > 1:
                print_number(self.x)
                self.x -= 1
                self.zero.release()

s = Solution(int(input()))
t1 = threading.Thread(target=s.remainder_zero,args=(print_number,))
t2 = threading.Thread(target=s.remainder_one,args=(print_number,))        
t3 = threading.Thread(target=s.remainder_two,args=(print_number,))
t1.start()
t2.start()
t3.start()