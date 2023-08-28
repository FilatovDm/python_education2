"""
Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним классы исключения
с выводом подробной информации. Поднимайте исключения внутри основного кода. Например нельзя создавать прямоугольник
со сторонами отрицательной длины.
"""

from student import Student

student = Student("дмитрий Филатов", "filatov.csv")
student.add_score("rus_lang", 5)
student.add_test_result("math", 95)
print(student.average_test_score("math"))
print(student.average_score())
