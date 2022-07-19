import os

for dirpath, dirnames, filenames in os.walk("."):
    for filename in filenames:
        print("Файл:", os.path.join(filename))
        if '(mp3cut.net)' in filename:
            oldtext = filename
            filename = filename.replace('(mp3cut.net)', '')
            os.rename(oldtext, filename)
            print('Стало: ', filename, '\nБыло: ', oldtext)
        if '(1)' in filename or '(2)' in filename or '(3)' in filename or '(4)' in filename:
            oldtext = filename
            try:
                filename = filename.replace('(1)', '')
            except:
                continue
            try:
                filename = filename.replace('(2)', '')
            except:
                continue
            try:
                filename = filename.replace('(3)', '')
            except:
                continue
            try:
                filename = filename.replace('(4)', '')
            except:
                continue
            os.rename(oldtext, filename)
