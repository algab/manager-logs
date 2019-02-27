import os
import time
from database import db
from threading import Thread
from app.batch import Batch
from app.file import save_error

class Manager(Thread):
    def run (self):
        while True:
            self.insert_logs()
            time.sleep(int(os.getenv('TIME'))) 
                
    def insert_logs(self):
        try:
            post_logs,get_logs,put_logs,delete_logs = Batch().get_inserts()
            if len(post_logs) != 0:
                db["post_logs"].bulk_write(post_logs)
            if len(get_logs) != 0:
                db["get_logs"].bulk_write(get_logs)
            if len(put_logs) != 0:
                db["put_logs"].bulk_write(put_logs)
            if len(delete_logs) != 0:
                db["delete_logs"].bulk_write(delete_logs)
            Batch().reset()                 
        except Exception as e:
            save_error(e,"INSERT logs")
            