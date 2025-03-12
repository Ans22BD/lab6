#1
import os
path=os.getcwd()
os.chdir('D:\Code2\Lab5')
l=os.listdir()
for i in l:
    if os.path.isfile(i): # isdir for directories
        print(i)

        
#2
path='D:\Code2\Lab5'
l=os.listdir()

def f(path):
    if not os.path.exists(path):
        print(f"{path} does not exist")
        return
    
    if os.access(path, os.R_OK):
        print(f"{path} is readable")
    else:
        print(f"{path} is not readable")

    if os.access(path, os.W_OK):
        print(f"{path} is writable")
    else:
        print(f"{path} is not writable")
    
    if os.access(path, os.X_OK):
        print(f"{path} is executable")
    else:
        print(f"{path} is not executable")

f(path)


#3
path='D:\Code2\Lab5'

def f(path):
    if os.path.exists(path):
        print(f"{path} exists")

        d = os.path.dirname(path)
        print(f"{d} is a directory portion")

        f_n = os.path.basename(path)
        print(f"{f_n} is a filename")
    else:
        print("The file does not exist")

f(path)

#4

with open(r'D:\Code2\Lab6\ex2.txt', 'r') as f:
    l = f.readlines()

    l = [line.strip() for line in l if line.strip()]
    print(len(l))  


    
    #5

    l=["red","blue","green","black"]
with open('D:\Code2\Lab6\ex.txt','w') as f:
    for i in l:
        f.write(str(i)+"\n")

        #6

        for i in range(26):
     name =chr(65+i)+'.txt'
    
    with open(name,'w') as f:
        f.write(f"This is a file named {name}")


#7

with open ('D:\Code2\Lab6\ex.txt','r') as f:
    l=f.readlines()
with open('D:\Code2\Lab6\ex2.txt','a') as f:
    for i in l:
        f.write(i)


#8


def delete_file(file_path):
    if os.path.exists(file_path):
        if os.path.isfile(file_path):
            if os.access(file_path, os.W_OK):
                os.remove(file_path)
                print(f"Файл '{file_path}' успешно удален.")
            else:
                print(f"У вас нет прав на удаление файла '{file_path}'.")
        else:
            print(f"Путь '{file_path}' не является файлом.")
    else:
        print(f"Файл по пути '{file_path}' не существует.")

file_path = r'D:\Code2\Lab6\example'
delete_file(file_path)