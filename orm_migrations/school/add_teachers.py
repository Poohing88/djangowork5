from school.models import Student, Teacher, StudentTeacher

student1 = Student.objects.get(id=1)
student2 = Student.objects.get(id=2)
student3 = Student.objects.get(id=3)
teacher1 = Teacher.objects.get(id=1)
teacher2 = Teacher.objects.get(id=2)
teacher3 = Teacher.objects.get(id=3)
student1.teacher.add(teacher1)
student2.teacher.add(teacher2)
student3.teacher.add(teacher3)