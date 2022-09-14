import string
from odoo import api, fields, models
# Lanjutan 31 Aug 2022 sesi 2 (membuat file supplier.py dan membahas tentang many2many)
# dimana si supplier ini akan disambungkan dengan barang

class supplier(models.Model):
    _name = 'njm.supplier'
    _description = 'model.technical.name'
    
    name = fields.Char(string='Nama Perusahaan')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='No. Telepon')
    barang_id = fields.Many2many(comodel_name='njm.barang', string='Barang')

# lanjut membuat file supplier_view.xml dan ada tambahan juga di Barang.py