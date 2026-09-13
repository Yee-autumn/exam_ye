#include <iostream>

using namespace std;

//定义结构体
struct Student
{
	char name[50];
	int id;
	double score;
};

void input(Student* p)
{
	cin >> p->name >> p->id >> p->score;
}

void display(Student* p)
{
	cout << "姓名：" << p->name << endl;
	cout << "学号：" << p->id << endl;
	cout << "成绩：" << p->score << endl;
}

int main()
{
	Student* stu = new Student;
	input(stu);
	display(stu);
	delete stu;
	return 0;
	return 0;
}