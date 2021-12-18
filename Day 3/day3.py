
#it's not pretty but it works

def most_freq(List):
    return max(set(List), key=List.count)

def least_freq(List):
    return min(set(List), key=List.count)

def diagnostic(input):
    with open (input, 'r') as f:
        lines = f.read().splitlines()
    
    final_most = []

    final_least = []

    for x in range(len(lines[0])):

        test_line = []

        for line in lines:

            test_line.append(line[x])            
            
        final_most.append(most_freq(test_line))
        final_least.append(least_freq(test_line))
    
    g = int(''.join(final_most), 2)
    e = int(''.join(final_least), 2)

    return g * e


def main():

    print(diagnostic('input.txt'))


if __name__ == '__main__':
    main()