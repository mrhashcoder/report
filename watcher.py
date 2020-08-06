import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

class Watcher:
    DIRECTORY_TO_WATCH = "C:\\Users\\abhis\\Desktop\\report"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print ("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
        else:
            os.system('git add .')
            os.system('git commit -m "report"')
            os.system('git push')
            print("done")
            

    @staticmethod
    def on_deleted(event):
        print("file deleted")

    @staticmethod
    def on_moved(event):
        print("moved a file")    

if __name__ == '__main__':
    w = Watcher()
    w.run()