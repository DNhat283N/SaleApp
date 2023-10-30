def get_categories():
    return [{
        'id': 1,
        'name': 'Mobile'
    }, {
        'id': 2,
        'name': 'Tablet'
    }
    ]

def get_products(key):
    products = [
        {
            'id': 1,
            'name': 'iPhone 13',
            'price': 20000000,
            'category_id': 1,
            'image': "https://cdn1.viettelstore.vn/Images/Product/ProductImage/213191152.jpeg"
        },
        {
            'id': 2,
            'name': 'iPhone 13 Pro',
            'price': 23000000,
            'category_id': 1,
            'image': "https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-13-pro.png"
        },
        {
            'id': 3,
            'name': 'iPhone 13 Pro Max',
            'price': 27000000,
            'category_id': 1,
            'image': "https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-13-pro-max-256gb.png"
        },
        {
            'id': 4,
            'name': 'iPhone 14',
            'price': 26000000,
            'category_id': 1,
            'image': "https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-14_1.png"
        },
        {
            'id': 5,
            'name': 'iPhone 14 Pro',
            'price': 26000000,
            'category_id': 1,
            'image': "https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-14-pro_2__4.png"
        },
        {
            'id': 6,
            'name': 'iPhone 14 Pro Max',
            'price': 26000000,
            'category_id': 1,
            'image': "https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-14-pro_2__5.png"
        },
        {
            'id': 7,
            'name': 'Xiaomi 13',
            'price': 11750000,
            'category_id': 1,
            'image': "https://cdn.mobilecity.vn/mobilecity-vn/images/2022/12/w300/xiaomi-13-xanh-mint-1.png.webp"
        },
        {
            'id': 8,
            'name': 'Xiaomi 14 Snapdragon 8 Gen 3',
            'price': 17950000,
            'category_id': 1,
            'image': "https://cdn.mobilecity.vn/mobilecity-vn/images/2023/10/w300/xiaomi-14-pro-titanium.jpg.webp"
        },
        {
            'id': 9,
            'name': 'Xiaomi 13 5G(Dimensity 1080)',
            'price': 11750000,
            'category_id': 1,
            'image': "https://cdn.mobilecity.vn/mobilecity-vn/images/2023/07/w300/xiaomi-redmi-13-ro-ri-00.jpg.webp"
        },
    ]
    if key:
        products = [p for p in products if p['name'].find(key) >= 0]

    return products
