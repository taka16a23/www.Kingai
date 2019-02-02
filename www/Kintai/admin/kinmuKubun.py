#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""kinmuKubun -- DESCRIPTION

"""
from django.contrib import admin
from django import forms
from ..models.kinmuKubun import KinmuKubun

class KinmuKubunForm(forms.ModelForm):
    """KinmuKubunForm

    KinmuKubunForm is a forms.ModelForm.
    Responsibility:
    """
    class Meta:
        """Meta

        Meta is a object.
        Responsibility:
        """
        model = KinmuKubun
        exclude = ['KoushinUser', ]



class KinmuKubunAdmin(admin.ModelAdmin):
    """KinmuKubunAdmin

    KinmuKubunAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    # exclude = ['KoushinUser', ]
    list_display = ('KinmuKubunMei', 'KoushinUser', 'KoushinJikan', )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# kinmuKubun.py ends here
