fib = [0, 1]
for i in range(2, 15):

    next_fib = fib[i-1] + fib[i-2]
    fib.append(next_fib)

print(fib)

#Через while 
fib = [0, 1]

while len(fib) < 15:
    next_num = fib[-1] + fib[-2]
    fib.append(next_num)

print(fib)