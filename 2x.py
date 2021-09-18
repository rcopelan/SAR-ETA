from datetime import datetime
import time

time1 = datetime.now()
time.sleep(10)
time2 = datetime.now()
diff = time2 - time1
print (diff.total_seconds())


