# Enter your code here. Read input from STDIN. Print output to STDOUT
X = input()
shoe_size = list(input().split(" "))
N = input()
purchase_list = []
for i in range(int(N)):
    user_input = tuple(input().split(" "))
    purchase_list.append(user_input)

sum = 0

for shoe, price in purchase_list:
    if shoe in shoe_size:
        sum += int(price)
        shoe_size.remove(shoe)
    else:
        pass
    
print(sum)