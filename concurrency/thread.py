import random
import time

from threading import Thread

class MyThread(Thread):
    """ A Threading example"""
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        """run the thread"""
        amount = 4#random.randint(3,15)
        #time.sleep(amount)
        msg = f"{self.name} is running"
        print(msg)

def create_threads():
    """Create a group of concurrency"""
    for i in range(10):
        name = f"Thread #{i+1}"
        my_thread = MyThread(name)
        my_thread.start()

if __name__ == "__main__":
    create_threads()
