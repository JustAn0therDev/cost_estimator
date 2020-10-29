import unittest
from cost_estimator import CostEstimator

cost_estimator = CostEstimator()


class CostEstimatorMonolithicTest(unittest.TestCase):

    test_hours = 8
    test_estimated_salary = 3400
    test_only_weekends = 's'
    test_months = 2
    test_days_per_week = 2
    test_weekends_too = 'n'
    test_expected_final_cost = 7300

    def test_cost_estimator(self):
        cost_estimator.set_hours(self.test_hours)
        self.assertTrue(self.test_hours == cost_estimator.hours)

        cost_estimator.set_estimated_salary(self.test_estimated_salary)
        self.assertTrue(self.test_estimated_salary == cost_estimator.estimated_salary)

        cost_estimator.set_only_weekends(self.test_only_weekends)
        self.assertTrue(cost_estimator.only_weekends)

        cost_estimator.set_days_per_week(self.test_weekends_too)
        self.assertTrue(self.test_days_per_week == cost_estimator.days_per_week)

        cost_estimator.set_months(self.test_months)
        self.assertTrue(cost_estimator.months == self.test_months)

        cost_estimator.calculate_final_costs()
        self.assertTrue(cost_estimator.cost_per_hour)
        self.assertTrue(cost_estimator.cost_per_hour != 0)
        self.assertTrue(cost_estimator.final_cost > self.test_expected_final_cost)


if __name__ == '__main__':
    unittest.main()
