
#it's not pretty but it works

def most_freq(List):
    return max(set(List), key=List.count)

def least_freq(List):
    return min(set(List), key=List.count)

def gamma():
    with open ('input.txt', 'r') as f:
        lines = f.read().splitlines()
    
    final = []

    for x in range(len(lines[0])):

        test_line = []

        for line in lines:

            test_line.append(line[x])            
            
        final.append(most_freq(test_line))
    
    return int(''.join(final), 2)

def epsilon():

    with open ('input.txt', 'r') as f:
        lines = f.read().splitlines()
    
    final = []

    for x in range(len(lines[0])):

        test_line = []

        for line in lines:

            test_line.append(line[x])            
            
        final.append(least_freq(test_line))
    
    return int(''.join(final), 2)


def main():
    
    g = gamma()

    e = epsilon()

    print(g * e)



if __name__ == '__main__':
    main()