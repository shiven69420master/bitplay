input("Build a bit mask -- one 1 at exactly that position.  Press Enter ")
for k in range(4):
    mask = 1 << k
    print("  bit", k, "  mask:", mask, "  binary:", bin(mask)[2:])


n = int(input("Enter a number (try 42 or 13): "))
input("Check if the Nth bit is set - AND with the mask.  Press Enter ")
result = (n >> 2) & 1
print("Binary form of n is", bin(n)[2:])
if result:
    print("Bit at the second position is on")
else:
    print("Bit at second position is off")    