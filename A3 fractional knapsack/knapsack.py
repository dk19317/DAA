# Class to store the item details
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    # Method to calculate the value-to-weight ratio
    def value_to_weight_ratio(self):
        return self.value / self.weight

# Function to solve the fractional knapsack problem
def fractional_knapsack(items, capacity):
    # Sort items by their value-to-weight ratio in descending order
    items.sort(key=lambda item: item.value_to_weight_ratio(), reverse=True)

    total_value = 0  # Total value in the knapsack
    remaining_capacity = capacity  # Remaining capacity of the knapsack

    # Loop through the sorted items
    for item in items:
        if item.weight <= remaining_capacity:
            # Take the entire item
            total_value += item.value
            remaining_capacity -= item.weight
        else:
            # Take the fraction of the remaining item
            fraction = remaining_capacity / item.weight
            total_value += item.value * fraction
            break  # Knapsack is full

    return total_value

# Main function to demonstrate the algorithm
if __name__ == "__main__":
    # List of items with value and weight
    items = [Item(60, 10), Item(100, 20), Item(120, 30)]
    capacity = 50  # Capacity of the knapsack

    max_value = fractional_knapsack(items, capacity)
    print(f"The maximum value in the knapsack is: {max_value}")

