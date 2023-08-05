class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Error'

    def average_grade(self):
        sum_grades = 0
        len_grades = 0
        for course in self.grades.values():
            sum_grades += sum(course)
            len_grades += len(course)
        avg_grade = round(sum_grades / len_grades, 1)
        return avg_grade

    def __str__(self):
        text = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade()}\nКурсы в процессе изучения: {",".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return text

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Нельзя сравнивать!")
            return
        return self.average_grade() < other.average_grade()

    def average_grades_for_course(self, course):
        sum_grades = 0
        len_grades = 0
        for crs in self.grades.keys():
            if crs == course:
                sum_grades += sum(self.grades[course])
                len_grades += len(self.grades[course])
        avg_grade_crs = round(sum_grades / len_grades, 1)
        return avg_grade_crs


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        sum_grades = 0
        len_grades = 0
        for course in self.grades.values():
            sum_grades += sum(course)
            len_grades += len(course)
        avg_grades = round(sum_grades / len_grades, 1)
        return avg_grades

    def __str__(self):
        text = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}'
        return text

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Нельзя сравнивать!")
            return
        return self.average_grade() < other.average_grade()

    def average_grades_for_course(self, course):
        sum_grades = 0
        len_grades = 0
        for crs in self.grades.keys():
            if crs == course:
                sum_grades += sum(self.grades[course])
                len_grades += len(self.grades[course])
        avg_grade_crs = round(sum_grades / len_grades, 1)
        return avg_grade_crs


class Reviewer(Mentor):
    def __int__(self, name, surname):
        super.__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

# Студенты Студентовы

student_1 = Student('Иван', 'Студентов', 'м')
student_1.courses_in_progress += ['Goland']
student_1.finished_courses += ['Python']

student_2 = Student('Мария', 'Студентова', 'ж')
student_2.courses_in_progress += ['Goland']
student_2.finished_courses += ['Python']

# Лекторы Лекторовы

lecturer_1 = Lecturer('Анастасия', 'Лекторова')
lecturer_1.courses_attached += ['Goland']

lecturer_2 = Lecturer('Милана', 'Лекторова')
lecturer_2.courses_attached += ['Goland']

# Проверяющие Проверяловы

reviewer_1 = Reviewer('Владимир', 'Проверялов')
reviewer_1.courses_attached += ['Goland']

reviewer_2 = Reviewer('Степан', 'Проверялов')
reviewer_2.courses_attached += ['Goland']

# Оценки Студентовым за домашнее задание

reviewer_1.rate_hw(student_1, 'Goland', 8)
reviewer_1.rate_hw(student_1, 'Goland', 10)
reviewer_1.rate_hw(student_1, 'Goland', 6)

reviewer_2.rate_hw(student_2, 'Goland', 2)
reviewer_2.rate_hw(student_2, 'Goland', 1)
reviewer_2.rate_hw(student_2, 'Goland', 4)

# Оценки Лекторовым за лекцию

student_1.rate_lecture(lecturer_1, 'Goland', 10)
student_1.rate_lecture(lecturer_1, 'Goland', 8)
student_1.rate_lecture(lecturer_1, 'Goland', 5)

student_2.rate_lecture(lecturer_2, 'Goland', 7)
student_2.rate_lecture(lecturer_2, 'Goland', 8)
student_2.rate_lecture(lecturer_2, 'Goland', 5)

list_student = [student_1, student_2]
list_lecturer = [lecturer_1, lecturer_2]
list_reviewer = [reviewer_2, reviewer_1]

def average_grade_for_course(course, list_student):
    sum_grades = 0
    qtl_grades = 0
    for student in list_student:
        for course in student.grades:
            student_sum_grades = student.average_grades_for_course(course)
            sum_grades += student_sum_grades
            qtl_grades += 1
    avg_grades = round(sum_grades / qtl_grades, 1)
    return avg_grades

print('=' * 10)
print(f'Средняя оценка за домашнее задание всех студентов: {average_grade_for_course("Goland", list_student)}')
print(f'Средняя оценка за проведенные лекции по всем лекторам: {average_grade_for_course("Goland", list_lecturer)}')
print('=' * 10)
print(student_1)
print('-' * 10)
print(student_2)
print('=' * 10)
print(lecturer_1)
print('-' * 10)
print(lecturer_2)
print('=' * 10)
print(reviewer_1)
print('-' * 10)
print(reviewer_2)
print('=' * 10)
