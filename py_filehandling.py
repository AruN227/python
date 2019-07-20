#Open file
fo = open("python_file.txt", "r+")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)

#Write file
fo.write( "Python is a great language.\nYeah its great!!\nThanks")

#Read file
str = fo.read(79)
print("Content: ",str)

#Check current position
position = fo.tell()
print("Current position: ", position)

fo.close()