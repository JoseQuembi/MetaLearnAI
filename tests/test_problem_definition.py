# MetaLearnAI test_problem_definition.py

import unittest
from metalearnai.problem_definition import LearningProblem

class TestLearningProblem(unittest.TestCase):
    def test_evaluate(self):
        search_space = [0, 1]
        objective_function = lambda x: x**2
        problem = LearningProblem(search_space, objective_function)
        self.assertEqual(problem.evaluate(2), 4)
        self.assertEqual(problem.evaluate(-2), 4)

if __name__ == "__main__":
    unittest.main()
