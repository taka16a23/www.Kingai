#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""dakoku_repository -- DESCRIPTION

"""
from Kintai.models import Dakoku
from Kintai.models import DakokuKubun

class DakokuRepository(object):
    """DakokuRepository

    DakokuRepository is a object.
    Responsibility:
    """
    def get_last_dakoku(self, user):
        """SUMMARY

        get_last_dakoku(user)

        @Arguments:
        - `user`:

        @Return:

        @Error:
        """
        dakokus = Dakoku.objects.filter(userID=user).latest('dakokuID')
        if dakokus is None:
            return None
        return dakokus

    def get_dakoku_kubun(self, user):
        """SUMMARY

        get_dakoku_kubun(idm)

        @Arguments:
        - `idm`:

        @Return:

        @Error:
        """
        # require
        last_dakoku = self.get_last_dakoku(user)
        if last_dakoku is None:
            return None
        return last_dakoku.dakokuStatusID

    def get_next_dakoku_kubun(self, user):
        """SUMMARY

        get_next_dakokuKubun()

        @Return:

        @Error:
        """
        # require

        # do
        dakokukubun = self.get_dakoku_kubun(user)
        normal_dakoku_kubun = DakokuKubun.objects.get(statusMei="通常出勤")

        # ensure
        if dakokukubun == normal_dakoku_kubun:
            return DakokuKubun.objects.get(statusMei="通常退勤")
        return normal_dakoku_kubun



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# dakoku_repository.py ends here
