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


# 自定义模型管理器Manage类
class StudentManager(models.Manager):
    def get_queryset(self):
        return super(StudentManager, self).get_queryset().filter(sgender=True)

    def createStudent(self, name, age, gender, contend, grade, delete=False):
        student = self.model()
        # print(type(student))
        student.sname = name
        student.sage = age
        student.sgender =gender
        student.scontend = contend
        student.sgrade =grade

        return student


class Student(models.Model):
    # 自定义模型管理器
    stuObj = models.Manager()
    stuObj2 = StudentManager()
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

    # 定义一个类方法创建对象
    @classmethod
    def createStudent(cls, name, age, gender, contend, grade, delete=False):
        stu = cls(sname=name, sage=age, sgender=gender, scontend=contend, sgrade=grade, isDelete=delete)
        return stu



