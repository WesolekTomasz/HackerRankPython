def validation(sentence):
    print(any([char.isalnum() for char in sentence]))
    print(any([char.isalpha() for char in sentence]))
    print(any([char.isdigit() for char in sentence]))
    print(any([char.islower() for char in sentence]))
    print(any([char.isupper() for char in sentence]))
        
if __name__ == '__main__':
    s = input()
    validation(s)