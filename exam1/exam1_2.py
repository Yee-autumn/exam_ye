
# py没有指针，所以这道题有点不符合题目要求
class Student:
    def __init__(self):
        self.name=""
        self.id=0
        self.score=0.0


def input_stu (stu):
    stu.name=input("姓名：")
    stu.id=int(input("学号："))
    stu.score=float(input("成绩："))


def display(stu):
    print(f"姓名：{stu.name}")
    print(f"学号：{stu.id}")
    print(f"成绩：{stu.score}")


def main():
    stu=Student()
    input_stu(stu)
    display(stu)


if __name__=='__main__':
    main()