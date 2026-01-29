<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Student Management System</title>
</head>
<body>

<h1>Step 1. MENU</h1>

<p><b>Show:</b></p>

<pre>
======== MENU ========
1. Add Student
2. View Students
3. Search Student
4. Remove Student
5. Exit
</pre>

<p><b>Error handling:</b></p>
<ol>
    <li>ValueError</li>
    <li>input range</li>
</ol>

<hr>

<h1>Step 2. Add student</h1>

<pre>
Enter your choice: 1
Enter student name: cc
Enter roll number: 33
Enter email: cc@gmail.com
Enter department: eng
New student added successfully!
</pre>

<p><b>Error handling:</b></p>
<ol>
    <li>ValueError</li>
    <li>NULL value</li>
    <li>large value</li>
    <li>valid email</li>
    <li>Duplicate roll</li>
</ol>

<hr>

<h1>Step 3. View students</h1>

<p><b>Show all the student</b></p>

<pre>
Enter your choice: 2
============================================================
Name                 Roll       Email               Department
============================================================
aa                   11         aa@                 eee
bb                   22         bb@gmail.com         cse
cc                   33         cc@gmail.com         eng
============================================================
</pre>

<p><b>Error handling:</b></p>
<ol>
    <li>empty file</li>
</ol>

<hr>

<h1>Step 4. Search student</h1>

<pre>
Enter your choice: 3
Enter student roll to search: 33
Name: cc, Roll: 33, Email: cc@gmail.com, Department: eng
</pre>

<p><b>Error handling:</b></p>
<ol>
    <li>ValueError</li>
    <li>value range</li>
    <li>empty file</li>
</ol>

<hr>

<h1>Step 5. Remove student</h1>

<pre>
Enter your choice: 4
Enter student roll to remove: 22
Are you sure you want to remove student with roll 22? (y/n): y
Student with roll 22 removed successfully!
</pre>

<p><b>Error handling:</b></p>
<ol>
    <li>ValueError</li>
    <li>value range</li>
    <li>empty file</li>
</ol>

<hr>

<h1>Step 6. Exit</h1>

<pre>
1. exit the program
</pre>

</body>
</html>
