# you can import any package that you need here
# -- write your code here -- 

import threading

def print_n(n):
    print(n,threading.current_thread())

class Solution:

    def __init__(self, n):
        self.n = n
        self.x = 1
        self.char = 3
        self.num_lock = threading.Lock()
        self.char_lock = threading.Lock()
        self.char_lock.acquire()

    def number(self, print_number):
        t = self.x
        for i in range(t,(self.n*2)+self.n+1):
            self.num_lock.acquire()
            if self.x > self.n*2+self.n:
                break
            elif self.x%3 == 0:
                self.char_lock.release()
                self.num_lock.acquire()
                if i < self.n*2 and self.n > 1:
                    print_number(i)
                    self.x += 1
                self.num_lock.release()
            else:
                self.num_lock.release()
                print_number(i)
                self.x += 1

    def character(self, print_character):
        while self.x <= self.n*2+self.n:
            self.char_lock.acquire()
            s = chr(self.char+62)
            print_character(s)
            self.x += 1
            self.char += 1
            self.num_lock.release()

s = Solution(26)
t1 = threading.Thread(target=s.number,args=(print_n,))
t2 = threading.Thread(target=s.character,args=(print_n,))
t1.start()
t2.start()
