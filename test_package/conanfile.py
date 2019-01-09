#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from conans import ConanFile
import os


class TestPackageConan(ConanFile):    
    def test(self):
        testdir = os.path.dirname(os.path.realpath(__file__))
        self.run("swig -python -outcurrentdir %s"%os.path.join(testdir, "test.i"))
        assert "example.py" in os.listdir(testdir)
