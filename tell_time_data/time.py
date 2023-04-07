
from datetime import datetime
import time

for i in range(100):
    time.sleep(5)
    file = open("log.txt", "a")
    time.sleep(1)
    file.write(datetime.today().strftime('%Y-%m-%d %H:%M:%S')+"\n")
file.close()