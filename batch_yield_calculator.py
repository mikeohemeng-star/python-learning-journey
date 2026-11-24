 #Multi-Batch Palm Oil Yield Calculator

for batch in range(1, 4):
    print("BATCH", batch)

    fruit = float(input("Enter fruit processed (kg): "))
    oil = float(input("Enter oil extracted (kg): "))

    yield_percentage = (oil / fruit) * 100

    print("Extraction yield:", yield_percentage, "%")
    print("------------------------")
