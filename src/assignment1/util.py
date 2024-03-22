def cal_avg():
    # student_marks = {}
    # for _ in range(n):
    #     name, *line = student_data[_].split()
    #     scores = list(map(float, line))
    #     student_marks[name] = scores
    #
    # if query_name in student_marks:
    #     avg = sum(student_marks[query_name]) / len(student_marks[query_name])
    #     return "{:.2f}".format(avg)
    n = int(input())
    student_dat = input().split()
    name = int(input())
    if name==student_dat[0]:
        print(student_dat[1:])
cal_avg()

