import string
def print_rangoli(size):
    # your code goes here
    width = size*4-3
    design = string.ascii_lowercase
    L =[]
    
    for i in range(size):
        s = "-".join(design[i:n])
        L.append((s[::-1]+s[1:]).center(width, "-"))        
    print('\n'.join(L[:0:-1]+L))