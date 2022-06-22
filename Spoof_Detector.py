import os
from datetime import datetime
import time

def arp_extract():
    arpTab = os.popen("arp -a").read()
    arpTab_lines = arpTab.splitlines()
    addr = {}
    for line in arpTab_lines:
        if "ff-ff-ff-ff-ff-ff" in line:
            break
        if arpTab_lines.index(line) > 2:
            ip, mac, _type = line.split()
            addr[ip] = mac

    duplication(addr)


def duplication(addr):
    temp_macList = []
    print("Scanning...")
    time.sleep(3)
    for mac in addr.values():
        if mac in temp_macList:
            print("Finished Scanning.")
            log("Arp Spoofed!\nThe address is :" + mac)
            break
        temp_macList.append(mac)


def log(message):
    print("Generating Log.")
    time.sleep(3)
    date = datetime.now()
    with open("log.txt", "a") as log:
        log.write(message + "\nDate: {}\n\n".format(date))
    print("The event is logged in log.txt")


if __name__ == "__main__":
    arp_extract()

input("\nPress 'Enter to exit the program")


