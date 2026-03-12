students = []

def add_student():
    num = input("请输入学号:")
    name = input("请输入姓名:")
    gender = input("请输入性别:")
    written_score = input("请输入笔试成绩:")
    sports_score = input("请输入体育成绩:")
    student = {"num": num, "name": name, "gender": gender, "written_score": written_score, "sports_score": sports_score}
    students.append(student)
    print("学生信息添加成功！")

def delete_student():
    num = input("请输入要删除的学号:")
    for student in students:
        if num == student.get("num"):
            students.remove(student)
            print("学生的信息删除成功！")
            break
    else:
        print("未找到")

def modify_student():
    num = input("请输入要修改的学号:")
    for student in students:
        if num == student.get("num"):
            print("1. 修改姓名")
            print("2. 修改性别")
            print("3. 修改笔试成绩")
            print("4. 修改体育成绩")
            choice = input("请选择要修改的信息:")
            if choice == "1":
                name = input("请输入修改后的姓名:")
                student["name"] = name
            elif choice == "2":
                gender = input("请输入修改后的性别:")
                student["gender"] = gender
            elif choice == "3":
                written_score = input("请输入修改后的笔试成绩:")
                student["written_score"] = written_score
            elif choice == "4":
                sports_score = input("请输入修改后的体育成绩:")
                student["sports_score"] = sports_score
            else:
                print("输入有误！")
            print("学生信息修改成功！")
            break
    else:
        print("未找到")

def show_students(students_list, search_num="", search_name="", score_type="written_score"):
    print("学号\t姓名\t性别\t笔试成绩\t体育成绩")
    if score_type not in ["written_score", "sports_score"]:
        print("输入错误")
        return
    sorted_students = sorted(students_list, key=lambda x: int(x[score_type]), reverse=True)
    for student in sorted_students:
        if (not search_num and not search_name) or (search_num and search_num == student.get("num")) or (search_name and search_name == student.get("name")):
            print(student.get("num") + "\t" + student.get("name") + "\t" + student.get("gender") + "\t" + student.get("written_score") + "\t" + student.get("sports_score"))

def sort_students():
    print("排序方式：")
    print("1. 按照笔试成绩升序排序")
    print("2. 按照笔试成绩降序排序")
    print("3. 按照体育成绩升序排序")
    print("4. 按照体育成绩降序排序")
    choice = input("请选择排序方式:")
    if choice == "1":
        show_students(students, score_type="written_score")
    elif choice == "2":
        show_students(students, score_type="written_score", search_num="", search_name="")
    elif choice == "3":
        show_students(students, score_type="sports_score")
    elif choice == "4":
        show_students(students, score_type="sports_score", search_num="", search_name="")
    else:
        print("输入有误！")

while True:
    print("------------2022级软件工程四班------------")
    print("学生信息管理系统")
    print("1. 添加学生信息")
    print("2. 删除学生信息")
    print("3. 修改学生信息")
    print("4. 显示学生信息")
    print("5. 排序")
    print("6. 退出")
    print("------------2022级软件工程四班------------")
    choice = input("请输入您的选择:")

    if choice == "1":
        add_student()
    elif choice == "2":
        delete_student()
    elif choice == "3":
        modify_student()
    elif choice == "4":
        print("1. 显示所有信息")
        print("2. 根据学号查询信息")
        print("3. 根据姓名查询信息")
        print("4. 退出查询")
        search_choice = input("请选择查询方式:")
        if search_choice == "1":
            show_students(students)
        elif search_choice == "2":
            num = input("请输入要查询的学生学号:")
            show_students(students, search_num=num)
        elif search_choice == "3":
            name = input("请输入要查询的学生姓名:")
            show_students(students, search_name=name)
        elif search_choice == "4":
            print("退出查询！")
        else:
            print("输入有误")
    elif choice == "5":
        sort_students()
    elif choice == "6":
        print("学生信息管理系统已退出！")
        break
    else:
        print("输入有误")
