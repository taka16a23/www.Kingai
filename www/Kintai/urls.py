#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""urls -- DESCRIPTION

"""
from django.conf.urls import url
from views import DakokuView


urlpatterns = [
    url(r'^dakoku$', DakokuView.as_view()),
]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# urls.py ends here
