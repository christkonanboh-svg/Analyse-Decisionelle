# model/algorithms.py
import itertools
import time

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

def greedy_solution(actions, budget):
    df = actions.copy()
    df['ratio'] = df['profit'] / df['cost']
    df = df.sort_values('ratio', ascending=False)
    selected, cost, prof = [], 0, 0
    for _, r in df.iterrows():
        if cost + r['cost'] <= budget:
            selected.append(r['id'])
            cost += r['cost']
            prof += r['profit']
    return selected, cost, prof

def brute_force(actions, budget):
    n = len(actions)
    if n > 30:
        return [], 0, 0
    best_p, best_s, best_c = 0, [], 0
    for combo in itertools.product([0, 1], repeat=n):
        cost = sum(actions.iloc[i]['cost'] for i in range(n) if combo[i])
        if cost > budget: continue
        prof = sum(actions.iloc[i]['profit'] for i in range(n) if combo[i])
        if prof > best_p:
            best_p, best_c = prof, cost
            best_s = [actions.iloc[i]['id'] for i in range(n) if combo[i]]
    return best_s, best_c, best_p