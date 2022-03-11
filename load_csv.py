import csv

from dk.models import Product, Shop, Category, User, Order


def shops():
    Shop.objects.all().delete()
    csv_dict = csv.DictReader(open('shops.csv'))
    for row in csv_dict:
        obj, created = Shop.objects.get_or_create(name=row['name'],
                                                  has_available_products=bool(row['has_available_products']),
                                                  is_open=bool(row['is_open']),
                                                  rate=float(row['rate']),
                                                  rate_count=int(row['rate_count']),
                                                  service_radius=int(row['service_radius'])
                                                  )
        obj.id = int(row['shop_id'])
        obj.save()
        print(created)


def category():
    Category.objects.all().delete()
    csv_dict = csv.DictReader(open('categories.csv'))
    for row in csv_dict:
        try:
            obj, created = Category.objects.get_or_create(category_id=int(row['id']), title_fa=row['title_fa'],
                                                          background_color=row['background_color'])
            obj.id = int(row['id'])
            obj.save()
            print(created)
        except:
            pass


def user():
    User.objects.all().delete()
    csv_dict = csv.DictReader(open('users.csv'))
    for row in csv_dict:
        try:
            obj, created = User.objects.get_or_create(user_id=int(row['id']))
            obj.id = int(row['id'])
            obj.save()
            print(created)
        except:
            print(row)
            # quit()


def product():
    Product.objects.all().delete()
    csv_dict = csv.DictReader(open('products.csv'))
    for row in csv_dict:
        obj, created = Product.objects.get_or_create(shop_id=int(row['shop_id']),
                                                     category_id=int(row['category_id']),
                                                     title_fa=row['title_fa'])
        print(created)


def order():
    Order.objects.all().delete()
    csv_dict = csv.DictReader(open('orders.csv'))
    for row in csv_dict:
        obj, created = Order.objects.get_or_create(shop_id=int(row['shop_id']),
                                                   user_id=int(row['user_id']),
                                                   shop_product_id=int(row['shop_product_id']),
                                                   rate=float(row['rate']))
        print(created)


# shops()
# category()
user()
product()
order()
