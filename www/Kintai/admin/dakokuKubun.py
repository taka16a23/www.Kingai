#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""dakokuKubun -- DESCRIPTION

"""
from django.contrib import admin


class DakokuKubunAdmin(admin.ModelAdmin):
    """DakokuKubunAdmin

    DakokuKubunAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('statusMei', 'KoushinUser', 'KoushinJikan', )
    ordering = ('KubunID', )

    fieldsets = [(None, {'fields': [('statusMei', )]}), ]

    def save_model_(self, request, obj, form, change):
        """更新ユーザーを自動更新

        save_model_(request, obj, form, change)

        @Arguments:
        - `request`:
        - `obj`:
        - `form`:
        - `change`:

        @Return: None

        @Error:
        """
        print('DEBUG-2-dakokuKubun.py')
        # obj.KoushinUser = request.user
        print('DEBUG-1-dakokuKubun.py')
        print(request.user)
        obj.save()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# dakokuKubun.py ends here
