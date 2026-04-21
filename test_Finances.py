from finance import calculateBudget, convertCurrency

# ---- calcuteBudget tests ----

result = calculateBudget(10, 25)
if result == 250:
    print("Test 1 passed.")
else:
    print(f"Test 1 failed. Expected 250, got {result}")

result = calculateBudget(0, 100)
if result == 0:
    print("Test 2 passed.")
else:
    print(f"Test 2 failed. Expected 0, got {result}")

result = calculateBudget("5.5", "20")
if result == 110:
    print("Test 3 passed.")
else:
    print(f"Test 3 failed. Expected 110, got {result}")


# ---- convertCurrency tests ----

result = convertCurrency(1500, "USD")
if result == 1:
    print("Test 4 passed.")
else:
    print(f"Test 4 failed. Expected 1, got {result}")

result = convertCurrency(3200, "EUR")
if result == 2:
    print("Test 5 passed.")
else:
    print(f"Test 5 failed. Expected 2, got {result}")

result = convertCurrency(600, "BRL")
if result == 2:
    print("Test 6 passed.")
else:
    print(f"Test 6 failed. Expected 2, got {result}")

result = convertCurrency(1000, "JPY")   
if result is None:
    print("Test 7 passed.")
else: 
    print(f"Test 7 failed. Expected None, got {result}")   



