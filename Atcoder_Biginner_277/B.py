n = int(input())
d = {}
for i in range(n):
    s = input()
    if s not in d:
        d[s] = 1
    else:
        print('No')
        exit()

    if s[0] == 'S' or s[0] == 'C' or s[0] == 'D' or s[0] == 'H':
        if s[1] == 'A' or s[1] == 'T' or s[1] == 'J' or s[1] == 'Q' or s[1] == 'K' or s[1] == '2' or s[1] == '3' or s[1] == '4' or s[1] == '5' or s[1] == '6' or s[1] == '7' or s[1] == '8' or s[1] == '9':
            continue
        else:
            print('No')
            exit()
    else:
        print('No')
        exit()
print('Yes')
