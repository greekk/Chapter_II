import os
import urllib.request
from threading import Thread
from queue import Queue

urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf"
        "http://www.irs.gov/pub/irs-pdf/f1040es.pdf"
        "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]

class Downloader(Thread):
    """Threaded File Downloader"""

    def __init__(self, queue):
        """Initialize the thread"""
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        """Run the thread"""
        while True:
            #gets the url form the queue
            url = self.queue.get()

            #download the file
            self.download_file(url)

            #send signal to the queue that the job is done
            self.queue.task_done()

    def download_file(self, url):
        """Download the file"""
        handle = urllib.request.urlopen(url)
        fname = os.path.basename(url)
        with open(fname, "wb") as f:
            while True:
                chunk = handle.read(1024)
                if not chunk: break
                f.write(chunk)

def main():
    """Run the program"""
    queue = Queue()
    #create a thread pool and give them a queue
    for i in range(5):
        t = Downloader(queue)
        t.setDaemon(True)
        t.start()

    #give the queue some data
    for url in urls:
        queue.put(url)

    #wait for the queue to finish
    queue.join()

if __name__ == "__name__":
    main()

