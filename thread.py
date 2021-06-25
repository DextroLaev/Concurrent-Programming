import threading
import time

def calc_square(numbers):
	for n in numbers:
		time.sleep(0.2)
		print('square :',n*n)

def calc_cube(numbers):
	for n in numbers:
		time.sleep(0.2)
		print('cube : ',n*n*n)

arr = [2,3,8,9]

t1 = threading.Thread(target=calc_square,args=(arr,))
t2 = threading.Thread(target=calc_cube,args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()