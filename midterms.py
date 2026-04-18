# Hardcoded Expense Categories
categories = {
    1: ["Food & Drinks", "Lunch, snacks, coffee"],
    2: ["Transportation", "Bus, jeepney, ride-share"],
    3: ["Mobile / Internet", "Load, data plan, WiFi top-up"],
    4: ["School Supplies", "Notebook, pen, bond paper"],
    5: ["Entertainment", "Games, movies, hangout"]
}

# 1. Ask for name and budget
name = input("Student name: ")
budget = float(input("Weekly budget: "))
threshold = budget * 0.25  # 25% threshold for the alert

# 2. Display categories using a loop
print("\n==========================================")
print("   WEEKLY EXPENSE -- CATEGORIES")
print("==========================================")
for num, info in categories.items():
    print(f" {num}. {info[0]:<20} [e.g. {info[1]}]")
print("==========================================")

logged_expenses = []

# 3. Accept 4 expense entries
for i in range(1, 5):
    print(f"\n--- EXPENSE {i} ---")
    cat_num = int(input("Category (0 to skip): "))
    
    # Skip if user types 0
    if cat_num == 0:
        continue
    
    # 4. If valid, ask for description and amount
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

# 6. Compute totals and status
total_spent = sum(item["amt"] for item in logged_expenses)
remaining = budget - total_spent

if remaining >= 0:
    status = "Budget OK! Keep it up."
else:
    status = "Overspent! Reduce spending."

# 7. Print formatted expense log
print(f"\n======================================================")
print(f"     {name.upper()} -- WEEKLY EXPENSE LOG")
print(f"======================================================")
print(f"  Weekly Budget  : P{budget:.2f}")

for idx, item in enumerate(logged_expenses, 1):
    print(f"  [{idx}] {item['cat']}")
    # Align description and amount with the tag
    print(f"      {item['desc']: <35} P{item['amt']:.2f}  {item['tag']}")

print(f"------------------------------------------------------")
print(f"  Total Spent    : P{total_spent:.2f}")
print(f"  Remaining      : P{remaining:.2f}")
print(f"  Status         : {status}")
print(f"======================================================")