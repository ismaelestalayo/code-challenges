from scapy.all import rdpcap

# dump = rdpcap('dump')
f = open('load.txt', 'w')

for i in range(len(dump)):
    try:
        f.write(dump[i].load.hex() + '\n')
    except:
        pass
    
f.close()