#!/usr/bin/env python3
import os
import time
import sys
import subprocess
from termcolor import colored #Requires: pip3 install termcolor

def getResponse(host):
    marco = os.system(f"ping -c 1 -W 1 {host} > /dev/null 2>&1")
    if marco == 0:
        return True
    else:
        return False

def pingHosts(hosts, results):
    new_results = []
    host_num = 0
    
    for host in hosts:
        if len(results) == 0:
            response = getResponse(str(host))
            new_results.append([str(host), response, "NEVER"])
        else:
            response = getResponse(str(host))
            if str(response) == str(results[host_num][1]):
                new_results.append([str(host), response, results[host_num][2]])
            else:
                new_results.append([str(host), response, getTime()])
            host_num += 1
            
    results = new_results
    return results

def getTime():
    localtime = time.localtime()
    current_time = time.strftime("%H:%M:%S", localtime)
    return current_time

hosts = sys.argv[1:]
results = []
status = []

while True:
    results = pingHosts(hosts, results)

    os.system('clear') 

    for result in results:
        if result[1]:
            print(result[0] + ": " + colored("UP", "green") + " Last Offline:" + result[2])
        else:
            print(result[0] + ": " + colored("DOWN", "red") + " Last Online:" + result[2])
    time.sleep(1)
