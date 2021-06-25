import threading


class Solution:
    def _init_(self, n, m):
        self.n = n
        self.m = m
        self.i=1
        self.locks=[]
        for x in range(self.n):
            temp=threading.Lock()
            self.locks.append(temp)
        for x in range(1,self.n):
            self.locks[x].acquire()
        # print(self.locks)

        # -- write your code here --

    # print_number(x) outputs "x", where x is an integer.
    def print_thread_number(self, print_number, thread_id):
        # -- write your code here --

        while self.i<=self.m:
            if (self.i-1)%self.n==thread_id:
                self.locks[thread_id].acquire()
                print_number(self.i)
                self.i+=1
                if thread_id==self.n-1:
                    self.locks[0].release()
                else:
                    self.locks[thread_id+1].release() 