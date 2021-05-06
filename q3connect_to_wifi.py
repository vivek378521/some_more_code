import subprocess as sp
import sys
import os

# the process to connect in windows
def connect(name, ssid, password):
    config = """<?xml version=\"1.0\"?>
    <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
        <name>""" + name + """</name>
        <SSIDConfig>
            <SSID>
                <name>""" + ssid + """</name>
            </SSID>
        </SSIDConfig>
        <connectionType>ESS</connectionType>
        <connectionMode>auto</connectionMode>
        <MSM>
            <security>
                <authEncryption>
                    <authentication>WPA2PSK</authentication>
                    <encryption>AES</encryption>
                    <useOneX>false</useOneX>
                </authEncryption>
                <sharedKey>
                    <keyType>passPhrase</keyType>
                    <protected>false</protected>
                    <keyMaterial>""" + password + """</keyMaterial>
                </sharedKey>
            </security>
        </MSM>
    </WLANProfile>"""
    command = "netsh wlan add profile filename=\"" + name + ".xml\"" + " interface=Wi-Fi"
    os.system(command)
    with open(name + ".xml", 'w') as file:
        file.write(config)
    command = "netsh wlan connect name=\"" + name + "\" ssid=\"" + ssid + "\" interface=Wi-Fi"
    os.system(command)
    os.remove(name + ".xml")

# checks if you are connected
def checkIfWifiConnected():
    command = "netsh interface show interface | findstr /C:\"Wi-Fi\" /C:\"Name\""
    results = sp.check_output(command, shell=True)
    results = results.decode("ascii")
    results = results.replace("\r", "")
    if "Connected" in results:
        return True
    else:
        return False


def showTop3WifiNetworks():
    results = sp.check_output(["netsh", "wlan", "show", "network"])
    results = results.decode("ascii") # needed in python 3
    results = results.replace("\r", "")
    ls = results.split("\n")
    ls = ls[4:]
    ssids = []
    x = 0
    while x < len(ls): # you might be wondering what is done here, actually to get the output and to get the ssid specifically the output had to be chunked off
        if x % 5 == 0:
            ssids.append(ls[x])
        x += 1
    networks_available = []
    for name in ssids:
        networks_available.append(name[4:])
    return networks_available[:3]


if __name__ == "__main__":
    try:
        networks = showTop3WifiNetworks()
        for i in networks:
            print(i)
        name = input("Please enter the number corresponding to the network you want to connect with: ")
        if checkIfWifiConnected():
            print("Please disconnect all wifi else it will just be an overlap")
            sys.exit()
        if name == '1':
            conn = networks[0][5:]
        elif name == '2':
            conn = networks[1][5:]
        elif name == '3':
            conn = networks[2][5:]
        else:
            print("Wrong choice! Run script again.")
            sys.exit(0)

        password = input("Enter the password: ")
        connect(conn, conn, password)
        if checkIfWifiConnected():
            print("You are connected.")
        else:
            print("Try again with right credentials")
            sys.exit(0)
    except KeyboardInterrupt as e:
        print("Exiting.")


'''nmcli dev wifi connect <ssid> password <password>
nmcli con up
nmcli dev wifi list'''