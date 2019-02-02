#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""dakokuMethod --

"""
from django.contrib import admin


class DakokuMethodAdmin(admin.ModelAdmin):
    """DakokuStatusAdmin

    DakokuStatusAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('dakouMethodMei', 'KoushinUser', 'sakujoFlag', 'KoushinJikan', )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# dakokuMethod.py ends here
