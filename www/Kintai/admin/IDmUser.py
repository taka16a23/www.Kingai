#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""IDmUser -- DESCRIPTION

"""
from django.contrib import admin


class IDmUserAdmin(admin.ModelAdmin):
    """IDmUserAdmin

    IDmUserAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('IDm',
                    'user',
                    'bikou',
    )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# IDmUser.py ends here
