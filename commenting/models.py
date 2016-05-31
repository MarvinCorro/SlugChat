from django.db import models
from datetime import datetime
from home.models import User

#a placeholder table that Comment can reference.
class File(models.Model):
    file = models.CharField(max_length=200)
    def __str__(self):
        return self.file

#the real Comment table. must change referenced table.
class Comment(models.Model):
    #change the following line to reference whatever table is desired
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    #the comment itself, simple text field
    comment = models.CharField(max_length=200)
    #creates a reference to the user who made the comment
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #pub_date is auto pulled. make sure datetime import is present
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.comment