import sys,os,time
import feios_utils.funcs as utils

################################

print("Welcome to FEI-ROS.")
print(f"Working on {os.name.upper()}")
print("Wait for key services to setup...")
time.sleep(3)
print("Starting detect services...")
time.sleep(3)
while True:
    s = input(">>>")
    utils.load_cmd(s)