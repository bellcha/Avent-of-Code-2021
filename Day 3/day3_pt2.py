#This is ugly but works.

def most_freq(List):

    ones = 0
    zeros = 0
    print(List)

    for i in List:
        if i == '1':
            ones +=1
        else:
            zeros += 1
        
    if ones == zeros:
        return '1'
    elif ones > zeros:
        return '1'
    else:
        return '0'

def least_freq(List):
    ones = 0
    zeros = 0
    print(List)

    for i in List:
        if i == '1':
            ones +=1
        else:
            zeros += 1
        
    if zeros == ones:
        return '0'
    elif zeros < ones:
        return '0'
    else:
        return '1'

def oxygen_rating(input):

    with open (input, 'r') as f:
        lines = f.read().splitlines()

    for x in range(len(lines[0])):

        test_line = [line[x] for line in lines]

        top = most_freq(test_line)

        for line in lines[:]:

            if line[x] != top:
                lines.remove(line)


    return int(''.join(lines), 2), lines

def co_rating(input):

    with open (input, 'r') as f:
        lines = f.read().splitlines()

    for x in range(len(lines[0])):

        if len(lines) > 1:

            test_line = [line[x] for line in lines]

            top = least_freq(test_line)

            for line in lines[:]:
                if line[x] != top:
                    lines.remove(line)
        else:
            break
    
    return int(''.join(lines), 2), lines


def life_support(input):

    x = oxygen_rating(input)

    y = co_rating(input)
    
    print(x, y)
    print (x[0] * y[0])


if __name__ == '__main__':
    life_support('input.txt')