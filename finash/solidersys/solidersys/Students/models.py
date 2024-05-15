from django.db import models


class User(models.Model):
    student_id = models.CharField(max_length=10)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.student_id

class BasicInfo(models.Model):
    name = models.CharField(max_length=20,
                            default='',
                            verbose_name="姓名",
                            null=False)
    gender = models.CharField(max_length=20,
                              default='',
                              verbose_name="性别",
                              null=False)
    nation = models.CharField(max_length=20,
                              default='',
                              verbose_name="民族",
                              null=False, )
    birthday = models.DateField(max_length=20,
                                default='',
                                verbose_name="出生日期",
                                null=False)
    politic = models.CharField(max_length=20,
                               default='',
                               verbose_name="政治面貌",
                               null=False)
    Sno = models.CharField(max_length=100,
                           default='',
                           verbose_name="学号",
                           null=False)
    domicile = models.CharField(max_length=200,
                                default='',
                                verbose_name="户籍地",
                                null=False)
    ID_card = models.CharField(max_length=200,
                               default='',
                               verbose_name="身份证号",
                               null=False)
    enlist_time = models.DateField(max_length=20,
                                   default='',
                                   verbose_name="入伍时间",
                                   null=False)
    retire_time = models.DateField(max_length=20,
                                   default='',
                                   verbose_name="退役时间",
                                   null=False)
    before_teacher = models.CharField(max_length=20,
                                      default='',
                                      verbose_name="入伍前班导师",
                                      null=False)
    retire_teacher = models.CharField(max_length=20,
                                      default='',
                                      verbose_name="退伍后班导师",
                                      null=False)
    before_class = models.CharField(max_length=20,
                                    default='',
                                    verbose_name="入伍前学院班级",
                                    null=False)
    retire_class = models.CharField(max_length=20,
                                    default='',
                                    verbose_name="退伍后学院班级",
                                    null=False)
    searvice_troops = models.CharField(max_length=20,
                                       default='',
                                       verbose_name="服役部队",
                                       null=False)
    duties = models.CharField(max_length=20,
                              default='',
                              verbose_name="职务",
                              null=False)
    number = models.CharField(max_length=20,
                              default='',
                              verbose_name="本人电话",
                              null=False)
    family_number = models.CharField(max_length=20,
                                     default='',
                                     verbose_name="家庭电话",
                                     null=False)
    enlist_place = models.CharField(max_length=20,
                                    default='',
                                    verbose_name="入伍地",
                                    null=False)
    pend = models.CharField(max_length=20,
                            default='',
                            verbose_name="挂科科目",
                            null=True)
    rewards = models.CharField(max_length=20,
                               default='',
                               verbose_name="奖惩情况",
                               null=True)
    certifiate = models.CharField(max_length=200,
                                  default='',
                                  verbose_name="专业培训及证书",
                                  null=True)
    personal_photo = models.CharField(max_length=200,
                                      verbose_name="个人照",
                                      null=False)
    enlist_photo = models.CharField(max_length=200,
                                    verbose_name="入伍通知书",
                                    null=False)
    retire_photo = models.CharField(max_length=200,
                                    verbose_name="退役证",
                                    null=False)
    sign_photo = models.CharField(max_length=200,
                                  verbose_name="本人签字",
                                  null=False)
    isValid = models.BooleanField(default=1,
                                  verbose_name="是否有效")

    class Meta:
        verbose_name = '基本信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



