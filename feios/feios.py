import sys,os,time
import feios_utils.stdapi as stdapi

################################

stdapi.clear()
print("Welcome to FEI-ROS.")
print(f"Working on {os.name.upper()}")
print("Wait for key services to setup...")
time.sleep(2.5)
print("Starting detect services...")
time.sleep(2.5)
print("We have to ensure that is you.")
if stdapi._login():
    print("We shall continue...")
    time.sleep(1)
else:
    print("Uh,that password is wrong.Try again.")
    exit()
while True:
    s = input(">>>")
    stdapi.load_cmd(s)