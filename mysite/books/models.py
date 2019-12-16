from django.db import models


# Create your models here.
# ͼ��-����-������
# ���������֡��պ��ʼ�����
# �����������ơ��ֵ���ַ�����ڳ��С��ݣ�ʡ�������Һ���վ
# ���������ͳ������ڣ�����һλ���λ���ߣ��������Ƕ�Զ��ϵ��,һ�������磨�����磨�����������һ�Զ��ϵ��


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
        # ָ������
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
