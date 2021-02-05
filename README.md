# AzoBrute
A tool to bruteforce the encryption key and GUID for AzoRult 3.2 and 3.3 using a [Known-Plaintext Attack](https://en.wikipedia.org/wiki/Known-plaintext_attack).

This script is able to bruteforce the XOR key used for encrypting the traffic sent via POST to the AzoRult Server. Afterwards, it automatically extracts the GUID which you can the use for [AzoSPam](http://github.com/hariomenkel/AzoSpam). One way to save those requests is with Burp Suite with which you are able to save out the requests to file:

Note: This project ist still work in progress - Bruteforcing the key takes several minutes depending on your CPU

# How To

Open Burp and execute the AzoRult malware (in a secure environment - don't make your CISO upset!)

Rightclick > Copy to file

The use azobrute.py <inputfile> to decrypt the request. Please note, that a normal C2-Traffic contains of two POST-Requests. One short "Check-In" and afterwards a bigger request with the Credentials, Cookies etc.
  
![alt text](https://github.com/hariomenkel/AzoDecrypt/raw/master/screenshot.PNG)

This should give you a file like this:

![alt text](https://github.com/hariomenkel/AzoDecrypt/raw/master/screenshot2.PNG)

This file can then be used as input which should produce the decrypted output saved as file:

![alt text](https://github.com/hariomenkel/AzoBrute/raw/main/screenshot.png)
