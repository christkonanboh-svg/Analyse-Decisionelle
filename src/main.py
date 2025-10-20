import pandas as pd
import itertools
import time

# Charger les données
df_small = pd.read_csv('../data/data_small.csv')
df_large1 = pd.read_csv('../data/data1.csv')
df_large2 = pd.read_csv('../data/data2.csv')

# Filtrer les actions (coût > 0 et <= 500000)
df_small = df_small[(df_small['cost'] > 0) & (df_small['cost'] <= 500000)].reset_index(drop=True)
df_large1 = df_large1[(df_large1['cost'] > 0) & (df_large1['cost'] <= 500000)].reset_index(drop=True)
df_large2 = df_large2[(df_large2['cost'] > 0) & (df_large2['cost'] <= 500000)].reset_index(drop=True)

# Budget maximum
BUDGET = 500000

# Calculer le profit pour chaque action
for df in [df_small, df_large1, df_large2]:
    df['profit'] = df['cost'] * (df['profit_pct'] / 100)
print("Liste des actions (petit dataset) :")
print(df_small)
print("\nListe des actions (grand dataset 1) :")
print(df_large1)
print("\nListe des actions (grand dataset 2) :")
print(df_large2)

# Solution DP : Optimisation exacte
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

# Solution Glouton : Approche rapide
def greedy_solution(actions, budget):
    actions['ratio'] = actions['profit'] / actions['cost']
    sorted_actions = actions.sort_values(by='ratio', ascending=False)
    selected = []
    total_cost = 0
    total_profit = 0
    for index, row in sorted_actions.iterrows():
        if total_cost + row['cost'] <= budget:
            selected.append(row['id'])
            total_cost += row['cost']
            total_profit += row['profit']
    return selected, total_cost, total_profit

# Solution Force Brute : Exhaustive pour petits datasets
def brute_force(actions, budget):
    n = len(actions)
    if n > 30:
        print("Force brute sautée car trop de données (n > 30)")
        return [], 0, 0
    max_profit = 0
    best_combo = []
    best_cost = 0
    for combo in itertools.product([0, 1], repeat=n):
        total_cost = sum(actions['cost'][i] for i in range(n) if combo[i] == 1)
        if total_cost > budget:
            continue
        total_profit = sum(actions['profit'][i] for i in range(n) if combo[i] == 1)
        selected = [actions['id'][i] for i in range(n) if combo[i] == 1]
        if total_profit > max_profit:
            max_profit = total_profit
            best_combo = selected
            best_cost = total_cost
    return best_combo, best_cost, max_profit

# Exécution
print("\n--- Exécution des solutions ---")

# DP sur grand dataset 1
start_time_dp1 = time.time()
dp_actions1, dp_cost1, dp_profit1 = dp_solution(df_large1, BUDGET)
end_time_dp1 = time.time()
print("\nSolution DP (grand dataset 1) :")
print("Actions :", dp_actions1)
print("Coût :", dp_cost1)
print("Profit :", dp_profit1)
print("Temps :", end_time_dp1 - start_time_dp1, "secondes")

# DP sur grand dataset 2
start_time_dp2 = time.time()
dp_actions2, dp_cost2, dp_profit2 = dp_solution(df_large2, BUDGET)
end_time_dp2 = time.time()
print("\nSolution DP (grand dataset 2) :")
print("Actions :", dp_actions2)
print("Coût :", dp_cost2)
print("Profit :", dp_profit2)
print("Temps :", end_time_dp2 - start_time_dp2, "secondes")

# Glouton sur grand dataset 1
start_time_greedy1 = time.time()
greedy_actions1, greedy_cost1, greedy_profit1 = greedy_solution(df_large1, BUDGET)
end_time_greedy1 = time.time()
print("\nSolution Glouton (grand dataset 1) :")
print("Actions :", greedy_actions1)
print("Coût :", greedy_cost1)
print("Profit :", greedy_profit1)
print("Temps :", end_time_greedy1 - start_time_greedy1, "secondes")

# Glouton sur grand dataset 2
start_time_greedy2 = time.time()
greedy_actions2, greedy_cost2, greedy_profit2 = greedy_solution(df_large2, BUDGET)
end_time_greedy2 = time.time()
print("\nSolution Glouton (grand dataset 2) :")
print("Actions :", greedy_actions2)
print("Coût :", greedy_cost2)
print("Profit :", greedy_profit2)
print("Temps :", end_time_greedy2 - start_time_greedy2, "secondes")

# Force Brute sur petit dataset
start_time_brute = time.time()
brute_actions, brute_cost, brute_profit = brute_force(df_small, BUDGET)
end_time_brute = time.time()
print("\nSolution Force Brute (petit dataset) :")
print("Actions :", brute_actions)
print("Coût :", brute_cost)
print("Profit :", brute_profit)
print("Temps :", end_time_brute - start_time_brute, "secondes")

# Comparaison
print("\n--- Comparaison ---")
print("Force Brute (petit) Profit :", brute_profit)
print("DP (dataset1) Profit :", dp_profit1)
print("Glouton (dataset1) Profit :", greedy_profit1)
print("DP (dataset2) Profit :", dp_profit2)
print("Glouton (dataset2) Profit :", greedy_profit2)