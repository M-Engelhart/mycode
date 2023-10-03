#!/usr/bin/env python3

import shutil # Shell utilities to move files
import os     # Perform OS operations

def main():
    os.chdir('/home/student/mycode/')             # Change into mycode/ directory
    shutil.move('raynor.obj', 'ceph_storage/')    # Run the 'mv' command

    xname = input('What is the new name for kerrigan.obj? ')           # Get input from user
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)  # moving kerrigan.obj into ceph_storage with the new name


if __name__ == "__main__":
    main()
