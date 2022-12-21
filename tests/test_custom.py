# pylint: skip-file

import unittest
from testing_imports import *
from HTMLTestRunner import HTMLTestRunner


class CustomTestsEx2(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.data = join_datasets_year("data", [2016])

    def test_custom_ex2_multiple_cols(self):
        # Check if short name and potential are correct
        filtered_df = find_max_col(self.data, "potential", ["short_name", "potential"])
        expected = pd.DataFrame({"short_name": ['L. Messi'],
                                 "potential": [95]})
        # Comparing dataframes is a bit complex, you can use this if you are sure that there are no NaNs
        self.assertTrue(
            (filtered_df.reset_index(drop=True) == expected.reset_index(drop=True)).all().all())

    def test_custom_ex2_multiple_rows(self):
        # Check if potential is correct
        filtered_df = find_max_col(self.data, "age", ["short_name", "age"])
        expected = pd.DataFrame({"short_name": ['Kim Byung Ji', 'B. Richardson'],
                                 "age": [45, 45]})
        # Comparing dataframes is a bit complex, you can use this if you are sure that there are no NaNs
        self.assertTrue(
            (filtered_df.reset_index(drop=True) == expected.reset_index(drop=True)).all().all())


class CustomTestsEx3(unittest.TestCase):

    @classmethod
    def setUp(cls):
        # Create some fake data
        cls.data = pd.DataFrame({"short_name": ["L. Messi", "A. Putellas", "A. Hegerberg"],
                                 "gender": ["M", "F", "F"],
                                 "year": [2021, 2021, 2022],
                                 "height_cm": [169, 171, 177],
                                 "weight_kg": [67, 66, 70]})

    def test_custom_ex3a_femeni(self):
        male_bmi = calculate_bmi(self.data, "F", 2021, ["short_name"])
        self.assertEqual(male_bmi["short_name"].iloc[0], "A. Putellas")
        self.assertEqual(male_bmi["BMI"].iloc[0], 66 / (1.71 * 1.71))


class CustomTestsEx4(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.data = join_datasets_year("data", [2016, 2017, 2018])

    def test_custom_ex4b_one(self):
        ids = [176580, 168542]
        columns_of_interest = ["short_name", "overall", "player_positions"]
        data_dict = players_dict(self.data, ids, columns_of_interest)
        data_dict = clean_up_players_dict(data_dict, [('short_name', 'one'),
                                                      ("player_positions", "del_rep")])

        # Check if name is only one:
        self.assertCountEqual(data_dict[176580]["short_name"], 'L. Suárez')
        self.assertCountEqual(data_dict[168542]["short_name"], 'David Silva')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(CustomTestsEx2))
    suite.addTest(unittest.makeSuite(CustomTestsEx3))
    suite.addTest(unittest.makeSuite(CustomTestsEx4))
    runner = HTMLTestRunner(log=True, verbosity=2, output='reports',
                            title='PAC4', description='PAC4 custom tests',
                            report_name='Custom tests')
    runner.run(suite)


