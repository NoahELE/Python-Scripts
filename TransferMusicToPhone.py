import os, shutil

os.chdir('D:\\Music')
origin_dir = [x for x in os.listdir('D:\\Music') if os.path.isfile(x) and os.path.splitext(x)[1]=='.mp3']
destination_dir = [x for x in os.listdir('Noah\'s Honor Play\
    \\Internal shared storage\\MusicDownload') if os.path.isfile(x) and os.path.splitext(x)[1]=='.mp3']
