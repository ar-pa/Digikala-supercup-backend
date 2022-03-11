from django.db import models
# from django.contrib.gis.db import models


class Category(models.Model):
    category_id = models.CharField(max_length=100)
    title_fa = models.CharField(max_length=100)
    background_color = models.CharField(max_length=100)


class User(models.Model):
    user_id = models.CharField(max_length=100)
    pass


class Shop(models.Model):
    name = models.CharField(max_length=100)

    has_available_products = models.BooleanField()
    # available_products_count
    is_open = models.BooleanField()
    rate = models.IntegerField()
    rate_count = models.IntegerField()

    # rate_tags, preparation_time, cart_close_limit,
    service_radius = models.IntegerField()
    # , service_radius_critical,
    # location = models.PointField()


class Product(models.Model):
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    # shop_prouct_id,
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    # , , brand_id,
    title_fa = models.CharField(max_length=100)
    # title_en = models.CharField(max_length=100)
    # , moderation_status, media, description, max_count_per_cart, price, discount, unit_price, vat, init_stock, remaining_stock


class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # user_address_id
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    shop_product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    # order_id, order_item_id, order_shipment_id, order_status, order_payable_price, order_discount, order_shipping_cost_total, order_checkout_status, order_item_quantity, order_item_payable_price, order_item_discount, order_shipment_status, order_shipment_delivery_status,
    rate = models.FloatField()
    # , tags
