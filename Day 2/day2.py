def main(commands):
    horizontal = 0
    depth = 0
    for i in commands:
        if i[0] == 'forward':
            horizontal += int(i[1])
        elif i[0] == 'down':
            depth += int(i[1])
        elif i[0] == 'up':
            depth -= int(i[1])
    return (horizontal * depth)


if __name__ == "__main__":
    with open ('input.txt', 'r') as f:
        lines = f.read().splitlines()
        commands = list(i.split(' ') for i in lines)

    print(main(commands))
