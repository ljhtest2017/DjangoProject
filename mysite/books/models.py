from django.db import models


# Create your models here.
# 图书-作者-出版社
# 作者有名字、姓和邮件电子
# 出版社有名称、街道地址、所在城市、州（省）、国家和网站
# 书有书名和出版日期，还有一位或多位作者（与作者是多对多关系）,一个出版社（出版社（外键）与书是一对多关系）


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    website = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        # 指定排序
        ordering = ['name']

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True,  verbose_name='e-mail')

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
