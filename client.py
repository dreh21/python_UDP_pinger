import sys, time
from socket import *

# Initialization Section
#    Set host, port and timeout
host = '127.0.0.1'
port = 12000
timeout = 1 # in second
#    YOU FILL IN: Create UDP client socket, set its timeout, and initialize a variable for the PING sequence number
clientSocket=socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

number=0
# Ping for 10 times using a while loop
while number<10:
    #increment the sequence number
    number=number+1
    # YOU FILL IN: Format a string message to be sent per the instructions above (hint: time.asctime() is nice)
    message = 'PING '+str(number)+' '+ time.asctime()
    # Put the rest in a try/except block to handle any possible timeouts


    try:
        # YOU FILL IN: Set a variable for the time sent (hint: time.time() is nice)
        time_sent=time.time()
        encoded_message = message.encode()
        # YOU FILL IN:Send the UDP packet with the ping message
        clientSocket.sendto(encoded_message, (host, port))
        # YOU FILL IN: Receive the server response and address; user recvfrom(1024).   Read the documentation!
        #              Pay attention to the format of the returned parameters.
        response, address=clientSocket.recvfrom(1024)
        decoded_message = response.decode()
        # YOU FILL IN: Set a variable for the time received
        time_recieved=time.time()
        print('Reply from '+address[0]+": "+decoded_message)
        print('RTT: ', time_recieved-time_sent)

    except:
        # Server does not respond.  Assume the packet is lost
        # Assume the packet is lost
        print ("Request timed out.")
        continue

# Close the client socket
clientSocket.close()
