# Program to construct a histogram based on a list of marks
# Lebogang Salagae
# 21 April 2024

# Converting user input into a list of integers
marks_input = input("Enter a space-separated list of marks:\n")
marks = list(map(int, marks_input.split()))

# Initializing counters for each category
counters = {
    "fail": 0,
    "third": 0,
    "lower_second": 0,
    "upper_second": 0,
    "first": 0,
}

# Categorizing marks to update the counters
for mark in marks:
    if mark < 50:
        counters["fail"] += 1
    elif 50 <= mark < 60:
        counters["third"] += 1
    elif 60 <= mark < 70:
        counters["lower_second"] += 1
    elif 70 <= mark < 75:
        counters["upper_second"] += 1
    else:
        counters["first"] += 1

# Printing the histogram with correct labels
print("Histogram:")
print("1  |" + "X" * counters["first"])  # First-class marks
print("2+ |" + "X" * counters["upper_second"])  # Upper second-class marks
print("2- |" + "X" * counters["lower_second"])  # Lower second-class marks
print("3  |" + "X" * counters["third"])  # Third-class marks
print("F  |" + "X" * counters["fail"])  # Failures