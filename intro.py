import binascii
import math

YourFirst = "lesson"
t = int.from_bytes(YourFirst.encode(), byteorder='little')


for i in range(0,29):
        m = t % 23
        t*=m if m>2 else 2

for i in range(0,1024):
        m = i % 27
        t-= pow(m,m) if m>0 else m*m

for i in range(0,32062):
        m = i % 23
        t-= pow(m,25) if m>0 else m*m

for i in range(0,43052):
        m = i % 19
        t+= pow(m,24) if m>0 else m*m

for i in range(0,36582):
        m = i % 13
        t+= pow(m,24) if m>0 else m*m

for i in range(0,813):
        m = i % 11
        t-= pow(m,24) if m>0 else m*m

for i in range(0,554772):
        m = i % 7
        t-= pow(m,24) if m>0 else m*m

for i in range(0,789):
        m = i % 5
        t+= pow(m,24) if m>0 else m*m

for i in range(0,3753):
        m = i % 4
        t+= pow(m,24) if m>0 else m*m

for i in range(0,5711):
        m = i % 3
        t-= pow(m,24) if m>0 else m*m

for i in range(0,101234):
        t-= 128

t += 328

p = 3562927236051182334153575355087347127407987755959461320351305838619130268209476696833779953363710389416751

print(f'To access the course:\n "https://" + DECODE({hex(p)[2:]}) + "/{hex(t)[2:]}"')
