import unittest


class MyTestCase(unittest.TestCase):
    def test_args_appkey_not_provided(self):
        from TrelloLabelReader import parse_args
        self.assertTrue(not parse_args(0))

    def test_args_appkey_valid(self):
        from TrelloLabelReader import parse_args
        self.assertTrue(parse_args("bar1bar1bar1bar1bar1bar1bar1bar1"))

    def test_args_appkey_invalid(self):
        from TrelloLabelReader import parse_args
        self.assertFalse(parse_args("bar1"))

    def test_args_boardname_provided(self):
        from TrelloLabelReader import parse_args
        apikey="bar1bar1bar1bar1bar1bar1bar1bar1"
        self.assertTrue(parse_args(apikey,"foobar"))


if __name__ == '__main__':
    unittest.main()
