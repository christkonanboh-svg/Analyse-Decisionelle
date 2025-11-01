# src/controller/main_controller.py
from model.data_loader import DataLoader
from model.algorithms import InvestmentOptimizer
from view.display import *
import time

class Controller:
    def __init__(self):
        self.datasets = {}
        self.results = []

    def load_dataset(self, name, path):
        loader = DataLoader(path)
        df = loader.load_and_filter()
        self.datasets[name] = df
        print(f"Dataset '{name}' chargé : {len(df)} actions valides.")

    def run_algorithm(self, dataset_name, algo_choice):
        if dataset_name not in self.datasets:
            print("Dataset non chargé.")
            return
        df = self.datasets[dataset_name]
        budget = 500000

        algo_map = {
            1: ("DP", InvestmentOptimizer.dp_solution),
            2: ("Glouton", InvestmentOptimizer.greedy_solution),
            3: ("Force Brute", InvestmentOptimizer.brute_force)
        }

        if algo_choice not in algo_map:
            print("Choix invalide.")
            return

        algo_name, func = algo_map[algo_choice]
        if algo_choice == 3 and len(df) > 30:
            print("Force Brute non disponible pour >30 actions.")
            return

        start = time.time()
        if algo_choice == 3:
            actions, cost, profit, status = func(df, budget)
        else:
            actions, cost, profit = func(df, budget)
        end = time.time()
        elapsed = end - start

        print_result(algo_name, actions, cost, profit, elapsed)
        self.results.append({
            'dataset': dataset_name,
            'algo': algo_name,
            'profit': profit,
            'time': elapsed
        })