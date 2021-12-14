def main():
    with open ('input.txt', 'r') as f:
        lines = f.read().splitlines()
        data_input = [int(l) for l in lines]

    increase_list = []
    increase = 0

    for i in range(len(data_input)):
        x = data_input[i:i+3]
        if len(x) == 3:
            increase_list.append((sum(x)))
    
    for i in range(len(increase_list)):
        if int(increase_list[i]) > int(increase_list[i - 1]):
            print (f'{increase_list[i]} Increase over {increase_list[i - 1]}')
            increase += 1
        
    print(increase)

if __name__ == '__main__':
    main()