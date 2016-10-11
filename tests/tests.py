from django.test import TestCase

from indian_numbers.templatetags.indian_numbers_tags import *


class DoAssertionIntCommaMixin(object):

    def do_assertion(self, arg, expect):
        result = intcomma_indian(arg)
        self.assertEqual(expect, result)


class TestIntCommaIndian(TestCase, DoAssertionIntCommaMixin):

    def test1(self):
        arg = 0
        expect = '0'
        self.do_assertion(arg, expect)

    def test2(self):
        arg = 0.00
        expect = '0'
        self.do_assertion(arg, expect)

    def test3(self):
        arg = 1
        expect = '1'
        self.do_assertion(arg, expect)

    def test4(self):
        arg = 26500
        expect = '26,500'
        self.do_assertion(arg, expect)

    def test5(self):
        arg = 126500
        expect = '1,26,500'
        self.do_assertion(arg, expect)

    def test6(self):
        arg = 1259647552
        expect = '1,25,96,47,552'
        self.do_assertion(arg, expect)

    def test7(self):
        arg = 1259647552.25
        expect = '1,25,96,47,552'
        self.do_assertion(arg, expect)

    def test8(self):
        arg = -126500
        expect = '-1,26,500'
        self.do_assertion(arg, expect)

    def test9(self):
        arg = 126500.25
        expect = '1,26,500'
        self.do_assertion(arg, expect)

    def test10(self):
        arg = '126500.25'
        expect = '1,26,500'
        self.do_assertion(arg, expect)


class DoAssertionFloatCommaMixin(object):

    def do_assertion(self, arg, expect):
        result = floatcomma_indian(arg)
        self.assertEqual(expect, result)


class TestFloatCommaIndian(TestCase, DoAssertionFloatCommaMixin):

    def test1(self):
        arg = 25
        expect = '25.00'
        self.do_assertion(arg, expect)

    def test2(self):
        arg = 121250.6
        expect = '1,21,250.6'
        self.do_assertion(arg, expect)

    def test3(self):
        arg = 121250.25
        expect = '1,21,250.25'
        self.do_assertion(arg, expect)

    def test4(self):
        arg = 121250.675
        expect = '1,21,250.675'
        self.do_assertion(arg, expect)

    def test5(self):
        arg = -121250.675
        expect = '-1,21,250.675'
        self.do_assertion(arg, expect)
