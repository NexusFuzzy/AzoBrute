import itertools
from datetime import datetime
import argparse
import sys
import os


def xor(data, key):
    l = len(key)
    return bytearray((
        (data[i] ^ key[i % l]) for i in range(0,len(data))
    ))
    
    
def print_header():
    print("   _____              __________                __   ")
    print("  /  _  \ ____________\______   \_______ __ ___/  |_  ____")
    print(" /  /_\  \\___   /  _ \|    |  _/\_  __ \  |  \   __\/ __\\")
    print("/    |    \/    (  <_> )    |   \ |  | \/  |  /|  | \  ___/")
    print("\____|__  /_____ \____/|______  / |__|  |____/ |__|  \___  >")
    print("        \/      \/            \/                         \/")

if len(sys.argv) < 2:
    print_header()
    print("Usage: " + sys.argv[0] + " --input_file <Input File>")
else:
    print_header()
    parser = argparse.ArgumentParser(
        description='AzoBrute - A tool to bruteforce the encryption key and GUID for AzoRult 3.3')
    parser.add_argument("--input_file", help="File which contains the encrypted POST data to AzoRult", type=str)
    args = parser.parse_args()

    if os.path.isfile(args.input_file):
        print("[ " + str(datetime.now()) + " ] Using file '" + args.input_file + "' as input.")

        input_file = open(args.input_file, "rb")
        input = input_file.read()

        for x in itertools.product([0, 1], repeat=24):
            integer = ''
            for val in x:
                integer += str(val)

            key = int(integer, 2).to_bytes(3, 'big')
            output = xor(input, key)
            o = output.decode('utf-8', errors='ignore')
            if "<info" in o:
                position_start = o.find("<info")
                stripped = o[position_start:]
                position_end = stripped.find(">")
                print("[ " + str(datetime.now()) + " ] Found GUID: " + stripped[+5:position_end])
                print("[ " + str(datetime.now()) + " ] Found possible key: " + str(key.hex()))
                exit()

    else:
        print("[!] Couldn't find input file; Aborting.")













