#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""dakoku -- DESCRIPTION

"""
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.db.models import Manager, Q

import dakokuKubun
import dakokuMethod


class ManagerAbstract(Manager):
    r"""ManagerAbstract

    ManagerAbstract is a models.Manager.
    Responsibility:
    """
    def __getattr__(self, name):
        return getattr(self.get_query_set(), name)


class DakokuQuerySet(QuerySet):
    """DakokuQuerySet

    DakokuQuerySet is a QuerySet.
    Responsibility:
    """
    def last_dakoku_by_user(self, user_id):
        """SUMMARY

        last_dakoku_by_user(user_id)

        @Arguments:
        - `user_id`:

        @Return:

        @Error:
        """
        # require

        # do
        return self.filter(Q(userID=user_id))


class Dakoku(models.Model):
    """Dakoku

    Dakoku is a models.Model.
    Responsibility:
    """
    # 打刻ID
    dakokuID = models.AutoField(
        primary_key=True #主キー
    )

    # ユーザーID
    userID = models.ForeignKey(
        User,                       #外部キー
        verbose_name='ユーザー',      #ヘッダー名
        null=False)                 #Null許可

    # 打刻時間
    dateTime = models.DateTimeField(
        auto_now_add=True,          #自動日時追加
        null=False,                 #Null不許可
        verbose_name='打刻日時')      #ヘッダー名

    # 打刻区分
    dakokuStatusID = models.ForeignKey(
        dakokuKubun.DakokuKubun,   #外部キー
        verbose_name='打刻区分',     #ヘッダー名
        null=False)                 #Null不許可

    # 打刻方法
    dakokuMethodID = models.ForeignKey(
        dakokuMethod.DakokuMethod, #外部キー
        verbose_name='打刻方法',    #ヘッダー名
        null=True)                 #Null許可

    # 備考
    Bikou = models.TextField(
        u'備考',                    #ヘッダー名
        null=True,                 #Null許可
        blank=True)                #ブランク許可

    # 削除フラグ
    sakujoFlag = models.BooleanField(
        u'削除フラグ',               #ヘッダー名
        default=False,             #初期値
        null=False)                #Null不許可



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# dakoku.py ends here
