x = (input("Enter a palindrome ", ))

def reverse(string):
    begin = 0
    end = len(string) - 1
    strlist = [i for i in string]
    while(begin < end):
        temp = strlist[begin]
        strlist[begin] = strlist[end]
        strlist[end] = temp
        begin += 1
        end -= 1
    return ''.join(strlist)

if reverse(x.lower()) == x.lower():
    print("This is is a palindrome")
else:
    print("Not a Palindrome")
