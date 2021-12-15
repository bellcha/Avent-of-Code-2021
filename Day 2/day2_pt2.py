def main(commands):
    horizontal = 0
    depth = 0
    aim = 0
    for i in commands:
        if i[0] == 'forward':
            horizontal += int(i[1])
            depth += (aim * int(i[1]))

        elif i[0] == 'down':
            aim += int(i[1])

        elif i[0] == 'up':
            aim -= int(i[1])

    print(f'Final Value: {(horizontal * depth)}')

if __name__ == "__main__":
    with open ('input.txt', 'r') as f:
        lines = f.read().splitlines()
        commands = list(i.split(' ') for i in lines)

    main(commands)