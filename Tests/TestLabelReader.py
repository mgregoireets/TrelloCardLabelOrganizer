import unittest
from TrelloLabelReader import initialise_dictionary
from TrelloLabelReader import parse_args
from TrelloLabelReader import dictionary
from TrelloLabelReader import fixedCardLabels
from TrelloLabelReader import process_duplicates
import TrelloLabelReader


class AppArgs(unittest.TestCase):
    def test_args_appkey_not_provided(self):
        self.assertTrue(not parse_args(0, 0))

    def test_args_username_not_provided(self):
        apikey = "bar1bar1bar1bar1bar1bar1bar1bar1"
        self.assertFalse(parse_args(apikey, 0))

    def test_args_appkey_valid(self):
        apikey = "bar1bar1bar1bar1bar1bar1bar1bar1"
        username = "foo"
        self.assertTrue(parse_args(apikey, username))

    def test_args_appkey_invalid(self):
        self.assertFalse(parse_args("bar1", "foobar"))


class TestDictionary(unittest.TestCase):
    def test_dictionary_init(self):
        initialise_dictionary()
        self.assertEquals(dictionary, set(fixedCardLabels.keys()))

    def test_process_duplicates(self):
        list = ["bug", "bugs", "bog", "Release", "realese", "Realease", "Product Launch", "Launch product",
                "Product-Launch"]
        duplicates = process_duplicates(list)
        duplicatesName = []
        for dup in duplicates:
            duplicatesName.append(dup[0])
        self.assertEquals(["bug", "Release", "Product Launch"], duplicatesName)


if __name__ == '__main__':
    unittest.main()
