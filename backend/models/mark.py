from datetime import datetime
from extensions import db


class Mark(db.Model):
    __tablename__ = "marks"

    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=False
    )

    subject_id = db.Column(
        db.Integer,
        db.ForeignKey("subjects.id"),
        nullable=False
    )

    exam_id = db.Column(
        db.Integer,
        db.ForeignKey("exams.id"),
        nullable=False
    )

    marks_obtained = db.Column(db.Float)

    max_marks = db.Column(db.Float)


class MarkEditHistory(db.Model):
    __tablename__ = "mark_edit_history"

    id = db.Column(db.Integer, primary_key=True)

    mark_id = db.Column(
        db.Integer,
        db.ForeignKey("marks.id"),
        nullable=False
    )

    old_marks = db.Column(db.Float)

    new_marks = db.Column(db.Float)

    edited_by = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    edited_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )