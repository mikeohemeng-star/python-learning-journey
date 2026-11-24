# Unlimited Palm Oil Batch Calculator

total_fruit = 0
total_oil = 0
batch = 0

while True:

    batch = batch + 1

    print("BATCH", batch)

    fruit = float(input("Enter fruit processed (kg): "))

    if fruit == 0:
        break

    oil = float(input("Enter oil extracted (kg): "))

    if fruit > 0 and oil >= 0:

        total_fruit = total_fruit + fruit
        total_oil = total_oil + oil

        yield_percentage = (oil / fruit) * 100

        print("Batch yield:", yield_percentage, "%")

    else:
        print("Invalid quantity. Batch not included.")
        batch = batch - 1

    print("--------------------")

if total_fruit > 0:

    overall_yield = (total_oil / total_fruit) * 100

    print("FINAL PRODUCTION REPORT")
    print("Total batches:", batch)
    print("Total fruit:", total_fruit, "kg")
    print("Total oil:", total_oil, "kg")
    print("Overall yield:", overall_yield, "%")
