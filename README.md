Step 1: Setting up the Categories
The program starts by creating a Dictionary called categories.
Key: The number (1–5) the user will type.
Value: A list containing the Category Name and Examples. This acts as the "database" for the program.
Step 2: Getting Basic User Info
The program asks for the student's Name and Weekly Budget.
It uses float() to convert the budget into a decimal number so it can handle centavos.
It immediately calculates the threshold (Budget x 0.25). This stores the "limit" for what counts as a "High Expense."
Step 3: Displaying the Menu
It uses a for loop to go through the dictionary and print the categories. This ensures that even if you added a 6th category later, it would automatically show up on the screen.
Step 4: The 4-Entry Loop
The code uses for i in range(1, 5): to repeat the expense entry process exactly 4 times. Inside this loop:
The Skip Rule: If you type 0, it hits continue. This tells the computer: "Stop right here and jump to the next expense slot."
Validation: It checks if cat_num in categories to make sure you didn't type a wrong number like 9.
Step 5: Logging and Alerting
If the category is valid:
It asks for the Description and Amount.
The High Expense Check: It compares the amt you just typed against the threshold calculated in Step 2.
Storage: It saves all this info (category name, description, amount, and the "Alert" tag) into a list called logged_expenses.
Step 6: Math & Final Status
After the loop finishes:
Totaling: It uses sum() to add up every "amt" saved in your list.
Remaining: It subtracts the total from your original budget.
Budget Status: It uses an if-else statement to check if your remaining balance is positive (Budget OK) or negative (Overspent).
Step 7: Printing the Final Report
Finally, it prints a formatted receipt:
name.upper(): Makes the student's name look professional in all caps.
enumerate(logged_expenses, 1): This loops through your saved items and automatically numbers them (1, 2, 3).
:.2f: This is "Formatting Magic" that ensures every price looks like P150.00 instead of P150.0.
