import math
print("Enter 2 large prime numbers: ")
p = int(input())
q = int(input())
n = p * q
phi = (p - 1) * (q - 1)
e_list = [e for e in range(2, phi) if math.gcd(e, phi) == 1]
print("List of e's: ", e_list)
e = int(input("Choose the encryption value 'e' from the list: "))
d = 2
while((e * d) % phi != 1):
 d += 1
print(f"Public key : ({e}, {n})")
print(f"Private key: ({d}, {n})")
plain = input("\nEnter the message to encrypt:");
cipherText = [(ord(p) ** e % n) for p in plain]
print("Cipher Text:", cipherText)
plainText = [chr(c ** d % n) for c in cipherText]
print('Plain Text:', ''.join(plainText))