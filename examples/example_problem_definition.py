# MetaLearnAI example_problem_definition.py

from metalearnai.problem_definition import LearningProblem

search_space = [0, 1, 2, 3, 4]
objective_function = lambda x: x**2
constraints = [lambda x: x >= 0]

problem = LearningProblem(search_space, objective_function, constraints)
print(problem.evaluate(2))
