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

import re

def remove_alphas(version_string):
    """
    Returns `version_string` with all alpha characters removed (a-z, either caps)
    """
    return re.sub("[^0-9.,-_~]", "", version_string)

def version_as_list(version):
    """
    Returns a list of the integer components of the supplied version string.

    Components are separated by , or . characters
    """
    values = re.split("[.,]", version)
    return [int(v) if v != "" else 0
            for v in values]

def split_revisions(version_string):
    """
    Returns a list of revisions pulled from the version string.

    Revisions are separated by -, _, or ~
    """
    return re.split('[-_~]', version_string)


class Version(object):
    """
    Represents an simple version in a comparable fashion

    `version_string`:
        The version string to parse the version from
    """
    def __init__(self, version_string):
        self.revs = [
            version_as_list(version)
            for version
            in split_revisions(remove_alphas(version_string))
        ]

        self.version_string = version_string

    def __cmp__(self, other):
        def pad(data, length):
            """
            Extends `data` with enough 0's to bring it to `length` length
            """
            return data.extend([0]*(length-len(data)))

        self_revs = list(self.revs)
        other_revs = list(other.revs)

        # Loop through and compare subrevisions until one doesn't match,
        # or we run out
        while self_revs and other_revs:
            self_rev = self_revs.pop(0)
            other_rev = other_revs.pop(0)
            length = max(len(self_rev), len(other_rev))

            pad(self_rev, length)
            pad(other_rev, length)

            # If this revision matches, then continue to the next one
            if self_rev == other_rev:
                continue

            # otherwise, the versions compare as this revision compares
            return cmp(self_rev, other_rev)

        # If the two versions match in all corresponding revisions,
        # then the one with more revisions is less than the one with fewer
        # revisions
        return len(other_revs) - len(self_revs)

    def __str__(self):
        return self.version_string
    
    def __repr__(self):
        return 'Version({string})'.format(string=repr(self.version_string))
