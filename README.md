# Python Port Scanner

Run the script in the Linux Kernel like:

root@user#: python Port_Scanner.py -H <Host> -P <Port Start> -S <Port Stop> -T <Timeout>

How It Works: Written in Python 2.7, the Port Scanner sends SYN packets, and waits for a response. If none is received, the port is closed, if a response is received, the port is open. 
