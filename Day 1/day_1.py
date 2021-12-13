def main():
    with open ('input.txt', 'r') as f:
        data_input = f.read().splitlines()

    increase = 0

    for i in range(len(data_input)):
        if int(data_input[i]) > int(data_input[i - 1]):
            print (f'{data_input[i]} Increase over {data_input[i - 1]}')
            increase += 1

    print(increase)

if __name__ == '__main__':
    main()
