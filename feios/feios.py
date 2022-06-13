import sys,os,time
import feios_utils.stdapi as stdapi

################################

os.system("cls" if os.name == 'nt' else "clear")
print("Welcome to FEI-ROS.")
print(f"Working on {os.name.upper()}")
print("Wait for key services to setup...")
time.sleep(3)
print("Starting detect services...")
time.sleep(3)
while True:
    s = input(">>>")
    stdapi.load_cmd(s)