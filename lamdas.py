def run():
    txt = str(input("enter name: "))
    palindrome = lambda name: name == name[::-1]
    print(palindrome(txt))

if __name__ == '__main__':
    run()