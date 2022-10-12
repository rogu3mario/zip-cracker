import zipfile
   #importing the zipfile module

def password_crack (passwords_file,obj):
    idx = 0
    with open ( password_file, 'rb') as file:
         #opening the file in read binary mode
            #file selected would be 'passwords.txt'
        
            
        for line in file:
            for word in line.split():
                try:
                    idx += 1
                    obj.extractall(pwd=word)
                    print(" PASSWORD FOUND AT LINE NUMBER: ", idx)
                          #location of the password is revealed, by showing the line number it is present at
                    
                    print("PASSWORD IS: ", word.decode())
                            #unicode-decode error will be prompted if the password is a non-character
                    return True
                except:
                    continue
    return False
password_file = "passwords.txt"
zip_file = "secret.zip"
  #initializing the zipfile function

obj = zipfile.ZipFile(zip_file)
cnt = len(list(open(password_file, "rb")))
print(" THERE ARE",CNT,"PASSWORDS IN THE FILE")
if password_crack (password_file, obj) == False:
    print("PASSWORD NOT FOUND")
                    #ending the program
