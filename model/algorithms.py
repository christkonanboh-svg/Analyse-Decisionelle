# src/model/algorithms.py
import itertools
import time

class InvestmentOptimizer:
    @staticmethod
    def dp_solution(actions, budget):
        n = len(actions)
        dp = [0.0] * (budget + 1)
        choices = [-1] * (budget + 1)
        for i in range(n):
            cost = actions.iloc[i]['cost']
            profit = actions.iloc[i]['profit']
            for w in range(budget, cost - 1, -1):
                new_profit = dp[w - cost] + profit
                if new_profit > dp[w]:
                    dp[w] = new_profit
                    choices[w] = i
        selected = []
        w = budget
        while w > 0 and choices[w] >= 0:
            i = choices[w]
            selected.append(actions.iloc[i]['id'])
            w -= actions.iloc[i]['cost']
        total_cost = budget - w
        return selected, total_cost, dp[budget]

    @staticmethod
    def greedy_solution(actions, budget):
        actions = actions.copy()
        actions['ratio'] = actions['profit'] / actions['cost']
        sorted_actions = actions.sort_values(by='ratio', ascending=False)
        selected, total_cost, total_profit = [], 0, 0
        for _, row in sorted_actions.iterrows():
            if total_cost + row['cost'] <= budget:
                selected.append(row['id'])
                total_cost += row['cost']
                total_profit += row['profit']
        return selected, total_cost, total_profit

    @staticmethod
    def brute_force(actions, budget):
        n = len(actions)
        if n > 30:
            return [], 0, 0, "Trop d'actions (>30)"
        max_profit = 0
        best_combo, best_cost = [], 0
        for combo in itertools.product([0, 1], repeat=n):
            total_cost = sum(actions['cost'][i] for i in range(n) if combo[i])
            if total_cost > budget: continue
            total_profit = sum(actions['profit'][i] for i in range(n) if combo[i])
            selected = [actions['id'][i] for i in range(n) if combo[i]]
            if total_profit > max_profit:
                max_profit = total_profit
                best_combo = selected
                best_cost = total_cost
        return best_combo, best_cost, max_profit, "OK"