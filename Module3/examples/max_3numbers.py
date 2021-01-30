"""
Program should output three sorted numbers
"""
a = int(input('1-st number: '))
b = int(input('2-nd number: '))
c = int(input('3-d number: '))

if a > b:
    max_v = a
    middle_v = b
else:
    max_v = b
    middle_v = a

if max_v > c:
    if middle_v > c:
        min_v = c
    else:
        middle_v, min_v = c, middle_v
else:
    max_v, middle_v, min_v= c, max_v, middle_v
    
print(min_v, middle_v, max_v)
        

 