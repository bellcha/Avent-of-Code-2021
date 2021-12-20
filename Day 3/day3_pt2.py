#test input works but not problem input

def most_freq(List):
    return max(set(List), key=List.count)

def least_freq(List):
    return min(set(List), key=List.count)

def oxygen_rating(input):

    with open (input, 'r') as f:
        lines = f.read().splitlines()

    for x in range(len(lines[0])):

        test_line = [line[x] for line in lines]

        top = most_freq(test_line)

        for line in lines[:]:

            if line[x] != top:
                lines.remove(line)

    return (int(''.join(lines), 2))

def co_rating(input):

    with open (input, 'r') as f:
        lines = f.read().splitlines()

    for x in range(len(lines[0])):

        test_line = [line[x] for line in lines]

        top = least_freq(test_line)

        for line in lines[:]:
            if line[x] != top:
                lines.remove(line)
    
    return int(''.join(lines), 2)



def life_support(input):

    x = oxygen_rating(input)

    y = co_rating(input)
    
    print(x, y)

            

def main():

    life_support('input.txt')

if __name__ == '__main__':
    main()