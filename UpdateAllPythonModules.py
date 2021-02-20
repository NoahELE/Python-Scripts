import pip


import subprocess


p = subprocess.Popen('pip list -o', shell = True, stdout = subprocess.PIPE)
outdated_list = str(p.communicate()[0], 'utf-8')

need_update = []

for i in outdated_list.splitlines()[2:]:
    need_update.append(i.split(' ')[0])

for i in need_update:
    com_update = 'pip install -U ' + i
    subprocess.call(com_update)
    print('updated:' + i)

print('check updates:\n')
subprocess.call('pip list -o')