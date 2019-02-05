#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""dakokuView -- DESCRIPTION

"""
from django.http import HttpResponse, HttpResponseBadRequest
from django.views import View
from Kintai import models
from Kintai.repository import IDmUserRepository
from Kintai.service.dakoku_data import DakokuData
from Kintai.service.normal_dakoku_service import NormalDakokuService


class DakokuView(View):
    """DakokuView

    DakokuView is a View.
    Responsibility:
    """
    GET_PARAM_IDM = 'idm'

    def get(self, request, *args, **kwargs):
        """
        """
        # リクエストパラメターチェック
        idm = request.GET.get(self.GET_PARAM_IDM)
        service = NormalDakokuService()
        data = DakokuData(idm)
        service.dakoku(data)
        if data.get_status() == data.SUCCESS:
            return HttpResponse('hello')
        return HttpResponse('failed')

    def post(self, request, *args, **kwargs):
        print('\n\npost')
        return HttpResponse('hello')



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# dakokuView.py ends here
