# MetaLearnAI example_performance_evaluation.py

from metalearnai.performance_evaluation import PerformanceEvaluator

def accuracy(true_values, predictions):
    return sum(t == p for t, p in zip(true_values, predictions)) / len(true_values)

evaluator = PerformanceEvaluator(metrics=[accuracy])
true_values = [1, 0, 1, 1]
predictions = [1, 0, 0, 1]
results = evaluator.evaluate(true_values, predictions)
print(results)
