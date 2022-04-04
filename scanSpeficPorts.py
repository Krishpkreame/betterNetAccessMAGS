import os
import time

x = int(input("Starting port"))
y = int(input("End port"))
try:
    for i in range(x, y+1):
        print("Trying port "+str(i))
        os.system("wget -T 4 -t 1 5 -qO- 35.180.139.74:"+str(i))
except:
    print("stopped")

"""
cd codingShit/Python
clear
python3 portscaner


"""
