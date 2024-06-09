# MetaLearnAI utils.py

import numpy as np

def load_data(file_path):
    # Implementação para carregar dados a partir de um arquivo
    pass

def preprocess_data(data):
    # Implementação para preprocessamento dos dados
    pass

def split_data(data, train_size=0.8):
    # Dividir os dados em treino e teste
    np.random.shuffle(data)
    split_idx = int(len(data) * train_size)
    return data[:split_idx], data[split_idx:]
