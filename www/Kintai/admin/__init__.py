#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
from django.contrib import admin

from .. import models

from dakokuKubun import DakokuKubunAdmin
from dakokuMethod import DakokuMethodAdmin
from kinmuKubun import KinmuKubunAdmin
from dakoku import DakokuAdmin
from IDmUser import IDmUserAdmin


__all__ = [
    'DakokuKubunAdmin',
    'DakokuMethodAdmin',
    'KinmuKubunAdmin',
    'DakokuAdmin',
    'IDmUserAdmin',
]

admin.site.register(models.DakokuKubun, DakokuKubunAdmin)
admin.site.register(models.DakokuMethod, DakokuMethodAdmin)
admin.site.register(models.KinmuKubun, KinmuKubunAdmin)
admin.site.register(models.Dakoku, DakokuAdmin)
admin.site.register(models.IDmUser, IDmUserAdmin)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
