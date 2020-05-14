from django.contrib import admin

# Register your models here.
from.models import Grades, Student


class StuentInfo(admin.TabularInline):
                # admin.StackedInline
    model = Student
    extra = 2


class GradesAdmin(admin.ModelAdmin):
    inlines = [StuentInfo]

    # 列表页属性
    list_display = ['pk', 'gname', 'gdate', 'ggirlnum', 'gboynum', 'isDelete']
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 5

    # 添加、修改页属性
    # fields = ['ggirlnum', 'gboynum', 'gname', 'gdate', 'isDelete']
    fieldsets = [
        ("num", {"fields":['ggirlnum', 'gboynum']}),
        ('base', {'fields':['gname', 'gdate', 'isDelete']})
    ]


# 注册

admin.site.register(Grades, GradesAdmin)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return '女'

     # 设置页码列的名称
    gender.short_description = "性别"

    list_display = ['pk', 'sname', 'sage', gender, 'scontend', 'sgrade', 'isDelete']
    list_per_page = 2

    # 执行动作位置
    actions_on_bottom = True
    actions_on_top = False


# admin.site.register(Student, StudentAdmin)

