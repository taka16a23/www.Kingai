#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""dakoku -- DESCRIPTION

"""
from django.contrib import admin


class DakokuAdmin(admin.ModelAdmin):
    """DakokuAdmin

    DakokuAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    TIME_FORMAT = "%y年%m月%d日 %H時%M分%S秒"

    list_display = ('dakokuID',
                    'userID',
                    'format_dateTime', # dateTime
                    'dakokuStatusID',
                    'dakokuMethodID',
                    'Bikou',
                    'sakujoFlag'
    )

    def format_dateTime(self, obj):
        """SUMMARY

        format_dateTime(obj)

        @Arguments:
        - `obj`:

        @Return:

        @Error:
        """
        # require

        # do
        return obj.dateTime.strftime(self.TIME_FORMAT)
        # ensure

    format_dateTime.admin_order_field = "dateTime"
    format_dateTime.short_description = "打刻日時"



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# dakoku.py ends here
