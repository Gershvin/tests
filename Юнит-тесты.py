import unittest
from SearchBrackets import regular
from SearchBrackets import unregular
from Korteges import func_1
from Korteges import func_2

class Brackets_Test(unittest.TestCase):
    """Тесты для 'name_function.py'."""

    def test_regular(self):
        """Удаляется ли текст в скобках с помощью регулярных выражений?"""
        result = regular("asdflj (kla (inner) asd) port (another ))(unclosed")
        self.assertEqual(result, "asdflj  asd) port )(unclosed")
    def test_unregular(self):
        """Удаляется ли текст в скобках без использования регулярных выражений?"""
        test = unregular("asdflj (kla (inner) asd) port (another ))(unclosed")
        self.assertEqual(test, "asdflj ) port )(unclosed")
    def test_func_1(self):
        """Корректно ли работает функция func_1"""
        pows = func_1("asdflj (kla (inner) asd) port (another ))(unclosed")
        self.assertEqual(pows, "asdflj  asd) port )(unclosed")
    def test_func_2(self):
        """Корректно ли работает функция func_2"""
        del_repeat = func_2("asdflj (kla (inner) asd) port (another ))(unclosed")
        self.assertEqual(del_repeat, "asdflj  asd) port )(unclosed")
unittest.main()

