#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""dakokuKubun -- DESCRIPTION

"""
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class DakokuKubun(models.Model):
    """DakokuKubun

    DakokuKubun is a models.Model.
    Responsibility:
    """
    KubunID = models.AutoField(u'ID', primary_key=True)
    statusMei = models.CharField(u'区分名', max_length=255)
    KoushinUser = models.ForeignKey(User, verbose_name='更新ユーザー', null=True)
    KoushinJikan = models.DateTimeField(auto_now_add=True, verbose_name='更新時間')

    def __unicode__(self):
        return unicode(self.statusMei)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# dakokuStatus.py ends here
