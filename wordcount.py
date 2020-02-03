# put your code h
file_name = open('test.txt')

'''Write a program, wordcount.py, that opens a file and counts how many times
each space-separated word occurs in that file. Your program should then print
those counts to the screen.

We’ve included a small file, test.txt, that you can use for testing out your
script. The file contains this poem:

test.txt
As I was going to St. Ives
I met a man with seven wives
Every wife had seven sacks
Every sack had seven cats
Every cat had seven kits
Kits, cats, sacks, wives.
How many were going to St. Ives? '''


def count_word(file_name):

    word_count = {}

    for line in file_name:
        line = line.rstrip()
        words = line.split(' ')
        print(words)
        # line.rstrip(' ')
        # print(line)

        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

    return word_count


print(count_word(file_name))


# first we need to open the file.
# take it line by line
# split the line using split('')
# then word by word
# then  iterate the word to get the word count
