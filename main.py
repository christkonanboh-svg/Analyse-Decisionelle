# src/main.py
from controller.main_controller import Controller
from view.display import *

def main():
    print_header()
    ctrl = Controller()

    # Chargement automatique des datasets
    ctrl.load_dataset("Petit", "../data/data_small.csv")
    ctrl.load_dataset("Dataset1", "../data/data1.csv")
    ctrl.load_dataset("Dataset2", "../data/data2.csv")

    while True:
        print_menu()
        choice = input("\nChoisir une option (1-4) : ").strip()

        if choice == '1':
            print("Datasets déjà chargés : Petit, Dataset1, Dataset2")

        elif choice == '2':
            dataset = input("Dataset (Petit/Dataset1/Dataset2) : ").strip()
            if dataset not in ctrl.datasets:
                print("Dataset inconnu.")
                continue
            print_algo_menu()
            algo = int(input("Algorithme (1-3) : ").strip())
            ctrl.run_algorithm(dataset, algo)

        elif choice == '3':
            if not ctrl.results:
                print("Aucun résultat à comparer.")
            else:
                print_comparison(ctrl.results)

        elif choice == '4':
            print("Au revoir !")
            break
        else:
            print("Option invalide.")

if __name__ == "__main__":
    main()