#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""normal_dakoku_service -- DESCRIPTION

"""
from Kintai.service.base_dakoku_service import BaseDakokuService
from Kintai.models import DakokuMethod, Dakoku
from Kintai.repository import IDmUserRepository
from Kintai.repository.dakoku_repository import DakokuRepository


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
        print(idm)
        # do
        idm_user = IDmUserRepository().IDmToUser(idm)
        if idm_user is None:
            data.set_status(data.FAILED)
            data.set_message("failed user")
            return

        dakoku_repository = DakokuRepository()
        dakoku_kubun = dakoku_repository.get_next_dakoku_kubun(idm_user.user)
        if dakoku_kubun == None:
            print('error')
            data.set_status(data.FAILED)
            data.set_message(unicode(dakoku_kubun.statusMei))
            return
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
        # ensure



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# normal_dakoku_service.py ends here
