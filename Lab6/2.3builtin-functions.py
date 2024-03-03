"""
Write a Python program with builtin function that checks whether a passed string is palindrome or not.
"""
def is_palindrome(word):
    word = word.replace(" ", "").lower()
    i = 0
    j = len(word) - 1
    while i < j: 
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True    

x = input("Enter a word or phrase to check, is it palindrome or not\n(code accepts string in this form too: mAda M -> True): ")
print(is_palindrome(x))