from django.db import models

# Create your models here.


class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.gname

    class Meta:
        db_table = "grades"
        ordering = ['id']


class Student(models.Model):
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    # 关联外键
    sgrade = models.ForeignKey('Grades', on_delete=models.CASCADE)

    def __str__(self):
        return self.sname

    class Meta:
        db_table = "students"
        ordering = ['id']

    def Getname(self):
        return self.sname



