from django.db import models
from django.utils.text import slugify


class ms_layanan(models.Model):
    layanan_name    = models.CharField(max_length=255, unique=True)
    created_by      = models.IntegerField()
    created_date    = models.DateTimeField(auto_now_add=True)
    updated_by      = models.IntegerField()
    updated_date    = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'ms_layanan'
    
    def __str__(self):
        return self.layanan_name

class ms_harga(models.Model):
    harga        = models.FloatField()
    created_by   = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_by   = models.IntegerField()
    updated_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'ms_harga'
    
    def __float__(self):
        return self.harga

class ms_menu(models.Model):
    menu_code       = models.CharField(max_length=255, unique=True)
    menu_name       = models.CharField(max_length=255)
    created_by      = models.IntegerField()
    created_date    = models.DateTimeField(auto_now_add=True)
    updated_by      = models.IntegerField()
    updated_date    = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'ms_menu'
    
    def __str__(self):
        return self.menu_code

class ms_komposisi(models.Model):
    menu_code       = models.ForeignKey(ms_menu, db_column='menu_code' ,to_field='menu_code', default=None, on_delete=models.CASCADE)
    komposisi_code  = models.CharField(max_length=255, unique=True)
    layanan_id      = models.ForeignKey(ms_layanan,db_column='layanan_id' , default=None, on_delete=models.CASCADE)
    harga_id        = models.ForeignKey(ms_harga, db_column='harga_id' , default=None, on_delete=models.CASCADE)
    created_by      = models.IntegerField()
    created_date    = models.DateTimeField(auto_now_add=True)
    updated_by      = models.IntegerField()
    updated_date    = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'ms_komposisi'
    
    def __str__(self):
        return self.komposisi_code

class ms_item(models.Model):
    item_code       = models.CharField(max_length=255, unique=True)
    item_name       = models.CharField(max_length=255, unique=False)
    unit            = models.CharField(max_length=255, unique=False)
    created_by      = models.IntegerField()
    created_date    = models.DateTimeField(auto_now_add=True)
    updated_by      = models.IntegerField()
    updated_date    = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'ms_item'
    
    def __str__(self):
        return self.item_name

class ms_komposisi_detail(models.Model):
    komposisi_code  = models.ForeignKey(ms_komposisi, db_column='komposisi_code' ,to_field='komposisi_code', default=None, on_delete=models.CASCADE)
    item_id         = models.ForeignKey(ms_item, db_column='item_id',default=None, on_delete=models.CASCADE)
    qty             = models.IntegerField()

    class Meta:
        db_table = 'ms_komposisi_detail'
    
    def __str__(self):
        return self.komposisi_code

class transaksi(models.Model):
    transaksi_code  = models.CharField(max_length=255, unique=True)
    customer_name   = models.CharField(max_length=255, unique=False)
    ppn_value     = models.FloatField()
    sub_value     = models.FloatField()
    pay_type        = models.CharField(max_length=255, unique=False)
    transaksi_date  = models.DateTimeField(auto_now_add=True)
    created_by      = models.IntegerField()
    updated_date    = models.DateTimeField(auto_now_add=True)
    updated_by      = models.IntegerField()

    class Meta:
        db_table = 'transaksi'
    
    def __str__(self):
        return self.transaksi_code

class transaksi_detail(models.Model):
    transaksi_code  = models.ForeignKey(transaksi, db_column='transaksi_code' , to_field='transaksi_code', default=None, on_delete=models.CASCADE)
    komposisi_code  = models.ForeignKey(ms_komposisi,db_column='komposisi_code', to_field='komposisi_code', default=None, on_delete=models.CASCADE)
    qty_porsi       = models.IntegerField()

    class Meta:
        db_table = 'transaksi_detail'
    
    def __str__(self):
        return self.transaksi_code