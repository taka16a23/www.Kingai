#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""normal_dakoku_service -- DESCRIPTION

"""
from Kintai.service.base_dakoku_service import BaseDakokuService
from Kintai.models import DakokuKubun, DakokuMethod, Dakoku
from Kintai.repository import IDmUserRepository


class NormalDakokuService(BaseDakokuService):
    """NormalDakokuService

    NormalDakokuService is a BaseDakokuService.
    Responsibility:
    """
    def __init__(self, ):
        """
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
        dakokuKubun = DakokuKubun.objects.get(statusMei="通常出勤")
        dakokuMethod = DakokuMethod.objects.get(
            dakouMethodMei="IC", sakujoFlag=False)
        idmUser = IDmUserRepository().IDmToUser(idm)
        # do
        if idmUser != None:
            dakoku = Dakoku(
                userID=idmUser.user, dakokuStatusID=dakokuKubun,
                dakokuMethodID=dakokuMethod)
            dakoku.save()
            print(idmUser.user)
            data.set_status(data.SUCCESS)
            return
        data.set_status(data.FAILED)
        # ensure



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# normal_dakoku_service.py ends here
