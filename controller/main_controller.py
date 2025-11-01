# controller/main_controller.py
import time
import os
from model.data_loader import load_dataset
from model.algorithms import dp_solution, greedy_solution, brute_force
from view.display import result

BUDGET = 500000

class Controller:
    def __init__(self):
        self.datasets = {}
        self.results = []

    def load(self, name, file):
        path = os.path.join("data", file)
        if not os.path.exists(path):
            print(f"ERREUR : {path} introuvable")
            return False
        self.datasets[name] = load_dataset(path, BUDGET)
        print(f"{name} chargé : {len(self.datasets[name])} actions")
        return True

    def run(self, name, choice):
        if name not in self.datasets:
            print("Dataset non chargé")
            return
        df = self.datasets[name]

        if choice == 1:
            algo, func = "DP", dp_solution
        elif choice == 2:
            algo, func = "Glouton", greedy_solution
        elif choice == 3:
            if len(df) > 30:
                print("Force Brute impossible (>30 actions)")
                return
            algo, func = "Force Brute", brute_force
        else:
            print("Choix invalide")
            return

        start = time.time()
        actions, cost, profit = func(df, BUDGET)
        t = time.time() - start

        result(algo, actions, cost, profit, t)
        self.results.append({
            'dataset': name,
            'algo': algo,
            'profit': profit,
            'time': t
        })