# MetaLearnAI performance_evaluation.py

class PerformanceEvaluator:
    def __init__(self, metrics):
        self.metrics = metrics

    def evaluate(self, true_values, predictions):
        results = {}
        for metric in self.metrics:
            results[metric.__name__] = metric(true_values, predictions)
        return results
