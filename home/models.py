from django.db import models


class User(models.Model):
        TA = "TA"
        PROFESSOR = "PR"
        STUDENT = "ST"
        statusChoices = (
                (TA, 'Teaching Assistant'),
                (PROFESSOR, 'Professor'),
                (STUDENT, 'Student'),
        )
        userID = models.CharField(max_length=100)
        firstName = models.CharField(max_length=50)
        lastName = models.CharField(max_length=50)
        school = models.CharField(max_length=50)
        studentID = models.CharField(max_length=10)
        email = models.CharField(max_length=50, unique=True)
        status = models.CharField(max_length=2,
                                  choices=statusChoices, default=STUDENT)
        profile_pic = models.CharField(max_length=200, default='N/A')
        completeProfile = models.BooleanField(default=False)

        def get_status(self):
            if self.status == "TA":
                return 'Teaching Assistant'
            elif self.status == "ST":
                return 'Student'
            elif self.status == "PR":
                return 'Professor'

        def __str__(self):
            return self.firstName


class Course(models.Model):
        # these field points to tuple in User DB
        professor = models.ForeignKey(
                'User',
                on_delete=models.CASCADE,
                related_name='professor',
        )
        ta = models.ForeignKey(
                'User',
                on_delete=models.CASCADE,
                # Make TA field optional
                null=True,
                blank=True,
                related_name='ta',
        )
        school = models.CharField(max_length=50)
        title = models.CharField(max_length=50)

        def __str__(self):
            return self.title


class Roster(models.Model):
        studentID = models.ForeignKey(
                'User',
                on_delete=models.CASCADE
        )
        courseID = models.ForeignKey(
                'Course',
                on_delete=models.CASCADE
        )

        def __str__(self):
            return self.courseID.title
