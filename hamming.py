import math
def getParityBitCount(data_count):
    p=1
    while not 2**p>=data_count+p+1:
        p+=1
    return p
def getArrangedBits(message,parity_count):
    n = len(message) + parity_count
    frame=[0]*n
    for i in range(1,n+1):
        if not math.log2(i).is_integer():
            frame[-i] = message.pop()
    return frame
def getHammingCode(message):
    message=[int(x) for x in message]
    parity_count=getParityBitCount(len(message))
    hamming_code=getArrangedBits(message,parity_count)
    bit=1
    #_
    for i in range(parity_count):
        parity_sum=0
        for i in range(1,len(hamming_code)+1):
            if i & bit:
                parity_sum+=hamming_code[-i]
        hamming_code[-bit]=parity_sum%2
        bit*=2
        return''.join([str(x) for x in hamming_code])
message=input("Enter the bit pattern:")
print("Hamming Code:",getHammingCode(message))
def checkHammingCode(message):
    message=[int(x) for x in message]
    bit=1
    error=''
    parity_count=round(math.log2(len(message)))+1
    #_
    for i in range(parity_count):
        parity_sum=0
        for i in range(1,len(message)+1):
            if i & bit:
                parity_sum+=message[-i]
        error=str(parity_sum%2)+error
        bit*=2
    return int(error,base=2)
def codeCorrection(message,position):
    p = len(message)-position
    return message[:p] + str(int(not int(message[p])))+message[p+1:]
message=input('Enter received message:')
position=checkHammingCode(message)
if position==0:
    print('No error in transmission.')
else:
    print('Error found at position:',position,'from right')
    print("Corrected message:",codeCorrection(message,position))   