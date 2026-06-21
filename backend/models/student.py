from extensions import db


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    enrollment_number = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    name = db.Column(db.String(100), nullable=False)

    department = db.Column(db.String(100))

    semester = db.Column(db.String(20))

    section = db.Column(db.String(20))