categories = {
    1: ["Food & Drinks", "Lunch, snacks, coffee"],
    2: ["Transportation", "Bus, jeepney, ride-share"],
    3: ["Mobile / Internet", "Load, data plan, WiFi top-up"],
    4: ["School Supplies", "Notebook, pen, bond paper"],
    5: ["Entertainment", "Games, movies, hangout"]
}


name = input("Student name: ")
while True:
    try:
        budget_input = input("Weekly budget: ")
        budget = float(budget_input)
        break  # Exit the loop if conversion to float is successful
    except ValueError:
        print("Invalid input! Please enter a numeric value for the budget.")

threshold = budget * 0.25 



print("\n==========================================")
print("   WEEKLY EXPENSE -- CATEGORIES")
print("==========================================")
for num, info in categories.items():
    print(f" {num}. {info[0]:<20} [e.g. {info[1]}]")
print("==========================================")

logged_expenses = []


for i in range(1, 5):
    print(f"\n--- EXPENSE {i} ---")
    cat_num = int(input("Category (0 to skip): "))
    
   
    if cat_num == 0:
        continue
    
    
    if cat_num in categories:
        desc = input("Description: ")
        amt = float(input("Amount: "))
        
        # 5. Tag high expenses (> 25% of budget)
        tag = ""
        if amt > threshold:
            tag = "! High Expense Alert!"
            
        logged_expenses.append({
            "cat": categories[cat_num][0],
            "desc": desc,
            "amt": amt,
            "tag": tag
        })
    else:
        print("Invalid category. Entry skipped.")

total_spent = sum(item["amt"] for item in logged_expenses)
remaining = budget - total_spent

if remaining >= 0:
    status = "Budget OK! Keep it up."
else:
    status = "Overspent! Reduce spending."


print(f"\n======================================================")
print(f"     {name.upper()} -- WEEKLY EXPENSE LOG")
print(f"======================================================")
print(f"  Weekly Budget  : P{budget:.2f}")

for idx, item in enumerate(logged_expenses, 1):
    print(f"  [{idx}] {item['cat']}")
   
    print(f"      {item['desc']: <35} P{item['amt']:.2f}  {item['tag']}")

print(f"------------------------------------------------------")
print(f"  Total Spent    : P{total_spent:.2f}")
print(f"  Remaining      : P{remaining:.2f}")
print(f"  Status         : {status}")
print(f"======================================================")


print("\n==========================================")
print("   WEEKLY EXPENSE -- CATEGORIES")
print("==========================================")
for num, info in categories.items():
    print(f" {num}. {info[0]:<20} [e.g. {info[1]}]")
print("============================================")

logged_expenses = []


for i in range(1, 5):
    print(f"\n--- EXPENSE {i} ---")
    cat_num = int(input("Category (0 to skip): "))
    
   
    if cat_num == 0:
        continue
    
    
    if cat_num in categories:
        desc = input("Description: ")
        amt = float(input("Amount: "))
        
        # 5. Tag high expenses (> 25% of budget)
        tag = ""
        if amt > threshold:
            tag = "! High Expense Alert!"
            
        logged_expenses.append({
            "cat": categories[cat_num][0],
            "desc": desc,
            "amt": amt,
            "tag": tag
        })
    else:
        print("Invalid category. Entry skipped.")

total_spent = sum(item["amt"] for item in logged_expenses)
remaining = budget - total_spent

if remaining >= 0:
    status = "Budget OK! Keep it up."
else:
    status = "Overspent! Reduce spending."


print(f"\n======================================================")
print(f"     {name.upper()} -- WEEKLY EXPENSE LOG")
print(f"======================================================")
print(f"  Weekly Budget  : P{budget:.2f}")

for idx, item in enumerate(logged_expenses, 1):
    print(f"  [{idx}] {item['cat']}")
   
    print(f"      {item['desc']: <35} P{item['amt']:.2f}  {item['tag']}")

print(f"------------------------------------------------------")
print(f"  Total Spent    : P{total_spent:.2f}")
print(f"  Remaining      : P{remaining:.2f}")
print(f"  Status         : {status}")
print(f"======================================================")
