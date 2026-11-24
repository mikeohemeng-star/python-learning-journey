# Palm Oil Batch Production Summary

total_fruit = 0
total_oil = 0

for batch in range(1, 4):

    print("BATCH", batch)

    fruit = float(input("Enter fruit processed (kg): "))
    oil = float(input("Enter oil extracted (kg): "))

    if fruit > 0:
        yield_percentage = (oil / fruit) * 100

        total_fruit = total_fruit + fruit
        total_oil = total_oil + oil

        print("Batch yield:", yield_percentage, "%")

    else:
        print("Invalid fruit quantity. Batch not included.")

    print("----------------------")

if total_fruit > 0:
    overall_yield = (total_oil / total_fruit) * 100

    print("TOTAL FRUIT:", total_fruit, "kg")
    print("TOTAL OIL:", total_oil, "kg")
    print("OVERALL YIELD:", overall_yield, "%")

