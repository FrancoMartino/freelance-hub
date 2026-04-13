def calculate_budget(estimated_hours, hourly_rate):
    try:
        hours = float(estimated_hours)
        rate = float(hourly_rate)
    except (ValueError, TypeError):
        print("Error: inputs must be numeric.")
        return None

    total_cost = hours * rate
    return total_cost
    

if __name__ == "__main__":
    print(calculate_budget(10,25))
    print(calculate_budget(0, 100))
    print(calculate_budget("abc", 25))
    print(calculate_budget(10, ""))
    print(calculate_budget("5.5", "20"))

