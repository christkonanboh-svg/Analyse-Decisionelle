# view/display.py
def header():
    print("\n" + "="*70)
    print("     ANALYSE DÉCISIONNELLE - OPTIMISATION D'INVESTISSEMENT")
    print("="*70)

def menu():
    print("\nMENU PRINCIPAL")
    print("1. Charger les datasets")
    print("2. Exécuter un algorithme")
    print("3. Voir la comparaison finale")
    print("4. Quitter")
    print("-" * 40)

def algo_menu():
    print("\nCHOISIR UN ALGORITHME")
    print("1. Programmation Dynamique (DP)")
    print("2. Glouton")
    print("3. Force Brute (petit dataset uniquement)")
    print("-" * 40)

def result(algo, actions, cost, profit, time):
    print(f"\nRÉSULTAT : {algo.upper()}")
    print(f"Actions sélectionnées : {len(actions)}")
    print(f"Actions choisies : {actions}")
    print(f"Coût total : {cost:,} F CFA")
    print(f"Profit total : {profit:,.2f} F CFA")
    print(f"Temps d'exécution : {time:.4f} s")
    print("-" * 40)

def comparison(results):
    print("\nCOMPARAISON FINALE")
    print("="*90)
    print(f"{'Dataset':<15} {'Algo':<12} {'Profit (F CFA)':>20} {'Temps (s)':>12}")
    print("-"*90)
    for r in results:
        print(f"{r['dataset']:<15} {r['algo']:<12} {r['profit']:>20,.2f} {r['time']:>12.4f}")
    print("="*90)

    # Comparaison avec Sienna
    sienna1 = 196610
    sienna2 = 193780
    dp1 = next((r['profit'] for r in results if r['dataset'] == 'Dataset1' and r['algo'] == 'DP'), 0)
    dp2 = next((r['profit'] for r in results if r['dataset'] == 'Dataset2' and r['algo'] == 'DP'), 0)

    print("\nCOMPARAISON AVEC SIENNA")
    print("-"*50)
    print(f"Dataset1 - Sienna : {sienna1:,} F CFA")
    print(f"Dataset1 - Mon DP : {dp1:,.2f} F CFA → Diff : {dp1 - sienna1:+,.2f}")
    print(f"Dataset2 - Sienna : {sienna2:,} F CFA")
    print(f"Dataset2 - Mon DP : {dp2:,.2f} F CFA → Diff : {dp2 - sienna2:+,.2f}")
    print("-"*50)