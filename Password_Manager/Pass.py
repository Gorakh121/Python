from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
        
write_key()

def load_key():
    file =open("key.key","rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def add():
    name = input("User name: ")
    pwd = input("Password: ")
    
    with open("Password.txt", "a") as f:
        f.write(name+ "|" + fer.encrypt(pwd.encode()).decode()+"\n")
    
def view():
    with open("Password.txt","r") as f:
        for line in f.readlines():
            data = line.rstrip() #it will remove the return line 
            Username, password = data.split("|")
            print("user:",Username,"Password:",fer.decrypt(password.encode()).decode())
            
while True:
    choice = input("Please enter what you want to do: view, add or q to exit: ").lower()
    if choice == "q":
        break
    if choice == "view":
        view()
    elif choice == "add":
        add()
    else:
        print("You have entered wrong choice")
        continue