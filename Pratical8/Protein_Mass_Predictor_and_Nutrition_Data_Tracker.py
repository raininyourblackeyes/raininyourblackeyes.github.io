# make a protein mass predictor
def calculate_protein_mass(sequence):
    amino_acid_masses = {
        "G": 57.02,
        "A": 71.04,
        "S": 87.03,
        "P": 97.05,
        "V": 99.07,
        "T": 101.05,
        "C": 103.01,
        "I": 113.08,
        "L": 113.08,
        "N": 114.04,
        "D": 115.03,
        "Q": 128.06,
        "K": 128.09,
        "E": 129.04,
        "M": 131.04,
        "H": 137.06,
        "F": 147.07,
        "R": 156.10,
        "Y": 163.06,
        "W": 186.08
    }
    sequence = sequence.upper().strip()

    if sequence == "":
        return 'Error: empty sequence provided.'
    
    total_mass = 0
    for amino_acid in sequence:
        if amino_acid in amino_acid_masses:
            total_mass += amino_acid_masses[amino_acid]
        else:
            return f'Error: invalid amino acid "{amino_acid}" found in sequence.'
        
    return total_mass

# nutrition data tracker
class food_item:
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

        if self.calories < 0 or self.protein < 0 or self.carbs < 0 or self.fat < 0:
            raise ValueError("Nutritional values cannot be negative.")
    
def nutrition_data_tracker(food_list):
    total_calories = 0
    total_protein = 0
    total_carbs = 0
    total_fat = 0

    for food in food_list:
        total_calories += food.calories
        total_protein += food.protein
        total_carbs += food.carbs
        total_fat += food.fat

    print("Nutrition report for 24 hours:")
    print(f"Total calories: {total_calories}")
    print(f"Total protein: {total_protein}g")
    print(f"Total carbs: {total_carbs}g")
    print(f"Total fat: {total_fat}g")

    warnings = []

    if total_calories > 2500:
        warning_massage = "Warning: Total calorie intake exceeds the recommended daily limit of 2500 calories."
        print(warning_massage)
        warnings.append(warning_massage)
    
    if total_fat > 90:
        warning_massage = "Warning: Total fat intake exceeds the recommended daily limit of 90g."
        print(warning_massage)
        warnings.append(warning_massage)

    return {
        "total_calories": total_calories,
        "total_protein": total_protein,
        "total_carbs": total_carbs,
        "total_fat": total_fat,
        "warnings": warnings
    }

#Example usage

if __name__ == "__main__":

    # Example usage of the protein mass predictor
    protein_sequence = 'ACDEFGHIKLMNPQRSTVWY'
    protein_mass = calculate_protein_mass(protein_sequence)
    print("Protein sequence: ", protein_sequence)
    print("Protein mass: ", round(protein_mass, 2), "amu")
    
    # Example usage of the nutrition data tracker
    apple = food_item("apple", 60, 0.3, 15, 0.5)
    rice = food_item("rice", 300, 6, 65, 1)
    chicken = food_item("chicken breast", 250, 45, 0, 5)
    burger = food_item("burger", 800, 35, 50, 40)
    fries = food_item("fries", 600, 7, 70, 35)
    cake = food_item("cake", 650, 6, 80, 25)

    food_list = [apple, rice, chicken, burger, fries, cake]
    nutrition_data_tracker(food_list)

