from django.db import models


class Creator (models.Model):
        creator_id = models.AutoField(primary_key=True)
        creator_name = models.CharField(max_length=100, verbose_name='Производитель')
        creator_cnt = models.CharField(max_length=100, verbose_name='Страна')

        def __str__(self):
            return self.creator_name

        class Meta:
            verbose_name_plural = "Производители"
            verbose_name = "Производитель"


class Vcard(models.Model):
    id_card = models.AutoField(primary_key=True)
    card_creator = models.ForeignKey(Creator, on_delete=models.CASCADE, verbose_name='Производитель')
    card_name = models.CharField(max_length=45, verbose_name='Название видеокарты')
    photo = models.ImageField(null=True, blank=True, verbose_name='Фото')
    card_price = models.CharField(max_length=15, verbose_name='Цена')

    def __str__(self):
        return self.card_name

    class Meta:
        verbose_name_plural = "Видеокарта"
        verbose_name = "Видеокарта"

    def get_card_name(self):
        return [u.username for u in self.card_name.all()]
    get_card_name.short_description = 'Названия видеокарт'

    def get_card_creator(self):
        return [u.creator_name for u in self.card_creator.all()]
    get_card_creator.short_description = 'Производитель'

class Order(models.Model):
    id_order = models.AutoField(primary_key=True)
    code_order = models.CharField(max_length=45, verbose_name='Код регистрации')
    card_order = models.ManyToManyField(Vcard, verbose_name='Выбранная видеокарта')

    def __str__(self):
        return self.code_order

    class Meta:
        verbose_name_plural = "Заказы"
        verbose_name = "Заказ"

    def get_card_order(self):
        return [u.card_name for u in self.card_order.all()]
    get_card_order.short_description = 'Названия видеокарт'

class Human(models.Model):
    id_human = models.AutoField(primary_key=True)
    fio = models.CharField(max_length=100, blank=False, null=False, verbose_name='ФИО')
    order_code = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Код заказа')

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name_plural = "Пользователи"
        verbose_name = "Пользователь"

    def get_registr_code(self):
        return [r.code_registr for r in self.registr_code.all()]
    get_registr_code.short_description = 'Номера заказов'