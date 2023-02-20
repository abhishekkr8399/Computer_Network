DATA_SIZE = 3
msg = input("Enter a message: ")
msg_chunks = [msg[i:i+DATA_SIZE] for i in range(0, len(msg), DATA_SIZE)]
frames = [{'segno':(i+1),'data':msg_chunks[i]}for i in range(len(msg_chunks))]
print("Fragmented frames: ",frames,"\n")
import random 
random.shuffle(frames)
print('Unordered frames received: ', frames,"\n")
print('Unordered message: '+ ''.join([x['data'] for x in frames]),"\n")
frames.sort(key=lambda x : x['segno'])
print('Sorted frames: ',frames,"\n")
print('Sorted message: ' + ''.join([x['data'] for x in frames]),"\n")