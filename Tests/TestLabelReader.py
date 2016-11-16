import unittest
from TrelloLabelReader import comparator
from TrelloLabelReader import parse_args


class AppArgs(unittest.TestCase):
    def test_args_appkey_not_provided(self):
        self.assertTrue(not parse_args(0))

    def test_args_appkey_valid(self):
        self.assertTrue(parse_args("bar1bar1bar1bar1bar1bar1bar1bar1"))

    def test_args_appkey_invalid(self):
        self.assertFalse(parse_args("bar1"))

    def test_args_boardname_provided(self):
        apikey = "bar1bar1bar1bar1bar1bar1bar1bar1"
        self.assertTrue(parse_args(apikey, "foobar"))


class TestComparator(unittest.TestCase):
    def test_label_matched(self):
        Bugcomparator="Bugs"
        self.assertEquals(Bugcomparator, comparator("bug"))
        self.assertEquals(Bugcomparator, comparator("bugs"))
        self.assertEquals(Bugcomparator, comparator("bog"))
        self.assertEquals(Bugcomparator, comparator("bogue"))
        self.assertEquals(Bugcomparator, comparator("Bugs"))
        self.assertEquals(Bugcomparator, comparator("Bug"))

        ReleaseComparator="Release"
        self.assertEquals(ReleaseComparator, comparator("release"))
        self.assertEquals(ReleaseComparator, comparator("Release"))
        self.assertEquals(ReleaseComparator, comparator("realese"))
        self.assertEquals(ReleaseComparator, comparator("Realease"))

        ProductLaunchComparator="Product launch"
        self.assertEquals(ProductLaunchComparator, comparator("Product Launch"))
        self.assertEquals(ProductLaunchComparator, comparator("Launch product"))
        self.assertEquals(ProductLaunchComparator, comparator("Product launch"))
        self.assertEquals(ProductLaunchComparator, comparator("Launch Product"))
        self.assertEquals(ProductLaunchComparator, comparator("Product-Launch"))


if __name__ == '__main__':
    unittest.main()
