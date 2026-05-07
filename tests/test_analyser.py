import unittest
from analytics.analyser import CountryAnalyser
class TestAnalyser(unittest.TestCase):

    def setUp(self):

        self.sample = [
            {"country": "USA", "sleep_hours": "7"},
            {"country": "India", "sleep_hours": "5"},
            {"country": "USA", "sleep_hours": "8"},
            {"country": "Canada", "sleep_hours": "4"},
            {"country": "India", "sleep_hours": "6"},
        ]

    def test_result_is_not_empty(self):

        analyser = CountryAnalyser(self.sample)

        analyser.analyse()

        self.assertNotEqual(analyser.result, {})

    def test_total_students(self):

        analyser = CountryAnalyser(self.sample)

        analyser.analyse()

        self.assertEqual(
            analyser.result["total_students"],
            5
        )

    def test_result_has_required_keys(self):

        analyser = CountryAnalyser(self.sample)

        analyser.analyse()

        self.assertIn("total_countries", analyser.result)
        self.assertIn("top_3", analyser.result)
        self.assertIn("all_countries", analyser.result)

    def test_analyse_twice(self):

        analyser = CountryAnalyser(self.sample)

        analyser.analyse()

        result1 = analyser.result.copy()

        analyser.analyse()

        self.assertEqual(analyser.result, result1)


if __name__ == "__main__":
    unittest.main()