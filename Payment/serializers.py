from rest_framework import serializers
from .models import Order, OrderSend, OrderItem, Gateway, Payment
from User.serializers import UserSerializer


class OrderSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField(read_only=True, default=1)
    payment_type = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['status', 'tracking_code', 'orders_price', 'payment_type', 'created_time',
                  'modified_time']

    def get_status(self, obj):
        return obj.get_status_display()

    def get_payment_type(self, obj):
        return obj.get_payment_type_display()

    def create(self, validated_data):
        user = self.data['request'].user
        Order.objects.create(user=user, **validated_data)


class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer(write_only=True)
    price = serializers.SerializerMethodField()

    # product = ProductSerializer()

    class Meta:
        model = OrderItem()
        fields = ['order', 'product', 'expire_time', 'count', 'price', 'created_time', 'modified_time']
        # extra_kwargs = {
        #     'order': {'write_only': True}}

    def get_price(self, obj):
        return obj.get_price()

    def validate(self, data):
        if data['count'] > data['product'].stock:
            raise serializers.ValidationError('product is not exist')
        return super(OrderItemSerializer, self).validate(data)


class OrderSendSerializer(serializers.ModelSerializer):
    order = OrderSerializer(write_only=True)
    post_type = serializers.SerializerMethodField()

    class Meta:
        model = OrderSend
        fields = ['order', 'post_type', 'recipient_first_name', 'recipient_last_name', 'recipient_phone_number',
                  'address', 'send_cost', 'created_time', 'modified_time', 'tracking_code']

    def get_post_type(self, obj):
        return obj.get_post_type_display()


class OrderSendCreateSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())

    class Meta:
        model = OrderSend
        fields = ['order', 'post_type', 'recipient_first_name', 'recipient_last_name', 'recipient_phone_number',
                  'address', 'send_cost', 'tracking_code']


class OrderViewSerializer(OrderSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['status', 'tracking_code', 'orders_price', 'payment_type', 'created_time',
                  'modified_time', 'order_items']


class OrderAllDetailSerializer(OrderSerializer):
    order_send = OrderSendSerializer()
    order_items = OrderItemSerializer(many=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['user', 'status', 'tracking_code', 'orders_price', 'payment_type', 'created_time',
                  'modified_time', 'order_items', 'order_send']


class GetewaySerialzier(serializers.ModelSerializer):
    class Meta:
        model = Gateway
        field = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gateway
        field = '__all__'
