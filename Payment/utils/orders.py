def update_price(order):
    order.check_items_available()
    total_price = 0
    order_items = order.order_itmes.all()
    if order_items:
        for item in order_items:
            total_price += item.get_price()
        order.
    return order

def check_order(order):
    if order.order_itmes.all():
        order.check_items_available()
        order.update_price()
        order.save()

