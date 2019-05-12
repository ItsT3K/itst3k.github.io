import os
import time
#This program tells the Raspberry Pi's CPU Temperature in Celcius
def measure_temp()
    temp = os.popen("vcgencmd measure_temp").readline()
    return (temp.replace("temp=",""))
while True:
    print"The Current CPU Temperature is" ,measure_temp()
    time.sleep(2)
    