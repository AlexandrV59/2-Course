while True:
    first_num = input()
    second_num = input()
    if first_num.isdigit() and second_num.isdigit():
        print(int(first_num) + int(second_num))
        break
