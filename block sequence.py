import numpy as np
import math
def solve(n):
    number = np.roots([1,1,-2*n])[1]
    packet = math.ceil(number)
    packetstring = ""
    helpstring = ""
    for i in range(1,packet + 1):
        helpstring += str(i)
        packetstring += helpstring
    print(number, packet)
    number = (number - (packet - 1)) * packet
    print(number)
    number = int(round(number))
    print(number)
    packetstring[number-1]
    return number


print(solve(9))
