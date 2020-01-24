n = int(input())

st = 0
temp_n = n
while(temp_n != 1):
	temp_n /= 2
	st += 1
count_game = 0
for i in range(st):
	count_game = count_game + 2 ** i
#print(count_game)
lst, com_number, new_lst, total_com = [], [], [], []

com_number = [i + 1 for i in range(n)]

for item in range(count_game):
 	lst.append(int(input()))
pos = 0
#print(lst)
#print(com_number)
total_com = com_number.copy()
while (n != 1):
	n = int(n / 2)
	for i in range(n):
		if lst[pos + i] == 1:
			new_lst.append(total_com[2 * i])
		else:
			new_lst.append(total_com[2 * i + 1])
	total_com = new_lst.copy()
	print(total_com)
	new_lst.clear()
	pos += n
print('Command number - ', total_com[0])

