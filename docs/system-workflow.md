\# System Workflow



\## Student Login Workflow



Student opens portal



↓



Click "Login with Google"



↓



Google authenticates student



↓



System checks email in Users table



↓



If approved:



\* Create session

\* Redirect to Student Dashboard



If not approved:



\* Access Denied



\---



\## Teacher Login Workflow



Teacher opens portal



↓



Click "Login with Google"



↓



Google authenticates teacher



↓



System checks email in Users table



↓



If approved:



\* Create session

\* Redirect to Teacher Dashboard



If not approved:



\* Access Denied



\---



\## Student Dashboard Workflow



Student logs in



↓



View Profile



↓



View Attendance



↓



View Marks



↓



Logout



\---



\## Teacher Attendance Workflow



Teacher logs in



↓



Select Subject



↓



Select Semester / Section



↓



Create Attendance Session



↓



View Student List



↓



Mark Present / Absent



↓



Save Attendance



↓



Attendance Records Created



\---



\## Student Attendance Workflow



Student logs in



↓



Open Attendance Page



↓



System fetches attendance records



↓



Calculate attendance percentage



↓



Display subject-wise attendance



\---



\## Teacher Marks Workflow



Teacher logs in



↓



Select Subject



↓



Select Exam



↓



Select Student



↓



Enter Marks



↓



Save Marks



↓



Marks Record Created



\---



\## Marks Edit Workflow



Teacher opens existing marks



↓



Modify marks



↓



Save changes



↓



Update Marks table



↓



Create Mark\_Edit\_History record



↓



Store:



\* Old marks

\* New marks

\* Edited by

\* Edit reason

\* Edit timestamp



\---



\## Student Marks Workflow



Student logs in



↓



Open Marks Page



↓



System fetches marks



↓



Display subject-wise marks



↓



Display exam-wise marks



\---



\## Admin Workflow



Admin logs in



↓



View Students



↓



Approve / Disable Student Accounts



↓



View Teachers



↓



Approve / Disable Teacher Accounts



↓



View Attendance Data



↓



View Marks Data



↓



View Audit Logs



\---



\## Logout Workflow



User clicks Logout



↓



Session destroyed



↓



Redirect to Login Page



