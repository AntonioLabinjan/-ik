import base64
'''
# string u base 64 i obratno
import base64

def stringToBase64(s):
    return base64.b64encode(s.encode('utf-8'))
def base64ToString(b):
    return base64.b64decode(b).decode('utf-8')
encoded_string = stringToBase64('Hello World')
print(encoded_string)  
decoded_string = base64ToString('SGVsbG8sIFdvcmxkIQ==')
print(decoded_string)
'''
'''
# Python program za konverziju iz stringa u UTF-8

#Funkcija za konverziju iz stringa u UTF-8
def konverzija(s):
    return s.encode('utf-8')

#Unos stringa
string = "Antonio Labinjan"
h = konverzija("AntonioLabinjančć")
print(h)

string2 = "MateoUdovičić"
k = string2.encode('utf-8', 'ignore')
print(k)
'''
'''
#ASCII to String
# Input list
lst = [109, 101, 100, 105, 117, 109, 46, 99, 111, 109]

# Using chr() Method
res = ""
for i in lst:
    res = res + chr(i)

print (str(res))

value1 = 78
value2 = 97
print(chr(value1))
print(chr(value2))
'''
'''
# string to ASCII
s = "hahaha"
bla = ''.join(str(ord(c)) for c in s)

print(bla)
'''
# Bytes to string
# Program for converting bytes
# to string using decode()
'''
data = b'VasaMajka'

# display input
print('\nInput:')
print(data)
print(type(data))

# converting
output = data.decode()

# display output
print('\nOutput:')
print(output)
print(type(output))
'''

# UTF to base64

b = base64.b64encode(bytes('your_string', 'utf-8')) # bytes
base64_str = b.decode('utf-8')
print(base64_str)
