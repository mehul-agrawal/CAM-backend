from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Subject(models.TextChoices):
    CN = "CN", "Computer Networks"
    DSA = "DSA", "Data Structures and Algorithms"
class Course(models.TextChoices):
    CS = "CS", "Computer Science"
    IT = "IT", "Information Technology"
class Assignment(models.Model):
    name = models.CharField(
        max_length=256,
        help_text="Assignment Name",
        unique=True
    )
    performance_date = models.DateField(
        help_text="Date on which assignment should be performed"
    )
    submission_date = models.DateField(
        help_text="Date on which assignment should be submitted"
    )
    subject = models.CharField(
        max_length=20,
        choices=Subject.choices,
    )

class Marks(models.Model):
    assignment = models.ForeignKey(
        Assignment,
        on_delete=models.RESTRICT,
        related_name="marks"
    )
    roll_number = models.IntegerField(
        help_text="Student roll number"
    )
    spo_marks = models.IntegerField(
        help_text="SPO Marks",
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    rpp_marks = models.IntegerField(
        help_text="RPP Marks",
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    academic_year = models.CharField(
        max_length=20,
        help_text="Academic Year"
    )
    course = models.CharField(
        max_length=20,
        choices=Course.choices,
        help_text="course"
    )
    performance_date = models.DateField(
        help_text="Date on which assignment was performed by student"
    )
    submission_date = models.DateField(
        help_text="Date on which assignment was submitted by student"
    )
    