with open ('input.txt', 'r') as f:
    data_input = f.read().splitlines()

increase = 0

for i in range(len(data_input)):
    if data_input[i] > data_input[i - 1]:
        print (f'{data_input[i]} Increase')
        increase += 1

print(increase)