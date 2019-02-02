#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""dakokuView -- DESCRIPTION

"""
from django.http import HttpResponse, HttpResponseBadRequest
from django.views import View
from Kintai import models
from Kintai.repository import IDmUserRepository


class DakokuView(View):
    """DakokuView

    DakokuView is a View.
    Responsibility:
    """
    GET_PARAM_IDM = 'idm'

    def get(self, request, *args, **kwargs):
        # dakoku = models.Dakoku()
        # dakoku.userID = request.user
        # dakoku.dakokuStatusID = models.DakokuStatus.objects.get(statusID=1)
        # dakoku.dakokuMethodID = models.DakokuMethod.objects.get(dakokuMethodID=1)
        # dakoku.save()

        # リクエストパラメターチェック
        idm = request.GET.get(self.GET_PARAM_IDM)
        dakokuKubun = models.DakokuKubun.objects.get(statusMei="通常出勤")
        dakokuMethod = models.DakokuMethod.objects.get(
            dakouMethodMei="IC", sakujoFlag=False)
        # idm to User チェック
        idmUser = IDmUserRepository().IDmToUser(idm)
        if idmUser != None:
            dakoku = models.Dakoku(userID=idmUser.user, dakokuStatusID=dakokuKubun, dakokuMethodID=dakokuMethod)
            dakoku.save()
            print(idmUser.user)

        return HttpResponse('hello')

    def post(self, request, *args, **kwargs):
        print('\n\npost')
        return HttpResponse('hello')



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# dakokuView.py ends here
