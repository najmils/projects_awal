# 07 sept 2022 sesi 1

from odoo import models, fields, api

class barangDatang(models.TransientModel):
    _name = 'njm.barangdatang'
    #lanjut membuat securitnya!

    barang_id = fields.Many2one(
        comodel_name='njm.barang',
        string='Nama Barang',
        required=True
    )

    jumlah = fields.Integer(
        string='jumlah',
        required=False
    )

    def button_barang_datang(self):
        for line in self:
            self.env['njm.barang'].search([('id','=', line.barang_id)]).write(
                {'stok':line.barang_id.stok + line.jumlah}
            )