
data = 'sg'
datalist = []
for i in data:
    datalist.append(i)

print(datalist)

length = len(datalist)
start = 0
end = length
add = 0
while end - start >= 1:
	end -= 1 
	print(i, start, end, datalist[start], datalist[end])
	if datalist[start] == datalist[end]:
		start += 1
	else:
		add += 1
		if start != 0:
			start = 0
			end += 1
	
print(length, add)
result = length + add        

print(result)