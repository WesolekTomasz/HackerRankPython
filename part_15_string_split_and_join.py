
def split_and_join(line):
    arr_split = list(line.split())
    joiner = "-".join(arr_split)
    return joiner

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)