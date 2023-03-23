number = 0
n2 = 0
with open("usernames.txt") as the:
    for line in the:
        if line =="cultiris":
            break
        number+=1
with open("passwords.txt") as the:
    for line in the:
        if n2 == number:
            print(line)
            break
        n2+=1
