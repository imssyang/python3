import unittest

from pattern.structural.decorator import BoldWrapper, ItalicWrapper, TextTag


class TestTextWrapping(unittest.TestCase):
    def setUp(self):
        self.raw_string = TextTag("raw but not cruel")

    def test_italic(self):
        self.assertEqual(
            ItalicWrapper(self.raw_string).render(), "<i>raw but not cruel</i>"
        )

    def test_bold(self):
        self.assertEqual(
            BoldWrapper(self.raw_string).render(), "<b>raw but not cruel</b>"
        )

    def test_mixed_bold_and_italic(self):
        self.assertEqual(
            BoldWrapper(ItalicWrapper(self.raw_string)).render(),
            "<b><i>raw but not cruel</i></b>",
        )
