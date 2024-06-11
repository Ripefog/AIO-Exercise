def count_words_in_file(path):
    word_count = {}
    with open(path, 'r') as file:
        for line in file:
            words = line.lower().split()

            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    return word_count

path = 'P1_data.txt'
print(count_words_in_file(path))