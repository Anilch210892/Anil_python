
def flip_words(input_sentense):
    words=input_sentense.split()
    flipped_words=reversed(words)
    flipped_sentense=' '.join(flipped_words)
    return flipped_sentense

input_sentence = "Hello world this is a test"
flipped_sentence = flip_words(input_sentence)
print(flipped_sentence)