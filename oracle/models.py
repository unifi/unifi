from django.db import models

# Create your models here.
from student.models import Student

class Oracle(Student):
    """ Oracle
    Student with a certain expertise.
    Assigned to one or many groups.
    """
    pass