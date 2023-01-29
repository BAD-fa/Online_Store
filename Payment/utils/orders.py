def check_items_available(items):
    if items:
        print(type(items))
        for item in items:
            if not item.is_available():
                item.count = 0
                item.is_valid = False

        items.bulk_update(items, ['count', 'is_valid'])
    return items


def update_price(items):
    items = check_items_available(items)
    total_price = 0
    if items:
        for item in items:
            price = item.get_price()
            print('price: ', price)
            total_price += item.get_price()
            print('total_price: ', total_price)
    return total_price


def check_order(order):
    try:
        items = order.order_items.all()
    except:
        items = None
        print('test failed 3')
    if items:
        order.orders_price = update_price(items)
        order.save()
        return order
