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
    list_display = ('dakokuID',
                    'userID',
                    'dateTime',
                    'dakokuStatusID',
                    'dakokuMethodID',
                    'Bikou',
                    'sakujoFlag'
    )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# dakoku.py ends here
