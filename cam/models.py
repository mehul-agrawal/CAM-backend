from django.db import models


# Create your models here.

class Subject(models.TextChoices):
    """
    """

    CN = "CN", "Cn"
    DSA = "DSA", "Dsa"


class Assignment():
    name = models.CharField(
        max_length=256,
        help_text="Assignment Name",
        unique=True
    )
    performance_date = models.DateField(
        help_text="Date on which assignment should performed"
    )
    submission_date = models.DateField(
        help_text="Date on which assignment should be submitted"
    )
    subject = models.CharField(
        max_length=20,
        choices=Subject.choices,
        blank=True
    )

class Marks():
    assignment = models.ForeignKey(
        Assignment,
        on_delete=models.RESTRICT,
        related_name="Assignment_marks"
    )
    Rollno = models.IntegerField(
        help_text="Student roll number",
    )
    Spo = models.IntegerField(
        help_text="SPO Marks"
    )
    Rpp = models.IntegerField(
        help_text="RPP Marks"
    )
    academic_year = models.CharField(

    )