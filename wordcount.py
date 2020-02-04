

def word_count(data_file):

    """input = our text of various words
    create empty dictionary
    for loop to go through all of text
    if word is not in dictionary, add it
    if word is already in dictionary, increment occurrence by one
    output = print out line by line word and occurrences """

    data_file = open(data_file)

    word_occurrences = {}

    for line in data_file:
        line.rstrip()
        split_paragraph = line.split()

        for word in split_paragraph:
            word_occurrences[word] = word_occurrences.get(word, 0) + 1

    for word in word_occurrences:
        print(word, word_occurrences[word])

    data_file.close()