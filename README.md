# Python Port Scanner

Run the script in the Linux Kernel like:

root@user#: python Port_Scanner.py -H 127.0.0.1 -P 1024 -S 65535 -T .2

Help:
-H : Attacking Host
-P : Port To Start Scan
-S : Port To Stop Scan 
-T : Timeout Duration

How It Works: Written in Python 2.7, the Port Scanner sends SYN packets, and waits for a response. If none is received, the port is closed, if a response is received, the port is open. 
