from odoo import api, fields, models


class Barang(models.Model):
    _name = 'njm.barang'
    _description = 'New Description'

    name = fields.Char(string='Nama Barang')
    harga_beli = fields.Integer(string='Harga Modal',required=True)
    harga_jual = fields.Integer(string='Harga Jual',required=True)
    # Perubahannya ada di sini
    kelompokbarang_id = fields.Many2one(comodel_name='njm.kelompokbarang',
                                        string='Kelompok Barang',
                                        #31 Aug 2022 sesi 2
                                        ondelete='cascade')
    supplier_id = fields.Many2many(comodel_name='njm.supplier', string='Supplier')
    
    # 01 Sept 2022 sesi 2
    stok = fields.Integer(string='Stok')