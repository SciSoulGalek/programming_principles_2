"""
Write a function that accepts string from user, return a sentence with the words reversed.
We are ready -> ready are We
"""
def reverse_sentence(string):
    words = string.split()
    words = words[::-1]
    reversed_sentence = ' '.join(words)
    return reversed_sentence
user_input = input("Enter a sentence: ")
print(reverse_sentence(user_input))