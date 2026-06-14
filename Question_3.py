#Q 3 Password Attempt
correct_password = "python123"
attemps = 0
max_attemps = 3
while attemps < max_attemps:
    user_password = input("Please enter your password:  ")
    if user_password == correct_password:
        print("Acess granted")
        break
    else:
            attemps += 1
            print("Incorrect password, try again")
if attemps == max_attemps:
     print("Account blocked")            

