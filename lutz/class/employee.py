class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @classmethod
    def from_string(cls, data_string):
        data_array = data_string.split('-')
        first_name = data_array[0]
        last_name = data_array[1]
        salary = int(data_array[-1])
        return cls(first_name, last_name, salary)

    def __str__(self):
        return f'First name: {self.first_name}, last Name: {self.last_name}, salary: {self.salary}'


if __name__ == '__main__':
    emp1 = Employee('Alex', 'Zernoklev', '150000')
    emp2 = Employee.from_string('Nastya-Zernokleva-250000')
    print(emp1)
    print(emp2)