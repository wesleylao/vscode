s1 = 'How do you do who are you'
s2 = 'What do you think how are you' # just for example
#TODO
################################

words_s1 = s1.lower().split()
words_s2 = s2.lower().split()

common_words = []
for word in words_s1:
    if word in words_s2 and word not in common_words:
        common_words.append(word)

print(sorted(common_words))

################################
