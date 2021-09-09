from django.test import TestCase

from indian_numbers.templatetags.indian_numbers_tags import *


class TestIntCommaIndian(TestCase):

    def test1(self):
        arg = 0
        expect = '0'
        result = intcomma_indian(arg)
        self.assertEqual(expect, result)

    def test2(self):
        arg = 0.00
        expect = '0'
        result = intcomma_indian(arg)
        self.assertEqual(expect, result)

    def test3(self):
        arg = 1
        expect = '1'
        result = intcomma_indian(arg)
        self.assertEqual(expect, result)

    def test4(self):
        arg = 26500
        expect = '26,500'
        result = intcomma_indian(arg)
        self.assertEqual(expect, result)

    def test5(self):
        arg = 126500
        expect = '1,26,500'
        result = intcomma_indian(arg)
        self.assertEqual(expect, result)

    def test6(self):
        arg = 1259647552
        expect = '1,25,96,47,552'
        result = intcomma_indian(arg)
        self.assertEqual(expect, result)

    def test7(self):
        arg = 1259647552.25
        expect = '1,25,96,47,552'
        result = intcomma_indian(arg)
        self.assertEqual(expect, result)

    def test7_with_decimal_places_preserved(self):
        arg = 1259647552.25
        expect = '1,25,96,47,552.25'
        result = intcomma_indian(arg, preserve_decimal=True)
        self.assertEqual(expect, result)

    def test8(self):
        arg = -126500
        expect = '-1,26,500'
        result = intcomma_indian(arg)
        self.assertEqual(expect, result)

    def test9(self):
        arg = 126500.25
        expect = '1,26,500'
        result = intcomma_indian(arg)
        self.assertEqual(expect, result)

    def test10(self):
        arg = '126500.25'
        expect = '1,26,500'
        result = intcomma_indian(arg)
        self.assertEqual(expect, result)

    def test11(self):
        arg = 'abc'
        expect = 'abc'
        result = intcomma_indian(arg)
        self.assertEqual(expect, result)

    def test12(self):
        arg = '123456789abc'
        expect = '123456789abc'
        result = intcomma_indian(arg)
        self.assertEqual(expect, result)

    def test13(self):
        arg = 'abc123456789'
        expect = 'abc123456789'
        result = intcomma_indian(arg)
        self.assertEqual(expect, result)


class TestFloatCommaIndian(TestCase):

    def test1(self):
        arg = 25
        expect = '25'
        result = floatcomma_indian(arg)
        self.assertEqual(expect, result)

    def test2(self):
        arg = 121250.6
        expect = '1,21,250.6'
        result = floatcomma_indian(arg)
        self.assertEqual(expect, result)

    def test3(self):
        arg = 121250.25
        expect = '1,21,250.25'
        result = floatcomma_indian(arg)
        self.assertEqual(expect, result)

    def test4(self):
        arg = 121250.675
        expect = '1,21,250.675'
        result = floatcomma_indian(arg)
        self.assertEqual(expect, result)

    def test5(self):
        arg = -121250.675
        expect = '-1,21,250.675'
        result = floatcomma_indian(arg)
        self.assertEqual(expect, result)

    def test5_with_2_decimal_positions(self):
        arg = -121250.675
        expect = '-1,21,250.67'
        result = floatcomma_indian(arg, decimal_pos=2)
        self.assertEqual(expect, result)

    def test6(self):
        arg = 12345678
        expect = '1,23,45,678'
        result = floatcomma_indian(arg)
        self.assertEqual(expect, result)

    def test6_with_2_decimal_positions(self):
        arg = 12345678
        expect = '1,23,45,678.00'
        result = floatcomma_indian(arg, decimal_pos=2)
        self.assertEqual(expect, result)

    def test7(self):
        arg = 'abc'
        expect = 'abc'
        result = floatcomma_indian(arg)
        self.assertEqual(expect, result)

    def test8(self):
        arg = '123456.45ab'
        expect = '123456.45ab'
        result = floatcomma_indian(arg)
        self.assertEqual(expect, result)

    def test9(self):
        arg = '6.02E2'
        expect = '602.0'
        result = floatcomma_indian(arg)
        self.assertEqual(expect, result)

    def test9_with_zero_decimal_places(self):
        arg = '6.02E2'
        expect = '602'
        result = floatcomma_indian(arg, decimal_pos=0)
        self.assertEqual(expect, result)

    def test9_with_3_decimal_places(self):
        arg = '6.02E2'
        expect = '602.000'
        result = floatcomma_indian(arg, decimal_pos=3)
        self.assertEqual(expect, result)


class TestFloatWordIndian(TestCase):

    def do_assertion(self, arg, expect):
        result = floatword_indian(arg)
        self.assertEqual(expect, result)

    def test1(self):
        arg = 0.00
        expect = '0.0'
        self.do_assertion(arg, expect)

    def test2(self):
        arg = '0'
        expect = '0'
        self.do_assertion(arg, expect)

    def test3(self):
        arg = '0.00'
        expect = '0.00'
        self.do_assertion(arg, expect)

    def test4(self):
        arg = '12'
        expect = '12'
        self.do_assertion(arg, expect)

    def test5(self):
        arg = '12.56'
        expect = '12.56'
        self.do_assertion(arg, expect)

    def test6(self):
        arg = '120'
        expect = '1.20 Hundreds'
        self.do_assertion(arg, expect)

    def test7(self):
        arg = 100
        expect = '1 Hundred'
        self.do_assertion(arg, expect)

    def test8(self):
        arg = 900
        expect = '9 Hundreds'
        self.do_assertion(arg, expect)

    def test9(self):
        arg = '1000'
        expect = '1 Thousand'
        self.do_assertion(arg, expect)

    def test10(self):
        arg = '19000'
        expect = '19 Thousands'
        self.do_assertion(arg, expect)

    def test11(self):
        arg = '19050'
        expect = '19.05 Thousands'
        self.do_assertion(arg, expect)

    def test12(self):
        arg = 100000
        expect = '1 Lakh'
        self.do_assertion(arg, expect)

    def test13(self):
        arg = 100325
        expect = '1 Lakh'
        self.do_assertion(arg, expect)

    def test14(self):
        arg = 1125000
        expect = '11.25 Lakhs'
        self.do_assertion(arg, expect)

    def test15(self):
        arg = 500000
        expect = '5 Lakhs'
        self.do_assertion(arg, expect)

    def test16(self):
        arg = 1125000
        expect = '11.25 Lakhs'
        self.do_assertion(arg, expect)

    def test17(self):
        arg = 10000000
        expect = '1 Crore'
        self.do_assertion(arg, expect)

    def test18(self):
        arg = 50000000
        expect = '5 Crores'
        self.do_assertion(arg, expect)

    def test19(self):
        arg = 56482485.25
        expect = '5.64 Crores'
        self.do_assertion(arg, expect)

    def test20(self):
        arg = 'abc.def'
        expect = 'abc.def'
        self.do_assertion(arg, expect)

    def test21(self):
        arg = 'abc'
        expect = 'abc'
        self.do_assertion(arg, expect)

    def test22(self):
        arg = 12
        expect = '12'
        self.do_assertion(arg, expect)
