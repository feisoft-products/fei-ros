import sys,os,time
import feios_utils.stdapi as stdapi
import feios_utils.msg as msg

################################

stdapi.clear()
if os.name == 'nt':
    os.system("color 5f")
    stdapi.clear()
    print(msg.STD_BOOT)
else:
    print(msg.STD_BOOT)
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
    stdapi.clear()
else:
    print("Uh,that password is wrong.Try again.")
    exit(time.sleep(2))
while True:
    s = input(">>>")
    stdapi.load_cmd(s)