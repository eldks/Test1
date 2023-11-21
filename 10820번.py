def count(string) :
    answer = [0] * 4
    for i in string:
            if i.islower():
                answer[0] += 1
            elif i.isupper():
                answer[1] += 1
            elif i.isdigit():
                answer[2] += 1
            elif i == ' ':
                answer[3] += 1
    print(answer)

while True:
    try:
        string = input()
        count(string)
        
    except EOFError:
        break

