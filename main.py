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

    def average_grades_home(self):
        sum_grades = 0
        len_grades = 0
        for course in self.grades.values():
            sum_grades += sum(course)
            len_grades += len(course)
        avg_grade = round(sum_grades / len_grades, 1)
        return avg_grade

    def __str__(self):
        text = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grades_home()}\nКурсы в процессе изучения: {",".join(self.courses_in_progress)}\nЗавершенные курсы:{", ".join(self.finished_courses)}'
        return text


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __int__(self, name, surname):
        super.__init__(name, surname)
        self.grades = {}

    def average_grade_lecture(self):
        sum_grades = 0
        len_grades = 0
        for course in self.grades.values():
            sum_grades += sum(course)
            len_grades += len(course)
        avg_grades = round(sum_grades / len_grades, 1)
        return avg_grades

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade_lecture()}'


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


