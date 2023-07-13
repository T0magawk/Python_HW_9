# # Дополнить телефонный справочник возможностью изменения и удаления данных. 
# # Пользователь также может ввести имя или фамилию, и 
# # Вы должны реализовать функционал для изменения и удаления данных


import codeop
from pathlib import Path

FILE_PATH = Path('phone.txt')
print(FILE_PATH)


def add_contakt():
    with open(FILE_PATH, 'a', encoding='utf8') as file: 
        info=input('Введите данные: ') 
        file.write(f'\n{info}')


def show_contakt():
    with open(FILE_PATH, 'r', encoding='utf8') as file: 
        # print([lines for lines in file])
        print(*[line for line in file])
        # print(file.readlines())


def find_contakt():
    list_1=[]
    serch=input('Ведите искомое: ').strip()
    with open(FILE_PATH, 'r', encoding='utf8') as file:
        for contakt in file:
            if serch in contakt:
                list_1.append(contakt)
        print(*[line for line in list_1])      
                
def edit_contact():
    search = input('Введите имя или фамилию контакта, который хотите изменить: ').strip()
    temp_file = FILE_PATH.with_name(FILE_PATH.stem + "_temp.txt")
    
    with open(FILE_PATH, 'r', encoding='utf8') as file, open(temp_file, 'w', encoding='utf8') as temp:
        updated = False
        for contact in file:
            if search in contact:
                new_data = input('Введите новые данные для контакта: ')
                temp.write(f'{new_data}\n')
                updated = True
            else:
                temp.write(contact)
    
    if updated:
        temp_file.replace(FILE_PATH)
        print('Контакт успешно изменен')
    else:
        temp_file.unlink()
        print('Контакт не найден')

def delete_contact():
    search = input('Введите имя или фамилию контакта, который хотите удалить: ').strip()
    temp_file = FILE_PATH.with_name(FILE_PATH.stem + "_temp.txt")
    
    with open(FILE_PATH, 'r', encoding='utf8') as file, open(temp_file, 'w', encoding='utf8') as temp:
        deleted = False
        for contact in file:
            if search in contact:
                deleted = True
            else:
                temp.write(contact)
    
    if deleted:
        temp_file.replace(FILE_PATH)
        print('Контакт успешно удален')
    else:
        temp_file.unlink()
        print('Контакт не найден')

def choouse():
    flag=True
    while flag:
        n=input('Введите действие: ')
        match n:
            case '1':
                add_contakt()
                
            case '2':
                show_contakt()
                
            case '3':
                find_contakt()
                
            case '4':
                edit_contact()

            case '5':
                delete_contact()
                
            case '6':
                break

  
choouse()