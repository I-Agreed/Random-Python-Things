def rbg2hex(red,green,blue):
    r2 = str(format(red, '02x'))
    g2 = str(format(green, '02x'))
    b2 = str(format(blue, '02x'))
    return("#" + r2 + b2 + g2)

def hex2rbg(hex):
    a = 0
    r = str()
    b = str()
    g = str()
    for i in hex:
        a += 1
        if a == 2 or a == 3:
            r = r + i
        if a == 4 or a == 5:
            b = b + i
        if a == 6 or a == 7:
            g = g + i
    r = "0x" + r
    r2 = int(r,16)
    b = "0x" + b
    b2 = int(b,16)
    g = "0x" + g
    g2 = int(g,16)
    return(r2,b2,g2)
