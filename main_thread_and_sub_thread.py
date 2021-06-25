import threading

def print_number(n):	
	print(n,threading.current_thread(),end=' ')

class solution:

	def sub_thread(self,print_number):
		self.lock_sub.acquire()
		t = self.turn
		for i in range(t,self.n+1):
			if self.turn > self.n:
				break
			elif (self.turn-1)//10%3 == 0:
				if self.main_lock.locked():
					self.main_lock.release()	
				self.lock_sub.acquire()
			else:
				print_number(self.turn)
				print()
				self.turn += 1
		if self.main_lock.locked():
			self.main_lock.release()

	def main_thread(self,num,print_number):
		if (num-1)//10%3!=0:
			self.main_lock.acquire()
		else:
			print_number(num)
			print()
		self.turn += 1		

	def print_number_using_thread(self,n,print_number):
		self.lock_sub = threading.Lock()
		self.main_lock = threading.Lock()
		self.lock_sub.acquire()
		self.n = n
		t = threading.Thread(target=self.sub_thread,args=(print_number,))
		t.start()
		self.turn = 1
		for i in range(1,self.n+1):
			if self.turn > self.n:
				break
			elif (self.turn-1)//10%3!= 0:
				self.main_lock.acquire()
				self.lock_sub.release()
			else:
				self.main_thread(self.turn,print_number)
		if self.main_lock.locked():
			self.main_lock.release()
		if self.lock_sub.locked():			
			self.lock_sub.release()

n = int(input())
s = solution().print_number_using_thread(n,print_number)