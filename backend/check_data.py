from app import app
from models import User, Student, Teacher, Subject

with app.app_context():

    print("\nUSERS")
    for user in User.query.all():
        print(user.id, user.email, user.role)

    print("\nSTUDENTS")
    for student in Student.query.all():
        print(
            student.id,
            student.enrollment_number,
            student.name
        )

    print("\nTEACHERS")
    for teacher in Teacher.query.all():
        print(
            teacher.id,
            teacher.teacher_code,
            teacher.name
        )

    print("\nSUBJECTS")
    for subject in Subject.query.all():
        print(
            subject.id,
            subject.subject_code,
            subject.subject_name
        )