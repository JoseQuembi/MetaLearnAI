# problem_definition.py

class LearningProblem:
    def __init__(self, search_space, objective_function, constraints=None):
        self.search_space = search_space
        self.objective_function = objective_function
        self.constraints = constraints or []

    def evaluate(self, solution):
        if all(constraint(solution) for constraint in self.constraints):
            return self.objective_function(solution)
        else:
            return float('inf')
