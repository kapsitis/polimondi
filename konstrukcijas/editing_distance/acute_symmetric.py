
# Cik vietās polimonda malas neatbilst ideāla trīsdaļīga grafa
# malu virzienu simetrijai. "Ideāls" trīsdaļīgs polimonds ir "ACECEAEAC".
# Tādam polimondam neatbilstību skaits ir 0.
# This string for n=27 has 2 mismatches (visible after we split into 3 parts): ACAEAEAECECECECECACACACACAC
#  *      *
# ACAEAEAEC
# ECECECECA
# CACACACAC
def tripartite_mismatches(arg):
    mismatches = 0
    letters = {'A':['A', 'C', 'E'], 'C':['C', 'E', 'A'], 'E':['E', 'A', 'C']}
    n = len(arg)
    ch1 = arg[0]
    ch2 = arg[n//3]
    ch3 = arg[(2*n)//3]
    if {ch1, ch2, ch3} != {'A', 'C', 'E'}:
        return n
    direction = 1
    if ch2 != 'C':
        # print("Strange exception: {}".format(arg))
        direction = -1
    for i in range(0, n // 3):
        rotated1 = letters[arg[i]][direction % 3]
        rotated2 = letters[arg[i]][(2*direction) % 3]
        if arg[n//3 + i] != rotated1:
            mismatches += 1
        if arg[(2*n)//3 + i] != rotated2:
            mismatches += 1
    return mismatches

def is_balanced(arg):
    n = len(arg)
    counts = [0,0,0]
    for i in range(n):
        if arg[i] == 'A':
            counts[0] += 1
        elif arg[i] == 'C':
            counts[1] += 1
        elif arg[i] == 'E':
            counts[2] += 1
    return (counts[0] == counts[1] and counts[0] == counts[2])





def main():
    div_by_three = [9, 27, 33, 39, 45, 51]
    for n in div_by_three:
        file_name = 'acute_{}.txt'.format(n)
        with open(file_name, 'r') as fp:
            for line in fp:
                line = line.strip()
                if is_balanced(line):
                    print(line)



if __name__ == '__main__':
    main()


