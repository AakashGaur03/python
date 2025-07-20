file = open('youtube.txt')
file = open('youtube.txt','w')

try:
    file.write('Add This Text')
finally:
    file.close()

# with open('youtube.txt','w') as file:
#     file.write("Some more")