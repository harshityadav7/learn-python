"""Given the names and grades for each student in a class of N students, store them in a
nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically
and print each name on a new line."""
if __name__ == '__main__':
    li = []
    scoreli = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        li.append([name, score])
        scoreli.append(score)
    # print(li)
    li.sort(key=lambda li_element: li_element[0])
    # print(li)
    scoreli=list(set(scoreli))
    scoreli.sort()
    var=scoreli[1]
    # print(var)
    for i in li:
        if var==i[1]:
            print(i[0])


