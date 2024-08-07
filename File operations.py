names = "C:/Users/CareersIT/Desktop/Names.txt.txt"
output = "C:/Users/CareersIT/Desktop/Output.txt.txt"

#reading files and displaying them
with open(names, 'r') as file:
    text = file.read()
    wordCount = len(text.split())
    print(text)
    print("Word count: ",wordCount)

#writing to a file
with open(output, 'w') as file:
    line1 = file.write('Careers IT\n')
    line2 = file.write('System Developers\n')
    line3 = file.write('Assessor - Mr Masiya')
    file.close()