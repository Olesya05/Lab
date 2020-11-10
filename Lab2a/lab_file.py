import math
from math import sqrt

print("first constant", False)
print("second constant", True)
print("third constant", None)

print(oct(16), "is 16 in oct \n")

print(ord('a'), "\n")

flaq = 23
if flaq - 10 == 5:
    print("clock\n")
else:
    print("not clock\n")

for i in range(3):
    print(" Python \n")



    with open("README.md", "w") as f:
        f.write("File message")

sub = lambda a, b: a-b
print(sub(34, 5))


Arg = -9
try:
    print("Що вийде при добуванні корення з -9", sqrt(Arg))
except Exception as e:
    print(e)
finally:
    print ("Ось що вийде")