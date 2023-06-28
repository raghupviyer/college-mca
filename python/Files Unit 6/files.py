# reading files
f = open('C:/Users/ACER/Projects/MCA/python/Files Unit 6/text.txt', 'r')
print(f.read())
print(f.read(10))
print(f.mode)
f.close()

# append files
f = open('C:/Users/ACER/Projects/MCA/python/Files Unit 6/text.txt', 'a')
f.write("hi") 
#though the name of the function is write, 
# it will append and not write because the mode in which the file was opened was append and not write, 
# there is another mode called write ('w')
f.close()


# write files
f = open('C:/Users/ACER/Projects/MCA/python/Files Unit 6/text.txt', 'w')
f.write("hi")
f.close()

# delete a file
import os
if os.path.exists('C:/Users/ACER/Projects/MCA/python/Files Unit 6/text.txt'):
  os.remove('C:/Users/ACER/Projects/MCA/python/Files Unit 6/text.txt')
else:
  print("this file does not exist")