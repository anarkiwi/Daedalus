# -*- coding: utf-8 -*-
"""
Test module for daedalus.
@author: Charlie Lewis
"""
from daedalus.daedalus import Daedalus


def test_start_remove_dovesnap():
    instance = Daedalus()
    instancce.set_config_dir()
    instance.start_dovesnap()
    instance.remove_dovesnap()
    instancce.reset_cwd()
