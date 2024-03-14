# insert_people.py

import os
import django
from django.db import connection



# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_project.settings')
django.setup()

from products.models import Product


Product.objects.all().delete()

products = [
    Product(name="Vaporwaffle Sacai Sail Gum", price=6500.00, image_name="product-1", sizes="37 38 39 40 42", category="Nike"),
    Product(name="Dunk Low Triple Pink", price=2500.00, image_name="product-2", sizes="37 38 39 41 43", category="Nike"),
    Product(name="Dunk Low Industrial Blue", price=2800.00, image_name="product-3", sizes="37 38 39 40 42", category="Nike"),
    Product(name="SB Dunk Low Concepts Orange Lobster", price=5800.00, image_name="product-20", sizes="37 38 39 40 42", category="Nike"),
    Product(name="Dunk Low SE Lottery Green Pale Ivory", price=2500.00, image_name="product-4", sizes="37 38 39 40 42", category="Nike"),
    Product(name="Dunk Low Next Nature Light Curry", price=1700.00, image_name="product-17", sizes="37 38 39 40 42", category="Nike"),
    Product(name="Dunk Low Mica Green", price=2400.00, image_name="product-19", sizes="37 38 39 40 42", category="Nike"),
    Product(name="Nike Hot Step Air Terra Drake NOCTA Violet Haze", price=2500.00, image_name="product-18", sizes="37 38 39 40 42", category="Nike"),
    Product(name="Dunk Low Disrupt 2 Multi-Color", price=2700.00, image_name="product-5", sizes="37 38 39 40 42", category="Nike"),
    Product(name="Dunk Low Chlorophyll", price=2600.00, image_name="product-6", sizes="37 38 39 40 42", category="Nike"),

    Product(name="Yeezy 450 Cloud White", price=3600.00, image_name="product-7", sizes="37 38 39 40 42", category="Yeezy"),
    Product(name="Yeezy 450 Dark Slate", price=4000.00, image_name="product-8", sizes="37 38 39 40 42", category="Yeezy"),
    Product(name="Yeezy Foam RNNR Clay Taupe", price=2600.00, image_name="product-10", sizes="37 38 39 40 42", category="Yeezy"),
    Product(name="Yeezy Boost 350 V2 Slate", price=4500.00, image_name="product-11", sizes="37 38 39 40 42", category="Yeezy"),
    Product(name="Yeezy Boost 350 V2 Hyperspace", price=4700.00, image_name="product-12", sizes="37 38 39 40 42", category="Yeezy"),
    Product(name="Adidas Yeezy 700 Analog", price=3500.00, image_name="product-14", sizes="37 38 39 40 42", category="Yeezy"),
    Product(name="Yeezy Boost 350 V2 Core Black Red", price=4800.00, image_name="product-16", sizes="37 38 39 40 42", category="Yeezy"),
    Product(name="Yeezy Boost 350 V2 MX Oate", price=3500.00, image_name="product-13", sizes="37 38 39 40 42", category="Yeezy"),
    Product(name="Yeezy 700 Wave Runner Solid Grey", price=6000.00, image_name="product-15", sizes="37 38 39 40 42", category="Yeezy"),
    Product(name="Yeezy Foam RNNR MX Brown Blue", price=2600.00, image_name="product-31", sizes="37 38 39 40 42", category="Yeezy"),

    Product(name="Air Jordan 1 High Dior", price=140000.00, image_name="product-22", sizes="37 38 39 40 42", category="Jordan"),
    Product(name="Air Jordan 1 Low Black White Diamond", price=2800.00, image_name="product-23", sizes="37 38 39 40 42", category="Jordan"),
    Product(name="Air Jordan 1 Low Travis Scott Reverse Mocha", price=18000.00, image_name="product-24", sizes="37 38 39 40 42", category="Jordan"),
    Product(name="Air Jordan 1 Low Washed Denim", price=2600.00, image_name="product-26", sizes="37 38 39 40 42", category="Jordan"),
    Product(name="Air Jordan 1 High Lucky Green", price=4900.00, image_name="product-25", sizes="37 38 39 40 42", category="Jordan"),
    Product(name="Air Jordan 4 Black Canvas", price=2400.00, image_name="product-27", sizes="37 38 39 40 42", category="Jordan"),
    Product(name="Air Jordan 1 Low Ice Blue Black", price=2400.00, image_name="product-29", sizes="37 38 39 40 42", category="Jordan"),
    Product(name="Air Jordan 1 Low Marina Blue", price=2500.00, image_name="product-32", sizes="37 38 39 40 42", category="Jordan"),
    Product(name="Air Jordan 1 Low Desert Berry", price=2700.00, image_name="product-30", sizes="37 38 39 40 42", category="Jordan"),
    Product(name="Air Jordan 1 Low Limelight", price=2400.00, image_name="product-33", sizes="37 38 39 40 42", category="Jordan")
]

Product.objects.bulk_create(products)
