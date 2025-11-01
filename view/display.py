# src/view/display.py
def print_header():
    print("\n" + "="*60)
    print("     ANALYSE DÉCISIONNELLE - OPTIMISATION D'INVESTISSEMENT")
    print("="*60)

def print_menu():
    print("\nMENU PRINCIPAL")
    print("1. Charger un dataset")
    print("2. Exécuter un algorithme")
    print("3. Comparaison finale")
    print("4. Quitter")

def print_algo_menu():
    print("\nChoisir un algorithme :")
    print("1. Programmation Dynamique (DP)")
    print("2. Glouton")
    print("3. Force Brute (petit dataset uniquement)")

def print_result(algo_name, actions, cost, profit, time_taken):
    print(f"\n--- RÉSULTAT {algo_name.upper()} ---")
    print(f"Actions sélectionnées : {len(actions)}")
    print(f"Coût total : {cost:,} F CFA")
    print(f"Profit total : {profit:,.2f} F CFA")
    print(f"Temps d'exécution : {time_taken:.4f} secondes")

def print_comparison(results):
    print("\n" + "="*70)
    print("               COMPARAISON FINALE DES ALGORITHMES")
    print("="*70)
    print(f"{'Dataset':<12} {'Algorithme':<12} {'Profit':>15} {'Temps (s)':>12}")
    print("-"*70)
    for res in results:
        print(f"{res['dataset']:<12} {res['algo']:<12} {res['profit']:>15,.2f} {res['time']:>12.4f}")