import shutil, os

print(os.getcwd())

for folderName, subfolder, filenames in os.walk(os.getcwd()):
    for file in filenames:
        if file.startswith('Harvard'):
            shutil.move(file,os.getcwd()+'\Harvard')
            print('Done')

	    
