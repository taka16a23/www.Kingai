#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""userIDm -- DESCRIPTION

"""
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.db.models import Manager, Q


class ManagerAbstract(Manager):
    r"""ManagerAbstract

    ManagerAbstract is a models.Manager.
    Responsibility:
    """

    def __getattr__(self, name):
        return getattr(self.get_query_set(), name)


class IDmUserManager(ManagerAbstract):
    """IDmUserManager

    IDmUserManager is a ManagerAbstract.
    Responsibility:
    """
    def get_user_from_IDm(self, IDm):
        """SUMMARY

        get_user_from_IDm(IDm)

        @Arguments:
        - `IDm`:

        @Return:

        @Error:
        """
        # require

        # do

        # ensure

        return self.filter(Q(IDm=IDm))


    def list_IDm_from_user(self, user):
        """SUMMARY

        list_IDm_from_user(user)

        @Arguments:
        - `user`:

        @Return:

        @Error:
        """
        # require

        # do

        # ensure

        return self.filter(Q(user=user))


class IDmUser(models.Model):
    """IDmUser

    IDmUser is a models.Model.
    Responsibility:

    IDm: IDmは、FeliCaカード製造時にＩＣチップに記録され書き換えができない固有のＩＤ番号である。
         IDmは8byte（16桁）の数字
    userID: ユーザーID 固有のID
    bikou: 備考
    """
    # objects = IDmUserManager()

    # Felica IDm
    IDm = models.CharField(
        verbose_name=u'IDm',
        primary_key=True,
        max_length=16,
        help_text=u'IDmは、FeliCaカード製造時にＩＣチップに記録され書き換えができない固有のＩＤ番号である。IDmは8byte（16桁）の数字')

    # User 外部キー
    user = models.OneToOneField(
        verbose_name=u'ユーザーID',
        to=User,
        null=False,
        help_text=u'UserID')

    # 備考
    bikou = models.TextField(
        verbose_name=u'備考',
        primary_key=False,
        unique=False,
        blank=True,
        null=False,
        default='',
        max_length=2000,
        help_text=u'IDm × UserID に関する備考')



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# userIDm.py ends here
