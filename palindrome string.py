def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = ''.join(s.split()).lower()
    
    # Compare the string with its reverse
    return s == s[::-1]

# Example usage:
test_string = "Able , was I , I saw eLba"
result = is_palindrome(test_string)
print(f'Is "{test_string}" a palindrome? {result}')
