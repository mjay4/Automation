import shutil, os

for filename in os.listdir():
    if filename.endswith('.pdf'):
        shutil.move(filename,os.getcwd()+'\PDF')
    else:
        if filename.endswith('.jpg'):
            shutil.move(filename,os.getcwd()+'\IMG')
        else:
            if filename.endswith('.mp4'):
                shutil.move(filename,os.getcwd()+'\VIDEO')
            else:
                if filename.endswith('.mp3'):
                     shutil.move(filename,os.getcwd()+'\AUDIO')
                else:
                    if filename.endswith('.docx'):
                     shutil.move(filename,os.getcwd()+'\TEXT')
