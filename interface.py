import sys
from bankerImplementation import BankersAlgorithm

def load_configuration(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    available = list(map(int, lines[0].strip().split()))
    max_demand = [list(map(int, line.strip().split())) for line in lines[1:1+len(available)]]
    allocation = [list(map(int, line.strip().split())) for line in lines[1+len(available):1+2*len(available)]]

    return available, max_demand, allocation

def display_state(available, max_demand, allocation):
    print("\nRecursos Disponibles:")
    print(available)
    print("\nDemanda Máxima:")
    for row in max_demand:
        print(row)
    print("\nAsignacion:")
    for row in allocation:
        print(row)

def main():
    if len(sys.argv) != 2:
        print("Uso: python3 interface.py <config_file>")
        sys.exit(1)

    config_file = sys.argv[1]
    available, max_demand, allocation = load_configuration(config_file)

    banker = BankersAlgorithm(available, max_demand, allocation)

    display_state(available, max_demand, allocation)
    print("\n¿Estado inicial seguro?", banker.is_safe())

if __name__ == "__main__":
    main()
