"""
Script Name: verifyInternetConnectivity.py
Author: Joshua Khokhar
Creation Date: 7/7/2023
Purpose: This script verifies the computer's internet connectivity.
"""

import requests
import socket

testUrl = "https://www.youtube.com"
timedOutWait = 5
hostname = socket.gethostname()


for i in range(5):
    try:
        request = requests.get(testUrl, timeout=timedOutWait)
        print(f"{hostname} is connected to the Internet.")
    except:
        print(f"{hostname} is not connected to the Internet.")

