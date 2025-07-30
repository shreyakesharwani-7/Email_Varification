
email = input(" Enter your Email : ")#g@g.in, shreya@gmail.com
k = 0
j = 0 
d = 0
if len(email)>=6:
    if email[0].isalpha():
        if ("@"in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3 ]== "."):
                for i in email:
                    if i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i.isupper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i =="." or i == "@":
                        continue
                    else:
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print(" Wrong email 5 (contains space, capital letter, or invalid character) ")
                else:
                    print(" Right email ")
            else:
                print(" Wrong email 4 (dot not at correct position) ")
        else:
            print(" Wrong email 3 (missing @ or more than one @) ")
    else:
        print(" Wrong email 2 (first character is not a letter) ")
else:
    print(" Wrong email 1 (length is less than 6) ")
