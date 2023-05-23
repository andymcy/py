#1
with open('names.txt', 'r') as file:
    longest_name = max(file.read().split(), key=len)
print(longest_name)

#2
with open('names.txt', 'r') as file:
    total_length = sum(len(line.strip()) for line in file)
print(total_length)

#3
with open('names.txt', 'r') as file:
    shortest_names = [line.strip() for line in file if len(line.strip()) == 2]
print('\n'.join(shortest_names))

#4
with open('names.txt', 'r') as input_file, open('name_length.txt', 'w') as output_file:
    for line in input_file:
        name = line.strip()
        length = str(len(name))
        output_file.write(length + '\n')
