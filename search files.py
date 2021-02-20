from easygui import *
import os

output = []


def find(key, root_dir):
    os.chdir(root_dir)
    cur_dir = os.listdir()
    for each in cur_dir:
        new_dir = os.path.join(root_dir, each)
        if os.path.isdir(new_dir):
            find(key, new_dir)
        if key in each and not os.path.isdir(new_dir):
            output.append(each + '\n' + new_dir)
    return output
             

key = enterbox('Input keywords of the file:', 'Search files')
root_dir = enterbox('Search in:', 'Search files')
result_list = find(key, root_dir)
result = ''
for each in result_list:
    result = result + each + '\n'
codebox('The result are:', 'Search results', result)
