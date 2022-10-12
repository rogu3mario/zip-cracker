import zipfile
def password_crack (passwords_file,obj):
    idx = 0
    with open ( password_file, 'rb') as file:
        for line in file:
            for word in line.split():
                try:
                    idx += 1
                    obj.extractall(pwd=word)
                    print(" PASSWORD FOUND AT LINE NUMBER: ", idx)
                    print("PASSWORD IS: ", word.decode())
                    return True
                except:
                    continue
    return False
password_file = "passwords.txt"
zip_file = "secret.zip"
obj = zipfile.ZipFile(zip_file)
cnt = len(list(open(password_file, "rb")))
print(" THERE ARE",CNT,"PASSWORDS IN THE FILE")
if password_crack (password_file, obj) == False:
    print("PASSWORD NOT FOUND")
                    
