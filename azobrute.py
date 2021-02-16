import itertools
from datetime import datetime
import argparse
import sys
import os

known_keys = [b'\x0d\x0a\xc8', b'\x03\x55\xae', b'\x0a\xc8\x0d']
known_guids = ["DV8CF101-053A-4498-98VA-EAB3719A088W-VF9A8B7AD-0FA0-4899-B4RD-D8006738DQCD",
            "EDSER93-1EDA-4W4C-BEED-WNFYRIFHBF4C04CFEW99-FES9-4558-9FEF-HFDIUFG6D851",
            "353E77DF-928B-4941-A631-512662F0785A3061-4E40-BBC2-3A27F641D32B-54FF-44D7-85F3-D950F519F12F353E77DF-928B-4941-A631-512662F0785A3061-4E40-BBC2-3A27F641D32B-54FF-44D7-85F3-D950F519F12F",
            "353E77DF-928B-4941-A631-512662F0785A3061-4E40-BBC2-3A27F641D32B-54FF-44D7-85F3-D950F519F12F",
            "2C5A87CB-758C-7293-47BC-475C65D699A584C5-7DC6-DC45-12A47C7DB587-F89F-78CD-96CA-FD478543C7F42C5A87CB-758C-7293-47BC-475C65D699A584C5-7DC6-DC45-12A47C7DB587-F89F-78CD-96CA-FD478543C7F4"]

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

        # Before we start, we try a collection of known keys so we don't have to brute-force it
        for known_key in known_keys:
            output = xor(input, known_key)
            o = output.decode('utf-8', errors='ignore')

            if "<info" in o or "Computer" in o or "PasswordsList" in o or "<c>" in o:
                guid = ""
                for g in known_guids:
                    if g in o:
                        guid = g
                '''
                position_start = o.find("<info")
                stripped = o[position_start:]
                position_end = stripped.find(">")
                '''
                # print("[ " + str(datetime.now()) + " ] Found GUID: " + stripped[+5:position_end])
                print("[ " + str(datetime.now()) + " ] Found GUID: " + guid)
                print("[ " + str(datetime.now()) + " ] Found possible key: " + str(known_key.hex()))
                exit()
        print("[ " + str(datetime.now()) + " ] Key is not known, now trying brute-force...")

        counter = 0
        for x in itertools.product([0, 1], repeat=24):
            integer = ''
            for val in x:
                integer += str(val)

            key = int(integer, 2).to_bytes(3, 'big')

#            print(f'\r' + str(counter) + " / " + str(256*256*256), end='', flush=True)

            output = xor(input, key)
            o = output.decode('utf-8', errors='ignore')
            if "<info" in o or "Computer" in o or "PasswordsList" in o or "<c>" in o:
                guid = ""
                for g in known_guids:
                    if g in o:
                        guid = g
                print("Found correct key: " + str(key))
                '''
                position_start = o.find("<info")
                stripped = o[position_start:]
                position_end = stripped.find(">")
                '''
                # print("[ " + str(datetime.now()) + " ] Found GUID: " + stripped[+5:position_end])
                print("[ " + str(datetime.now()) + " ] Found GUID: " + guid)
                print("[ " + str(datetime.now()) + " ] Found possible key: " + str(key.hex()))
                exit()
            counter = counter +1
    else:
        print("[!] Couldn't find input file; Aborting.")













