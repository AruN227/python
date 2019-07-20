def reverse(s):
    return s[::-1]


def isPalindrome(s):
    rev = reverse(s)

    if(s == rev):
        return True
    return False


s = "malayala"
result = isPalindrome(s)

if result == 1:
    print('Palindrome')
else:
    print('Not palindrome')