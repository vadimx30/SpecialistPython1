s = "hello, I'm Python and I am ready to \\ten\ speak to you"
print(s)
print(s.find('Python'))

s_new = s.replace('you', 'YOU')
print(s_new)

##  можно задать количество замен
s_change = s.replace('I', 'i', 1)
print(s_change)

pattern = r'\ten'  ## raw string
print(pattern)

s_new = s.replace(pattern, 'TEN')
print(s_new)

# ## raw string отключают механизм управляющих символов
# ##'\n', '\r', '\t', '\b', '\a', '\0'
s = r"hello, I'm Python and I am ready to \\ten\ speak to you"
s_new = s.replace(pattern, 'TEN')
print(s_new)

s_example = r'123-345 test'
print(s_example.find(r'\d\d'))  ## Error

