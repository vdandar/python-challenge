# Initial variable to track shopping status
cart = 'Yes'

# List to track pie purchases
pie_order = []

# Pie List
pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun",
            "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

# Display initial message
print("Welcome to the Valerie's Pies! Here are our pies:")

# While we are still shopping...
while cart == "Yes":

    # Show pie selection prompt
    print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, " +
          " (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, " +
          " (9) Tamale, (10) Steak ")

    pie_choice = input("Which would you like to oder? ")

    # Add pie to the pie list
    pie_order.append(pie_choice)


    # Inform the customer of the pie purchase
    print("Great! We'll have that " + pie_list[int(pie_choice) - 1] + " pie right out for you.")

    # Provide exit option
    cart = input("Would you like to make another purchase: (Yes) or (No)? ")

# Once the pie list is complete
print("You purchased a total of " + str(len(pie_order)) + " pies.")
