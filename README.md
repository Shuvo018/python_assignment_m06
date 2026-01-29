<h1>Step 1. MENU </h1>
Show:<br>
======== MENU ========<br>
1. Add Student<br>
2. View Students<br>
3. Search Student<br>
4. Remove Student<br>
5. Exit<br>

<b>Error handling: </b>
1. ValueError
2. input range 

<h1>Step 2. Add student </h1>
Enter your choice: 1<br>
Enter student name: cc<br>
Enter roll number: 33<br>
Enter email: cc@gmail.com<br>
Enter department: eng<br>
New student added successfully!<br>

<b>Error handling: </b>
1. ValueError
2. NULL value
3. large value
4. valid email
5. Duplicate roll

<h1>Step 3. View students </h1>
<b>Show all the student</b>
Enter your choice: 2
============================================================
Name                 Roll       Email                Department
============================================================
aa                   11         aa@                  eee
bb                   22         bb@gmail.com         cse
cc                   33         cc@gmail.com         eng
============================================================
<b>Error handling: </b>
1. empty file

<h1>Step 4. Search student </h1>
Enter your choice: 3
Enter student roll to search: 33
Name: cc, Roll: 33, Email: cc@gmail.com, Department: eng
<b>Error handling: </b>
1. ValueError
2. value range
3. empty file


<h1>Step 5. Remove student </h1>
Enter your choice: 4
Enter student roll to remove: 22
Are you sure you want to remove student with roll 22? (y/n): y
Student with roll 22 removed successfully!
<b>Error handling: </b>
1. ValueError
2. value range
3. empty file
<h1>Step 6. Exit </h1>
1. exit the program