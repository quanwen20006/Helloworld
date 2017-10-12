# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    articletype = (('auto', '自动化测试'), ('safe', '安全测试'), ('per', '性能测试'), ('busi', '业务'))
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    atype = models.CharField(max_length=10, choices=articletype, default='auto')

    class Meta:
        ordering = ('pub_date',)

    def __unicode__(self):
        return self.title
