def analyze_behavior(performance_data):
    comparisons = performance_data.get('comparisons', 0)
    swaps = performance_data.get('swaps', 0)
    time_taken = performance_data.get('time', 0)

    tips = []

    if comparisons > 500:
        tips.append("Try choosing a more efficient algorithm like Quick Sort for large datasets.")
    if swaps > 500:
        tips.append("Minimize swaps by better understanding algorithm efficiency.")
    if time_taken > 2:
        tips.append("Consider optimizing your input or using faster algorithms.")

    if not tips:
        tips.append("Great job! Your understanding seems solid.")

    performance = "High"
    if comparisons > 100 or swaps > 50 or time_taken > 2:
        performance = "Medium"
    if comparisons > 200 or swaps > 100 or time_taken > 4:
        performance = "Low"

    return {
        "performance": performance,
        "tips": tips
    }
