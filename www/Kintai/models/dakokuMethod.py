#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""dakokuMethod -- DESCRIPTION

"""
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class DakokuMethod(models.Model):
    """DakokuMethod

    DakokuMethod is a models.Model.
    Responsibility:
    """
    # 打刻方法ID
    dakokuMethodID = models.AutoField(u'打刻方法ID', primary_key=True)

    # 打刻方法名
    dakouMethodMei = models.CharField(u'打刻方法名', max_length=50)

    # 削除フラグ
    sakujoFlag = models.BooleanField(u'削除フラグ', default=False)

    # 更新ユーザー
    KoushinUser = models.ForeignKey(User, verbose_name='更新ユーザー')

    # 更新時間
    KoushinJikan = models.DateTimeField(auto_now_add=True, verbose_name='更新時間')

    def __unicode__(self):
        return unicode(self.dakouMethodMei)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# dakokuMethod.py ends here
