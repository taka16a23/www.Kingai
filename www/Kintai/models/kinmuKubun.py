#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""kinmuKubun -- DESCRIPTION

"""
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class KinmuKubun(models.Model):
    """KinmuKubun

    KinmuKubun is a models.Model.
    Responsibility:
    """
    KinmuKubunID = models.AutoField(u'勤務区分ID', primary_key=True)
    KinmuKubunMei = models.CharField(u'区分名', max_length=50)
    KoushinUser = models.ForeignKey(User, verbose_name='更新ユーザー', null=True)
    KoushinJikan = models.DateTimeField(auto_now_add=True, null=True)

    def __unicode__(self):
        return unicode(self.KinmuKubunMei)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# kinmuKubun.py ends here
