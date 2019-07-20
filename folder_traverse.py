import os, shutil

for folder, subFolders, filenames in os.walk('D:\Hopvinna'):
    print("The current Folder " +folder)

    for subFolder in subFolders:
        print("SubFFolder of" +folder+ ' : ' +subFolder)
    
    for filename in filenames:
        print('FILE INSIDE OF ' + folder + ': ' + filename)

    print('')
