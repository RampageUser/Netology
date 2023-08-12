from rest_framework import serializers
from .models import Product, StockProduct, Stock

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']

class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        # создаем склад по его параметрам
        stock = super().create(validated_data)
        if positions:
            for value in positions:
                StockProduct.objects.create(product=value['product'], stock=stock,
                                            quantity=value['quantity'], price=value['price'])
        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)
        if positions:
            for position_data in positions:
                product = position_data['product']
                quantity = position_data['quantity']
                price = position_data['price']
                stock_product, _ = StockProduct.objects.update_or_create(
                    stock=stock,
                    product=product,
                    defaults={'quantity': quantity, 'price': price}
                )

        return stock
