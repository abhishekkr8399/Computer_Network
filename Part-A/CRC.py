def getCRC(message):
    reg=[0]*17
    for bit in message:
        reg.pop(0)
        reg.append(int(bit))
        if reg[0]:
            reg[0]^=1
            reg[4]^=1
            reg[11]^=1
            reg[16]^=1
    return ''.join([str(x) for x in reg[1:]])
print("--sender--")
msg=input("Enter the  binary message: ")
crc=getCRC(msg+'0'*16)
msg+=crc
print("CRC:",crc,"\nMessage with crc: ",msg)
print("--recriver--")
msg=input("Enter the received binary  message: ")
crc=getCRC(msg)
print("CRC:",crc)
print("Error in transmission."if int(crc,base=2) else "No error in transmission")