def run():
    palindrome = lambda name: name == name[::-1]
    print(palindrome('david'))

if __name__ == '__main__':
    run()