from student import Student
from group import Group
from exceptions import GroupLimitError

def main():
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

    gr = Group('PD1')
    gr.add_student(st1)
    gr.add_student(st2)

    print(gr)

    assert gr.find_student('Jobs') == st1
    assert gr.find_student('Jobs2') is None

    gr.delete_student('Taylor')
    print(gr)

    try:
        for i in range(3, 13):
            student = Student(
                'Male',
                20,
                f'Student{i}',
                f'LastName{i}',
                f'AN14{i}'
            )
            gr.add_student(student)
    except GroupLimitError as e:
        print(e)


if __name__ == "__main__":
    main()