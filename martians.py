import random

def find_martian_cargo():
    total_weight = 713
    cargo_positions = [0, 0, 0]

    def tentacles_move_boxes(cargo_positions):
        return [random.randint(1, 7) for _ in cargo_positions]

    while True:
        print("Enter the kilometer marks where the boxes may be buried (1-7):")
        for i in range(3):
            kilometer_mark = int(input(f"Enter the kilometer mark for Box {i + 1}: "))

            if cargo_positions[i] == kilometer_mark:
                print(f"Box {i + 1} found at {kilometer_mark} kilometers.")
            else:
                print(f"Box {i + 1} not found at {kilometer_mark} kilometers. Tentacles are moving boxes.")
                cargo_positions = tentacles_move_boxes(cargo_positions)

        if sum(cargo_positions) == total_weight:
            print("Congratulations! All boxes found, and the total weight is correct.")
            break
        else:
            print("The total weight is incorrect. Try again.")

if __name__ == "__main__":
    print("Martian Cargo Recovery Program")
    find_martian_cargo()
