#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""normal_dakoku_service -- DESCRIPTION

"""
from collections import Iterable

from django.db.models import Q

from Kintai.service.base_dakoku_service import BaseDakokuService
from Kintai.models import DakokuMethod, Dakoku, DakokuKubun
from Kintai.repository import IDmUserRepository
from Kintai.repository.dakoku_repository import DakokuRepository


class DakokuAnalyzer(object):
    """DakokuAnalyzer

    DakokuAnalyzer is a object.
    Responsibility:
    """
    def __init__(self, user_id):
        """

        @Arguments:
        - `user_id`: User model instance
        """
        self._user_id = user_id
        shukkin_dakoku_kubun = DakokuKubun.objects.get(statusMei="通常出勤")
        taikin_dakoku_kubun = DakokuKubun.objects.get(statusMei="通常退勤")

        self._dakokus = list(
            Dakoku
            .objects
            .filter(userID=self._user_id)
            .filter(Q(dakokuStatusID=shukkin_dakoku_kubun)
                    | Q(dakokuStatusID=taikin_dakoku_kubun))
            .order_by('dateTime')
            .reverse()[:20])

    def get_last_dakoku(self, ):
        """Get last Dakoku present or out.

        get_last_dakoku()

        @Return:
        None if record not exists.
        Or Dakoku model.

        @Error:
        """
        if len(self._dakokus) <= 0:
            return None
        return self._dakokus[0]

    def is_last_shukkin(self, ):
        """Return True if last dakoku is 通常出勤 by user.

        is_last_shukkin()

        @Return: True if last dakoku is 通常出勤 by user. if not False

        @Error:
        """
        # require
        last_dakoku = self.get_last_dakoku()
        if last_dakoku is None:
            return False
        # do
        shukkin_dakoku_kubun = DakokuKubun.objects.get(statusMei="通常出勤")
        # ensure
        if last_dakoku.dakokuStatusID.KubunID == shukkin_dakoku_kubun.KubunID:
            return True
        return False


class NormalDakokuService(BaseDakokuService):
    """NormalDakokuService

    NormalDakokuService is a BaseDakokuService.
    Responsibility:
    """
    def dakoku(self, data):
        """SUMMARY

        dakoku(data)

        @Arguments:
        - `data`: DakokuData

        @Return:

        @Error:
        """
        # require
        idm = data.get_idm()
        # temporary
        print(idm)
        # do
        idm_user = IDmUserRepository().IDmToUser(idm)
        if idm_user is None:
            data.set_status(data.FAILED)
            data.set_message("failed user")
            return

        # punch out if last dakoku is present
        analyzer = DakokuAnalyzer(idm_user.user)
        dakoku_kubunmei = '通常出勤'
        if analyzer.is_last_shukkin():
            dakoku_kubunmei = '通常退勤'
        print(dakoku_kubunmei)
        dakoku_kubun = DakokuKubun.objects.get(statusMei=dakoku_kubunmei)
        #
        if dakoku_kubun is None:
            data.set_status(data.FAILED)
            data.set_message(unicode(dakoku_kubun.statusMei))
            return
        #
        dakoku_method = DakokuMethod.objects.get(
            dakouMethodMei="IC", sakujoFlag=False)
        dakoku = Dakoku(
            userID=idm_user.user,
            dakokuStatusID=dakoku_kubun,
            dakokuMethodID=dakoku_method)
        dakoku.save()
        print(idm_user.user)
        data.set_status(data.SUCCESS)
        data.set_message(unicode(dakoku_kubun.statusMei))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# normal_dakoku_service.py ends here
