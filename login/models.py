from django.db import models

class User(models.Model):
#        TA = "TA"
#        PROFESSOR = "PR"
#        STUDENT = "ST"
#        statusChoices = (
#                (TA, 'Teaching Assistant'),
#                (PROFESSOR, 'Professor'),
#                (STUDENT, 'Student'),
#        )
#        username = models.CharField(max_length=50)
        firstName = models.CharField(max_length=50)
        lastName = models.CharField(max_length=50)
#        school = models.CharField(max_length=50)
#        studentID = models.CharField(max_length=10)
        email = models.CharField(max_length=50)
#        status = models.CharField(max_length=2, choices=statusChoices, default=STUDENT)

        def __str__(self):
            return self.firstName

#class Course(models.Model):
#        # these field points to tuple in User DB
#        professor = models.ForeignKey(
#                'User',
#                on_delete=models.CASCADE
#        )
#        ta = models.ForeignKey(
#                'User',
#                on_delete=models.CASCADE
#        )
#        school = models.CharField(max_length=50)
#        title = models.CharField(max_length=50)
#
#class Roster(models.Model):
#        studentID = models.ForeignKey(
#                'User',
#                on_delete=models.CASCADE
#        )
#        courseID = models.ForeignKey(
#                'Course',
#                on_delete=models.CASCADE
#        )
