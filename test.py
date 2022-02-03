from decimal import ROUND_DOWN
import openpyxl
import pathlib
import os
import pymysql
from google.cloud.sql.connector import connector
import sqlalchemy
import datetime
from datetime import datetime


from datetime import timedelta
import threading
import time

list = [11, 18, 19, 21,24]

length = len(list)

middle_index = round(length / 2)

first_half = list[:middle_index+1]
second_half = list[middle_index+1:]

print(first_half)
print(second_half)




def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# Create two threads as follows
try:
   x1 = threading.Thread(target=print_time, args=('thread-1',1,))
   x1.start()
   x2 = threading.Thread(target=print_time, args=('thread-2',2,))
   x2.start()
   x1.join()
   x2.join()
   print('all done')
except Exception as e:
   print ("Error: unable to start thread")

   


