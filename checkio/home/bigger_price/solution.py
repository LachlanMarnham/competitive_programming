def bigger_price(limit: int, data: list) -> list:
    data.sort(key=lambda item: item["price"], reverse=True)
    return data[:limit]
