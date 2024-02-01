"""
Write a Python function that checks whether a word or phrase is palindrome or not.
Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
"""
def is_palindrome(word):
    # Remove spaces and convert to lowercase
    word = word.replace(" ", "").lower()
    i = 0
    j = len(word) - 1
    while i < j: 
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True    

x = str(input("Enter a word or phrase to check, whether a word is palindrome or not\n(code accepts string in this form too: mAda M -> True): "))
print(is_palindrome(x))