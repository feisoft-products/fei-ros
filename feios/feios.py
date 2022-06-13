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
while True:
    s = input(">>>")
    stdapi.load_cmd(s)