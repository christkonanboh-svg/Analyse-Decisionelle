# main.py
from controller.main_controller import Controller
from view.display import header, menu, algo_menu, comparison

ctrl = Controller()

# Chargement automatique
ctrl.load("Petit", "data_small.csv")
ctrl.load("Dataset1", "data1.csv")
ctrl.load("Dataset2", "data2.csv")

header()

while True:
    menu()
    choice = input("Choisir (1-4) : ").strip()

    if choice == '1':
        ctrl.load("Petit", "data_small.csv")
        ctrl.load("Dataset1", "data1.csv")
        ctrl.load("Dataset2", "data2.csv")

    elif choice == '2':
        dataset = input("Dataset (Petit/Dataset1/Dataset2) : ").strip()
        if dataset not in ctrl.datasets:
            print("Dataset inconnu")
            continue
        algo_menu()
        try:
            algo = int(input("Algorithme (1-3) : ").strip())
            ctrl.run(dataset, algo)
        except:
            print("Entrez un nombre valide")

    elif choice == '3':
        if ctrl.results:
            comparison(ctrl.results)
        else:
            print("Aucun résultat disponible")

    elif choice == '4':
        print("Au revoir !")
        break

    else:
        print("Option invalide")