# Interactive Palm Oil Yield Calculator

fruit_bunches = float(input("Enter fruit processed in kg: "))
oil_extracted = float(input("Enter oil extracted in kg: "))

if fruit_bunches > 0:
    yield_percentage = (oil_extracted / fruit_bunches) * 100

    print("--------------------------")
    print("PALM OIL PRODUCTION REPORT")
    print("Fruit processed:", fruit_bunches, "kg")
    print("Oil extracted:", oil_extracted, "kg")
    print("Extraction yield:", yield_percentage, "%")

else:
    print("Error: Fruit processed must be greater than zero.")
