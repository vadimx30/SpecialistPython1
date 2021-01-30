"""
Program should output three sorted numbers
"""
a = int(input('1-st number: '))
b = int(input('2-nd number: '))
c = int(input('3-d number: '))

if a < b:
    a, b = b, a
    
if a < c:
    a, b, c = c, a, b
else:
    if c > b:
        b, c = c, b
    
print(a, b, c)
        
# a b c
# b a c
