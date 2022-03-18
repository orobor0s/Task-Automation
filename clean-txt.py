import re

# if you know patterns of characters you'd like to remove from text, copy the first expression and put each pattern in the first set of parentheses
def cleantxt(file, txt, name):
    txt = re.sub("", "", txt) #(string you want to replace, what you're replacing it with, input type)

    newFile = open(name, 'w', encoding = 'UTF-8')
    newFile.write(txt)
    newFile.close()
    print('complete')

file = open("", encoding = "UTF-8") # file path of the txt file you want to clean
txt = file.read()
name = "" # name of new file
cleantxt(file, txt, name)
