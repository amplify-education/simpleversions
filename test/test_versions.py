# This file is part of simpleversions
#
#Copyright (c) 2012 Wireless Generation, Inc.
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

from simpleversions import Version
from nose.tools import assert_true

def test_versions():
    assert_true(Version('12.1.0') > Version('12.0.0'))
    assert_true(Version('12.1.0') > Version('12.0'))
    assert_true(Version('12.0.0') == Version('12.0'))
    assert_true(Version('12.0.0') == Version('12'))
    assert_true(Version('12.1.0') > Version('12'))
    assert_true(Version('12.0.0') == Version('12'))
    assert_true(Version('01.0.0') < Version('12'))
    assert_true(Version('12.1.x') == Version('12.1.0'))
    assert_true(Version('') < Version('12.1.0'))
    assert_true(Version('development') < Version('12.1.0'))

    assert_true(Version('1') ==
                Version('1.0') ==
                Version('1.0.0') ==
                Version('1.0.0a') ==
                Version('1.0.0test'))

    assert_true(Version('1') <
                Version('2') <
                Version('2.1~a1') <
                Version('2.1') <
                Version('2.2'))

def test_revisions():
    assert_true(Version('12.0.0_rc2') < Version('12.0.0'))
    assert_true(Version('1') >
                Version('1~100') >
                Version('1~1'))

def test_nonnumerics():
    assert_true(Version('1.0') == Version('1,0'))
    assert_true(Version('1-0') == Version('1_0') == Version('1~0'))
    assert_true(Version('1') == Version('1a') == Version('1 '))
