import requests

response = requests.get("https://fakestoreapi.com/products")

if response.status_code == 200:
    products = response.json()

    prices = [product['price'] for product in products]
    max_price = max(prices)
    min_price = min(prices)
    avg_price = sum(prices) / len(prices)

    print(f"Max Price: {max_price}")
    print(f"Min Price: {min_price}")
    print(f"Average Price: {avg_price}")

    categories = sorted(set(product['category'] for product in products))
    print("\nCategories (sorted, unique):")
    print(categories)

    title_id_list = [(product['title'], product['id']) for product in products]
    sorted_title_id_list = sorted(title_id_list, key=lambda x: x[0])

    print("\nProducts (title, id) sorted by title:")
    for title, product_id in sorted_title_id_list:
        print(f"Title: {title}, ID: {product_id}")

    ratings = [(product['rating']['rate'], product['title']) for product in products]
    sorted_ratings = sorted(ratings, key=lambda x: x[0])

    print("\nProducts sorted by rating (rate):")
    for rate, title in sorted_ratings:
        print(f"Rating: {rate}, Title: {title}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
