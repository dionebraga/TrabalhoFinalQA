import random

def generate_product():
    return {
        "name": f"Produto {random.randint(1, 1000)}",
        "description": "Descrição gerada automaticamente.",
        "price": round(random.uniform(10, 1000), 2),
        "image_url": "https://via.placeholder.com/150"
    }
