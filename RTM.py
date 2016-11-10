import psutil
import time
import threading
import csv
import os
import numpy as np
import datetime
elements = []
total_time = []

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
  #print cpu_percent , util_level
  # set the x string with parameters from psutil
  u = util_level
  #ts =datetime.now()

  x = psutil.cpu_times() + (psutil.cpu_percent(interval=1),) + psutil.virtual_memory() + psutil.swap_memory() + psutil.disk_usage('/') + psutil.disk_io_counters() + (u,)
  #print "psutil.cpu_times(): ", psutil.cpu_times()
  #print "psutil.cpu_percent(interval=1): ", psutil.cpu_percent(interval=1)
  #print "psutil.virtual_memory(): ", psutil.virtual_memory()
  #print "psutil.swap_memory(): ", psutil.swap_memory()
  #print "psutil.disk_usage('/'): ",psutil.disk_usage('/')
  #print "psutil.disk_io_counters(): ", psutil.disk_io_counters()
  #print "------------"
  #print "------------"
  #print psutil.disk_usage('/')
  #print psutil.disk_io_counters()
  elements.append(x)
  myfile = open("cassandra-workloada.csv", 'wb')
  wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
  wr.writerow(["CPU user","CPU nice","CPU system","CPU idle","CPU iowait", "CPU irq", "CPU softirq","CPU steal", "CPU guest", "CPU guest nice","CPU percent","VMem total","VMem available","VMem percent","VMem used","VMem free", "VMem acti$
  wr.writerows(elements)
  global count
  #print len(elements)
  #print elements[-1]
  #print len(elements)
  size = len(elements)
  end = time.time()
  elapsed = end - start
  total_time.append(elapsed)
  #print sum(total_time)
  #print datetime.now()
  if size == count:
    #print "Elapsed time:", elapsed
    count = count + copy_delay
    print "Count: ", count
    start = time.time()
    # connect to VM and upload scv file
    #os.system("scp -i key.pem cassandra-test2.csv ubuntu@147.27.50.177:/var/www")
    end = time.time()
    elapsed = end - start
    #print "Elapsed time:", elapsed
printit()