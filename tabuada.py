mult: int

x = int(input("Deseja saber a tabuada de qual valor? "))

for i in range (0, 10):
    mult = x * (i+1)
    print(f"{x} x {i+1} = {mult}")
