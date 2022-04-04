import os
import time

x = int(input("Starting port"))

os.system("clear")
print("""
###################################################################
###################################################################
###################################################################
\n\n\n
""")
try:
    while(True):
        print("Trying port"+str(x))
        os.system("wget -T 4 -t 1 5 -qO- 35.180.139.74:"+str(x))
        x += 9
except:
    print("stopped")

"""
cd codingShit/Python
clear
python3 portscaner


"""
