import time
n = int(input('Enter the number of packets:'))
packets = []
for i in range(1, n+1): #read packet size and its arrival time
 pkt_size = int(input("Enter packet size and arrival time of packet "+ str(i) + ": "))
 arrival_time = int(input())
 packets.append((pkt_size, arrival_time))
bucket_capacity = int(input("Enter bucket capacity: "))
output_rate = int(input("Enter the output rate: "))
bucket_current_size = 0
t = 0 #time
dt = 2 #transmission time interval: transmit at every dt seconds
while len(packets) > 0 or bucket_current_size > 0:
 print('\nTime:', t)
 packets_at_t = [p for p in packets if p[1] == t] # Packets with arrival time t
 packets = [p for p in packets if p not in packets_at_t] # retain packets with arrival time > t
 for p in packets_at_t: # Check for packet and bucket status and Queue it
    if p[0] > bucket_capacity: # if packet size is > bucket capacity
        print(f'Packet of size {p[0]} arrived. [Discarded]. Packet size exceedes bucket capacity.')
    elif (p[0] + bucket_current_size) > bucket_capacity: # if adding the packet to bucket will overflow bucket
        print(f'Packet of size {p[0]} arrived. [Discarded]. Bucket overflow.')
    else: # queue the packet
        print(f'Packet of size {p[0]} arrived.[Queued]')
        bucket_current_size += p[0]
 if t % dt == 0: # @ time interval dt, drain the packets.
    if bucket_current_size >= output_rate:
        print(output_rate, 'bytes transmited.')
        bucket_current_size -= output_rate
 else:
    print(bucket_current_size, 'bytes transmited.')
    bucket_current_size = 0
 print('Free space in the bucket:', bucket_capacity-bucket_current_size)
 t += 1
 time.sleep(1)