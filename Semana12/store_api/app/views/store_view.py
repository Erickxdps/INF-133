def render_product_list(products):
    return [
        {
            "id":product.id,
            "marca":product.name,
            "peso":product.description,
            "sabor":product.price,
            "origen":product.stock
        }
        for product in products
    ]

def render_product_detail(product):
    return {
            "id":product.id,
            "marca":product.name,
            "peso":product.description,
            "sabor":product.price,
            "origen":product.stock
        }