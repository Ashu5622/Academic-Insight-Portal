# Database Design

## Users

Purpose: Store all authenticated users.

Fields:

* id
* email
* role (student, teacher, admin)
* is_active
* created_at

---

## Students

Purpose: Store student information.

Fields:

* id
* user_id
* enrollment_number
* name
* department
* semester
* section
* mobile_number
* profile_photo

---

## Teachers

Purpose: Store teacher information.

Fields:

* id
* user_id
* teacher_code
* name
* department
* mobile_number
* profile_photo

---

## Subjects

Purpose: Store all subjects.

Fields:

* id
* subject_code
* subject_name
* subject_type

---

## Teacher_Subjects

Purpose: Map teachers to subjects.

Fields:

* id
* teacher_id
* subject_id

---

## Attendance_Sessions

Purpose: Store each attendance event.

Fields:

* id
* subject_id
* teacher_id
* attendance_date
* created_at

---

## Attendance_Records

Purpose: Store attendance of each student.

Fields:

* id
* attendance_session_id
* student_id
* status

---

## Exams

Purpose: Store exam types.

Fields:

* id
* exam_name

Examples:

* MST1
* MST2
* Assignment
* Project

---

## Marks

Purpose: Store marks.

Fields:

* id
* student_id
* subject_id
* exam_id
* marks_obtained
* max_marks
* entered_by
* created_at

---

## Mark_Edit_History

Purpose: Track mark modifications.

Fields:

* id
* mark_id
* old_marks
* new_marks
* edited_by
* edit_reason
* edited_at
