#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""dakoku_data -- DESCRIPTION

"""

class DakokuData(object):
    """DakokuData

    DakokuData is a object.
    Responsibility:
    """
    FAILED = 0
    SUCCESS = 1

    def __init__(self, idm):
        """

        @Arguments:
        - `idm`:
        """
        self._idm = idm
        self.status = DakokuData.FAILED

    def get_idm(self, ):
        """SUMMARY

        get_idm()

        @Return:

        @Error:
        """
        # require

        # do

        # ensure

        return self._idm

    def get_status(self, ):
        """SUMMARY

        get_status()

        @Return:

        @Error:
        """
        # require
        # do
        self.status = DakokuData.SUCCESS

        # ensure

    def set_status(self, status):
        """SUMMARY

        set_status(status)

        @Arguments:
        - `status`:

        @Return:

        @Error:
        """
        # require

        # do
        self.status = status
        # ensure



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# dakoku_data.py ends here
