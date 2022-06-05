def get_student_names(students:dict):
    '''
    Напишите функцию, которая вернет массив с именами студентов в алфавитном порядке. Принимать она должна словарь.
    '''
    return sorted(students.values())


if __name__ == '__main__':
    students = {'student1': 'George', 'student2': 'Benjamin', 'student3': 'Alex'}
    get_student_names(students)
    print(get_student_names(students))
