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
                                                  service_radius=int(row['service_radius']),
                                                  latitude=float(row['latitude']),
                                                  longitude=float(row['longitude']))
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
        try:
            obj, created = Product.objects.get_or_create(shop_id=Shop.objects.get(pk=int(row['shop_id'])),
                                                         category_id=Category.objects.get(pk=int(row['category_id'])),
                                                         title_fa=row['title_fa'])
            print(created)
        except:
            print(row)
        # quit()


def order():
    Order.objects.all().delete()
    csv_dict = csv.DictReader(open('orders.csv'))
    for row in csv_dict:
        # try:
            Order.objects.get_or_create(shop_id=Shop.objects.get(pk=int(row['shop_id'])),
                                        user_id=User.objects.get(pk=int(row['user_id'])),
                                        shop_product_id=Product.objects.get(pk=int(row['shop_product_id'])),
                                        rate=float(row['rate']))
            # print(created)
        # except:
        #     print(row)


# print(Shop.objects.get(""))
# shops()
# category()
# user()
# product()
order()
