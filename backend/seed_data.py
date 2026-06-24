from app import app
from extensions import db

from models import User, Student, Teacher, Subject


with app.app_context():

    # Admin User
    admin = User.query.filter_by(email="admin@example.com").first()

    if not admin:
        admin = User(
            email="admin@example.com",
            role="admin"
        )
        db.session.add(admin)

    # Student User
    student_user = User.query.filter_by(email="ashu@example.com").first()

    if not student_user:
        student_user = User(
            email="ashu@example.com",
            role="student"
        )
        db.session.add(student_user)

    # Teacher User
    teacher_user = User.query.filter_by(email="teacher1@example.com").first()

    if not teacher_user:
        teacher_user = User(
            email="teacher1@example.com",
            role="teacher"
        )
        db.session.add(teacher_user)

    db.session.commit()

    # Student
    student = Student.query.filter_by(
        enrollment_number="0827DD25CA12"
    ).first()

    if not student:
        student = Student(
            user_id=student_user.id,
            enrollment_number="0827DD25CA12",
            name="Ashu",
            department="IMCA",
            semester="2",
            section="A"
        )
        db.session.add(student)

    # Teacher
    teacher = Teacher.query.filter_by(
        teacher_code="T001"
    ).first()

    if not teacher:
        teacher = Teacher(
            user_id=teacher_user.id,
            teacher_code="T001",
            name="Teacher A",
            department="Computer Applications"
        )
        db.session.add(teacher)

    # Subjects
    subjects = [
        ("DS101", "Data Structures", "theory"),
        ("STAT101", "Statistics", "theory"),
        ("POM101", "Principles of Management", "theory")
    ]

    for code, name, subject_type in subjects:

        existing = Subject.query.filter_by(
            subject_code=code
        ).first()

        if not existing:
            db.session.add(
                Subject(
                    subject_code=code,
                    subject_name=name,
                    subject_type=subject_type
                )
            )

    db.session.commit()

    print("Sample data inserted successfully.")