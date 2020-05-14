from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("A Good Man")


def detail(request, question_id, question_id2):
    return HttpResponse("You're looking at question %s or %s." % (question_id, question_id2))



from.models import Grades

from django.db.models import F, Q
def grades(request):
    # 在模板中取数据

    gradesList = Grades.objects.all()
    # F对象
    g = Grades.objects.filter(ggirlnum__gt=F('gboynum')+2)
    print(g)
    


    # 将数据传递给模板,模板在渲染页面，返回给浏览器

    return render(request, 'myApp/grades.html', {"grades": gradesList})


from.models import Student, Grades


def Stu(request):
    stuList = Student.stuObj.all()

    return render(request, 'myApp/Students.html', {"Students": stuList})


#从模型类中添加信息
def addStu(request):
    grade = Grades.objects.get(pk=1)
    stu = Student.createStudent("刘德华", 53, True, '我是天王', grade)
    stu.save()
    return HttpResponse("awxdeodjdsfjs")


# 从管理器中添加信息
def addStu2(request):
    grade = Grades.objects.get(pk=1)
    stu = Student.stuObj2.createStudent("张学友", 78, True, '张宝美比我帅气', grade)
    stu.save()
    return HttpResponse("**********")


# 显示前5条学生信息
def showStu(request):
    stuList = Student.stuObj.all()[0:5]
    return render(request, 'myApp/Students.html', {"Students": stuList})


# 分页显示
def showStuPage(request, page):
    # 0-5  5-10  10-15
    #   1   2      3

    stuList = Student.stuObj.all()[(page - 1)*4:page*4]
    return render(request, 'myApp/Students.html', {"Students": stuList})

# 引入聚合函数
from django.db.models import Max, Min

# 字段查询
def studentsearch(request):
    # 01、包含某个字段
    # studentsList = Student.stuObj.filter(sname__contains='刘')

    # 02、以某个value开头或结尾
    # studentsList = Student.stuObj.filter(sname__startswith="张")

    # 03、是否包含在范围内
    # studentsList = Student.stuObj.filter(pk__in=[1, 3, 5, 7, 9])

    # 03、大于等于36
    # studentsList = Student.stuObj.filter(sage__gte=36)

    # 04 跨关联查询
    grade = Grades.objects.filter(student__scontend__contains="张宝美")
    print(grade)

    # 聚合函数
    maxAge = Student.stuObj.aggregate(Max('sage'))
    print(maxAge)

    # Q对象
    studentsList = Student.stuObj.filter(Q(sage__gte=50) | Q(sage__lte=25))

    return render(request, 'myApp/Students.html', {"Students": studentsList})


