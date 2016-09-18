#!/usr/bin/env python2
# Author is Moses Arocha

import optparse
import socket
import sys
import os


# For Each Port between Start & Stop:
#       Try to Connect to Host: Port timeout if no answer
def portScan(port_start, port_stop, timeout, host):
    for port in range(port_start, port_stop + 1):
        try:
	    sock = socket.create_connection((host, port), timeout)
        except socket.error:
	    pass
#        print ("Connection Failed: Port {}".format(port))
        except socket.timeout:
	    print ("Connection Timed Out: Port {}".format(port))
    else:
	try:
	    service = socket.getservbyport(port, 'tcp')
	except:
	    service = 'unknown'
	print ("Connection Successful: Port {} ({})".format(port, service))
	sock.close()
	
	#    if successful
	#        print host: port success
	#   else if connection fail
	#        print host: port fail
	#   else if timeout
	#        print host: port timeout


def main():
    if not os.geteuid() == 0:
        sys.exit('\tMust Be Root!')
    parser = optparse.OptionParser("Usages For Program: -H <Host> -P <Port Start> -S <Port Stop> -T <Timeout>")
    parser.add_option('-H', dest='host', type='string', help='Specify Host IP Address')
    parser.add_option('-P', dest='port_start', type='int', help='Specify Port Start', default=0)
    parser.add_option('-S', dest='port_stop', type='int', help='Specify Port Stop', default=65535)
    parser.add_option('-T', dest='timeout', type='int', help='Specify Timeout Time', default=0.1)
    (options, args) = parser.parse_args()
    port_start = options.port_start
    port_stop = options.port_stop
    timeout = options.timeout
    if options.host == None:
	print parser.usage
	exit(0)
    else:
	host = options.host
    portScan(port_start, port_stop, timeout, host)


if __name__ == '__main__':
    main()
