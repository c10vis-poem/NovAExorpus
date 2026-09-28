# Genymobile scrcrcpy

Skip to content 
Genymobile 
scrcpy 
Repository navigation 
Code 
Issues 
2.8k 
 (2.8k) 
Pull requests 
82 
 (82) 
scrcpy/doc 
/connection.md 
karasuhebirom1v 
karasuhebi 
and 
rom1v 
2 years ago 
132 lines (97 loc) · 3.35 KB 
 
Preview 
 
Code 
 
Blame 
Connection 
Selection 
If exactly one device is connected (i.e. listed by adb devices), then it is automatically selected. 
 
However, if there are multiple devices connected, you must specify the one to use in one of 4 
ways: 
 
by its serial: 
scrcpy --serial=0123456789abcdef 
scrcpy -s 0123456789abcdef   # short version 
 
# the serial is the ip:port if connected over TCP/IP (same behavior as adb) 
scrcpy --serial=192.168.1.1:5555 
the one connected over USB (if there is exactly one): 
scrcpy --select-usb 
scrcpy -d   # short version 
the one connected over TCP/IP (if there is exactly one): 
scrcpy --select-tcpip 
scrcpy -e   # short version 


a device already listening on TCP/IP (see below): 
scrcpy --tcpip=192.168.1.1:5555 
scrcpy --tcpip=192.168.1.1        # default port is 5555 
The serial may also be provided via the environment variable ANDROID_SERIAL (also used by 
adb): 
 
# in bash 
export ANDROID_SERIAL=0123456789abcdef 
scrcpy 
:: in cmd 
set ANDROID_SERIAL=0123456789abcdef 
scrcpy 
# in PowerShell 
$env:ANDROID_SERIAL = '0123456789abcdef' 
scrcpy 
TCP/IP (wireless) 
Scrcpy uses adb to communicate with the device, and adb can connect to a device over TCP/IP. 
The device must be connected on the same network as the computer. 
 
Automatic 
An option --tcpip allows to configure the connection automatically. There are two variants. 
 
If adb TCP/IP mode is disabled on the device (or if you don't know the IP address), connect the 
device over USB, then run: 
 
scrcpy --tcpip   # without arguments 
It will automatically find the device IP address and adb port, enable TCP/IP mode if necessary, 
then connect to the device before starting. 
 
If the device (accessible at 192.168.1.1 in this example) already listens on a port (typically 5555) 
for incoming adb connections, then run: 
 
scrcpy --tcpip=192.168.1.1       # default port is 5555 
scrcpy --tcpip=192.168.1.1:5555 
Prefix the address with a '+' to force a reconnection: 
 
scrcpy --tcpip=+192.168.1.1 
Manual 
Alternatively, it is possible to enable the TCP/IP connection manually using adb: 
 
Plug the device into a USB port on your computer. 
 
Connect the device to the same Wi-Fi network as your computer. 
 


Get your device IP address, in Settings → About phone → Status, or by executing this 
command: 
 
adb shell ip route | awk '{print $9}' 
Enable adb over TCP/IP on your device: adb tcpip 5555. 
 
Unplug your device. 
 
Connect to your device: adb connect DEVICE_IP:5555 (replace DEVICE_IP with the device IP 
address you found). 
 
Run scrcpy as usual. 
 
Run adb disconnect once you're done. 
 
Since Android 11, a wireless debugging option allows you to bypass having to physically 
connect your device to your computer. 
 
Autostart 
A small tool (by the scrcpy author) allows you to run arbitrary commands whenever a new 
Android device is connected: AutoAdb. It can be used to start scrcpy: 
 
autoadb scrcpy -s '{}' 
  
