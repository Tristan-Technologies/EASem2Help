import _thread
import time
 
def firstThread():
  while True:
    print("Hello from thread 1")
    time.sleep(1)
    
def secondThread():
    print("Hello from thread 2")
    time.sleep(3)
 
_thread.start_new_thread(firstThread, ())
_thread.start_new_thread(secondThread, ())