
f = open('load.txt', 'r')
load = f.read()
f.close()

load = load.split('\n')


"""
80 == "1000 0000"
       ^ most significant bit to 1 means the next byte is also part of the f
"""
def read_var_size(data, max_bytes):
    n = 0
    total = 0
    while n < max_bytes:
        h = data[0+(2*n):2+(2*n)] # hex data
        b = bin( int(h, 16))[2:].zfill(8)
        more_bytes = b[0] == '1'
        value = int(b[1:], 2) << (7*n)
        total += value
        
        # if the flag more_bytes is set and havent read max_bytes, do it again
        if more_bytes == True or h == '00':
            n += 1
        else:
            break
    return total, n+1


for l in load:
    length, offset = read_var_size(l[0:2*5], 5)
    if l[(2*offset):(4*offset)] != '00':
        print("FUCK")
        print(l)
    packetID, offset= read_var_size(l[(2*offset):(2*offset)+(2*5)], 5)