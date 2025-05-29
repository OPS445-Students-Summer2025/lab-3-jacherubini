#!/usr/bin/env python3
'''Lab 3 Part 4 - free_space function'''
# Author ID: jacherubini

import subprocess

def free_space():
    # Run the shell command and capture the output
    result = subprocess.run("df -h | grep '/$' | awk '{print $4}'", 
                            shell=True, capture_output=True, text=True)
    return result.stdout.strip()

if __name__ == '__main__':
    print(free_space())
