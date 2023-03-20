## This doesn't work too well and I did not have the time to work more on it before it was due :(
## I'm not sure if I entirely understand how to use the find function or if it would be easier to use a different one in this case
## I was also unsure of how to print the line number

print('Opening origin.txt')
with open('origin.txt', 'r') as file:
    print('Opening originoutput.txt')
    with open('originoutput.txt', 'w') as out_file:
        for line in file:
            line = line.strip()
            word_list = line.split()
            all_herits = "*herit*"
            words = word_list.find(all_herits)
            for word in words:
                out_file.write('{0}\n'.format(line))
                out_file.write('{0}\t'.format(word))
print("Words found! (hopefully)")
print('origin.txt is closed?', file.closed)
print('originoutput.txt is closed?', out_file.closed)
