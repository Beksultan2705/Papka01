def find_cargo():
    total_weight = 713
    cargo_positions = [0, 0, 0]
    
    while True:
        print("Enter kilometer mark where the box may be buried (1-7):")
        for i in range(3):
            kilometer_mark = int(input(f"Box {i + 1}: "))
            
            # Check if cargo is at the entered kilometer mark
            if cargo_positions[i] == kilometer_mark:
                print(f"Box {i + 1} found at {kilometer_mark} kilometers.")
            else:
                print(f"Box {i + 1} not found at {kilometer_mark} kilometers. Tentacles are moving boxes.")
                # Update box positions randomly
                cargo_positions[i] = (cargo_positions[i] + 2) % 7 + 1
        
        # Check if the total weight is correct
        if sum(cargo_positions) == total_weight:
            print("Congratulations! All boxes found, and total weight is correct.")
            break
        else:
            print("Total weight is incorrect. Try again.")

if __name__ == "__main__":
    print("Martian Cargo Recovery Program")
    find_cargo()
