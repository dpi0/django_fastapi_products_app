def product_serializer(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "image": product["content"],
    }


def product_list_serializer(products) -> list:
    return [product_serializer(product) for product in products]
