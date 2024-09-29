if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        average_score = round(sum(map(float, line)) / len(line), 2)
        student_marks[name] = average_score
    query_name = input()
    print('%.2f'% student_marks[query_name])


