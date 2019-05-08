import os
import urllib.request
from threading import Thread

urls = ["https://www.irs.gov/pub/irs-pdf/f1040.pdf",
        "https://www.irs.gov/pub/irs-pdf/f1040a.pdf",
        "https://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
        "https://www.irs.gov/pub/irs-pdf/f1040es.pdf",
        "https://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]


class DownloadThread(Thread):
    """ A threading example that can download a file """

    def __init__(self, url, name):
        """Initialilze the tread"""
        Thread.__init__(self)
        self.name = name
        self.url = url

    def run(self):
        """Run the thread"""
        handle = urllib.request.urlopen(self.url)
        if "Downloads" not in os.listdir(os.getcwd()):
            os.mkdir("Downloads")
        fname =  os.path.join("Downloads", os.path.basename(self.url))
        with open(fname, "wb") as f_handler:
            while True:
                chunk = handle.read(1024)
                if not chunk:
                    break
                f_handler.write(chunk)
        msg = "%s has finished downloading %s!" % (self.name, self.url)
        print(msg)


def main(urls):
    """Run the program"""
    for item, url in enumerate(urls):
        name = "Thread %s" % (item+1)
        thread = DownloadThread(url, name)
        thread.start()

if __name__ == "__main__":
    main(urls)
