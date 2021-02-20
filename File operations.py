import os
import os.path


def search(keyword):
    dir_list = os.listdir()
    result_list = []
    for each in dir_list:
        if os.path.isdir(each):
            search(each)
        elif keyword in each:
            result_list.append(os.curdir+'each')
    return result_list


def create(file_name, location, content):
    os.chdir(location)
    with open(file_name, "w") as f:
        f.write(content)


def start_working():
    while True:
        dir = input('working dir:')
        if not os.path.isdir(dir):
            print('dir do not exist')
        os.chdir(dir)

        type = input('input 1 to search, 2 to create and 3 to quit: ')

        if type == 1:
            keyword = input('keyword of file: ')
            pass
            search(keyword)
        elif type == 2:
            file_name = input('name of file: ')
            location = input('where you want to create the file: ')
            content = input('content: \n')
            create(file_name, location, content)
        elif type == 3:
            break
        else:
            print('not defined')
