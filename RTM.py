import psutil
import time
import threading
import csv
import os
import numpy as np
import datetime

elements = []
total_time = []

csvfile = "cassandra-workloada.csv"

from datetime import datetime
count = 10
copy_delay = 60
print datetime.now()
def printit():
  start = time.time()
  threading.Timer(1.0, printit).start()
  cpu_percent = psutil.cpu_percent(interval=1)
  if cpu_percent <=33:
    util_level = "low"
  if cpu_percent >33 and cpu_percent <66:
    util_level = "medium"
  if cpu_percent >=66:
    util_level = "high"

  u = util_level
  x = psutil.cpu_times() + (psutil.cpu_percent(interval=1),) + psutil.virtual_memory() + psutil.swap_memory() + psutil.disk_usage('/') + psutil.disk_io_counters() + (u,)

  elements.append(x)
  myfile = open(csvfile, 'wb')
  wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
  wr.writerow(["CPU user","CPU nice","CPU system","CPU idle","CPU iowait", "CPU irq", "CPU softirq","CPU steal", "CPU guest", "CPU guest nice","CPU percent","VMem total","VMem available","VMem percent","VMem used","VMem free", "VMem active", "Vmem inactive","VMem buffers", "VMem cached","Swap total", "Swap used", "Swap free","Swap percent","Swap sin","Swap sout","Disk usage total", "Disk usage used","Disk usage free","Disk usage percent","IO read count","IO write count","IO read bytes","IO write bytes","IO read time","IO write time","IO read merged count", "IO write merged count" ,"IO busy time", "UtilLevel"])
  global count
  wr.writerows(elements)  
  size = len(elements)
  end = time.time()
  elapsed = end - start
  total_time.append(elapsed)
  print elements[-1]
  if size == count:
    #print "Elapsed time:", elapsed
    count = count + copy_delay
    print "Count: ", count
    start = time.time()
    # connect to VM and upload scv file
    os.system("scp -i key.pem " + csvfile + " ubuntu@147.27.50.177:/var/www")
    end = time.time()
    elapsed = end - start
    #print "Elapsed time:", elapsed
printit()