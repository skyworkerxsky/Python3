filename = "teext.txt"

with open(filename) as file_object:
    contents = file_object.read()

with open(filename) as file_object:
    for line in file_object:
        print(line)

with open(filename) as file_object:
    lines = file_object.readlines()

print(lines)

filename = 'million_degits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(f"{pi_string[:52]}...")
print(len(pi_string))

# write_message
'''
Файлы можно открывать:
- в режиме чтения ('r'),
- записи ('w'), 
- присоединения ('a') или в режиме, допускающем как чтение, так и запись в файл ('r+'). 

Если аргумент режима не указан, Python по умолчанию, открывает файл в режиме только для чтения.
'''

filename = 'preogramming_text.txt'
with open(filename, 'w') as file_object:
    file_object.write('Test sentence.')
    file_object.write("Second sentence.")

filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")