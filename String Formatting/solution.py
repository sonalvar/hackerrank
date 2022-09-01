def print_formatted(number):
    # your code goes here
    l1 = len(bin(number)[2:])
    for i in range(1, number+1):
        octf = oct(i).split('o')
        hexf = hex(i).split('x')
        binf = bin(i).split('b')
        print(str(i).rjust(l1, ' '), str(octf[1]).rjust(l1, ' '), str(hexf[1].upper()).rjust(l1, ' '), str(binf[1]).rjust(l1, ' '))
        # print(str(i).rjust(l1,' '),end=" ")
        # print(oct(i).split('o')[1].rjust(l1,' '),end=" ")
        # print(((hex(i).split('x')[1]).upper()).rjust(l1,' '),end=" ")
        # print(bin(i).split('b')[1].rjust(l1,' '),end=" ")
        # print("")
        