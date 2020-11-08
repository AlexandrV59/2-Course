string = str(input())#'AAAlsdjkflsdjf' #input and output
count1 = 0 #count_lower
count2 = 0 #count_upper
i = 0
for i in range(len(string)):
    if string[i].islower():
        count1 += 1 #lower()
    else:
        count2 += 1 #upper()
if count1 == count2:
    print(string.lower())
elif count1 > count2:
    print(string.lower())
else:
    print(string.upper()) 
