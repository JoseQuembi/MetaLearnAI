
### Módulos

#### `metalearnai/problem_definition.py`

python
class LearningProblem:
    def __init__(self, search_space, objective_function, constraints=None):
        self.search_space = search_space
        self.objective_function = objective_function
        self.constraints = constraints or []

    def evaluate(self, solution):
        # Implementação da avaliação da solução
        pass
