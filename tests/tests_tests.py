#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Tests for the tests package."""
#
# (C) Pywikibot team, 2014-2019
#
# Distributed under the terms of the MIT license.
from __future__ import absolute_import, division, unicode_literals

import pywikibot

from tests.aspects import unittest, TestCase
from tests.utils import allowed_failure


class HttpServerProblemTestCase(TestCase):

    """Test HTTP status 502 causes this test class to be skipped."""

    sites = {
        '502': {
            'hostname': 'http://httpbin.org/status/502',
        }
    }

    def test_502(self):
        """Test a HTTP 502 response using http://httpbin.org/status/502."""
        self.fail('The test framework should skip this test.')
        pass


class TestPageAssert(TestCase):

    """Test page assertion methods."""

    family = 'wikipedia'
    code = 'en'

    dry = True

    @allowed_failure
    def test_assertPageTitlesEqual(self):
        """Test assertPageTitlesEqual shows the second page title and '...'."""
        pages = [pywikibot.Page(self.site, 'Foo'),
                 pywikibot.Page(self.site, 'Bar'),
                 pywikibot.Page(self.site, 'Baz')]
        self.assertPageTitlesEqual(pages, ['Foo'], self.site)


class TestLengthAssert(TestCase):

    """Test length assertion methods."""

    net = False

    seq1 = ('foo', 'bar', 'baz')
    seq2 = 'foo'

    def test_assert_is_emtpy(self):
        """Test assertIsEmpty method."""
        self.assertIsEmpty([])
        self.assertIsEmpty('')

    @unittest.expectedFailure
    def test_assert_is_emtpy_fail(self):
        """Test assertIsEmpty method failing."""
        self.assertIsEmpty(self.seq1)
        self.assertIsEmpty(self.seq2)

    def test_assert_is_not_emtpy(self):
        """Test assertIsNotEmpty method."""
        self.assertIsNotEmpty(self.seq1)
        self.assertIsNotEmpty(self.seq2)

    @unittest.expectedFailure
    def test_assert_is_not_emtpy_fail(self):
        """Test assertIsNotEmpty method."""
        self.assertIsNotEmpty([])
        self.assertIsNotEmpty('')

    def test_assert_length(self):
        """Test assertIsNotEmpty method."""
        self.assertLength([], 0)
        self.assertLength(self.seq1, 3)
        self.assertLength(self.seq1, self.seq2)

    @unittest.expectedFailure
    def test_assert_length_fail(self):
        """Test assertIsNotEmpty method."""
        self.assertLength([], 1)
        self.assertLength(self.seq1, 0)
        self.assertLength(None, self.seq)


if __name__ == '__main__':  # pragma: no cover
    try:
        unittest.main()
    except SystemExit:
        pass
