def linecheck(list1, x):
    for x in list1:
        getlength = len(list1)
        lenornah = False
        capitalornah = any(x.isupper() for x in list1) #loops through list1 until it finds an upper; returns boolean
        numornah = any(x.isnumeric() for x in list1)

        if getlength >= 8 and getlength <= 24: lenornah = True

        if lenornah and capitalornah and numornah: return True
            
        else: return False
            
#hard coded file name just to let you know
with open('passwordCheck.csv', 'r') as F:
    lines=F.readlines() #IS A LIST
    for line in lines:
        line = line.strip() #takes out \n's IS A STRING
        email,password = line.split(",") #makes back into a list
        if linecheck(password, line):
            print("success!!")
        else:
            print(email)

