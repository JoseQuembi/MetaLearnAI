import numpy as np

def evaluate_performance(algorithm, problem, metrics):
    """
    Avalia o desempenho de um algoritmo de meta-aprendizado em um problema de aprendizado.

    Args:
        algorithm: O algoritmo de meta-aprendizado.
        problem: O problema de aprendizado.
        metrics: Uma lista de métricas para avaliar.

    Returns:
        Um dicionário com as métricas e seus valores.
    """
    results = {}
    for metric in metrics:
        results[metric.__name__] = metric(algorithm, problem)
    return results

# Exemplo de uma métrica de avaliação
def mean_squared_error(algorithm, problem):
    """
    Calcula o erro quadrático médio do algoritmo no problema.

    Args:
        algorithm: O algoritmo de meta-aprendizado.
        problem: O problema de aprendizado.

    Returns:
        O erro quadrático médio.
    """
    predictions = algorithm.predict(problem)
    true_values = problem.true_values()
    mse = np.mean((predictions - true_values) ** 2)
    return mse
