#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""IDmUserRepository -- DESCRIPTION

"""
from Kintai import models


class IDmUserRepository(object):
    """IDmUserRepository

    IDmUserRepository is a object.
    Responsibility:
    """

    def IDmToUser(self, IDm):
        """SUMMARY

        IDmToUser(IDm)

        @Arguments:
        - `IDm`:

        @Return: None or User Model.

        @Error:
        """
        return models.IDmUser.objects.filter(IDm=IDm).first()

    def list_IDm_from_user(self, user):
        """SUMMARY

        list_IDm_from_user(user)

        @Arguments:
        - `user`:

        @Return: list of IDm

        @Error:
        """
        return models.IDmUser.objects.list_IDm_from_user(user)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# IDmUserRepository.py ends here
