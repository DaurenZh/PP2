#1
import os
path = 'g:\\testpath\\'
print("Only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nOnly files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\nAll directories and files :")
print([ name for name in os.listdir(path)])
#2
import os
print('Exist:', os.access('c:\\Users\\Public\\C programming library.docx', os.F_OK))
print('Readable:', os.access('c:\\Users\\Public\\C programming library.docx', os.R_OK))
print('Writable:', os.access('c:\\Users\\Public\\C programming library.docx', os.W_OK))
print('Executable:', os.access('c:\\Users\\Public\\C programming library.docx', os.X_OK))
#3 
import os
print("Test a path exists or not:")
path = r'g:\\testpath\\a.txt'
print(os.path.exists(path))
path = r'g:\\testpath\\p.txt'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))
#4
with open(r"myfile.txt", 'r') as fp:
    lines = len(fp.readlines())
    print('Total Number of lines:', lines)
#5
names = ['Jhon', 'Jon', 'Dauren']
with open(r'myfile.txt', 'w') as fp:
    for item in names:
        fp.write("%s\n" % item)
    print('Done')
#6
import string, os
if not os.path.exists("letters"):
   os.makedirs("letters")
for letter in string.ascii_uppercase:
    open(letter + ".txt", "w")
#7
with open('first.txt','r') as firstfile, open('second.txt','a') as secondfile: 
	for line in firstfile: 
			secondfile.write(line)
#8
import os
path = 'C:\Users\zhylk\OneDrive\Рабочий стол\2\1.txt'
try:
	os.remove(path)
	print("% s removed successfully" % path)
except OSError as error:
	print(error)
	print("File path can not be removed")
  
