from colorama import Fore, Style, init
import os

init()

# colors
c = Fore.LIGHTCYAN_EX
y = Fore.LIGHTYELLOW_EX
re = Fore.RESET

# styles
dim = Style.DIM
res = Style.RESET_ALL

ip_address = input(y + "[+] Gateway IP address: " + re)

print(c + "[*] " + re + "Running nmap command. Please wait...")

os.system("nmap -sn " + ip_address + "/24 > nmap.txt")

print(c + "[*] " + re + "Done! Showing results:")
print("")

counter = 0

with open("nmap.txt", "r") as fr:
    for line in fr.readlines():
        if "Nmap scan" in line.strip("\n"):
            split = line.strip("\n").split(" ")

            ip = split[5].strip("(").strip(")")

            counter += 1

            if counter == 1:
                print(dim + "ID | IP Address      | Name" + res)
                print(dim + "---+-----------------+---------------------------------" + res)

            print(dim + "{:02d}".format(counter) + " | " + res + "{:<15}".format(ip) + " | " + split[4])
