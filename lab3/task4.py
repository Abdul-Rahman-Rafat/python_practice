import json
from task7 import log_time


@log_time
def product_data_transformer():

    products = input("Enter product names (comma-separated): ").strip().split(",")
    products = [p.strip() for p in products if p.strip()]  
    
    while True:
        try:
            prices = list(map(float, input("Enter product prices (comma-separated): ").strip().split(",")))
            break
        except ValueError:
            print("Invalid input! Please enter numbers only (e.g., 10, 20.5, 30)")
    
    paired = list(zip(products, prices))

    valid_items = list(filter(lambda z: z[1] > 0, paired))

    transformed = list(map(lambda x: {
        "product": x[0],
        "price": x[1],
        "discounted": round(x[1] * 0.9, 2)
    }, valid_items))

    with open("products.json", "w") as f:
        json.dump(transformed, f, indent=4)

    print("Preview of first 5 results:")
    for item in transformed[:5]:
        print(item)


