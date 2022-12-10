from cryptography.fernet import Fernet
def load_key():
    
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key



key = load_key() 
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, paswrd = data.split("|")
            print("User:", user, "Password:", fer.decrypt(paswd.ecnode()).decode())
def add():
    acc_id = input("Account id: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(acc_id+ "|"+ fer.encrypt(pwd.ecnode()).decode()+ "\n")
        
    
while True:
    p2 = input("Would you like to add a new or view existing passwords?(Choose: view/add/'q' to quit): ").lower()
    
    if p2 == 'q':
        break
    if p2 == "view":
        view()
    if p2 == "add":
        add()

    
