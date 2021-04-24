import os
import json
import psutil
import speedtest
st = speedtest.Speedtest()
from time import sleep


#CPU
'''
print(psutil.cpu_percent())
# gives an object with many fields
print(psutil.virtual_memory())
# you can convert that object to a dictionary 
print(dict(psutil.virtual_memory()._asdict()))
# you can have the percentage of used RAM
print(psutil.virtual_memory().percent)
# you can calculate percentage of available memory
print(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)

'''

#NETWORK
'''

print("STARTING")
while True:
    print("UP  :", st.upload())
    print("DOWN:", st.download())
    servernames =[]  
  
    st.get_servers(servernames)  
  
    print("PING:",st.results.ping) 
    # sleep(1)

'''