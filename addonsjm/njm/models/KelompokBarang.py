from odoo import api, fields, models


class KelompokBarang(models.Model):
    _name = 'njm.kelompokbarang'
    _description = 'New Description'

    # Perubahan pada tanggal 30-08-2022
    name = fields.Selection([
        ('makananbasah', 'Makanan Basah'), 
        ('makanankering', 'Makanan Kering'),
        ('minuman','Minuman')
    ], string = 'Nama Kelompok')
    kode_kelompok = fields.Char(onchange='_compute_kode_kelompok', string='Kode Kelompok')
    
    @api.onchange('name')
    def _compute_kode_kelompok(self):
        if (self.name == 'makananbasah'):
            self.kode_kelompok = 'mak01'
        elif (self.name == 'makanankering'):
            self.kode_kelompok = 'mak02'
        elif (self.name == 'minuman'):
            self.kode_kelompok = 'min'
    # batas perubahan tanggal 30-08-2022
    
    kode_rak = fields.Char(string='Kode Rak')
    # Perubahannya di sini
    barang_ids = fields.One2many(comodel_name='njm.barang',
                                inverse_name='kelompokbarang_id',
                                string='Daftar Barang')
    
    # Perubahan pada tanggal 30-08-2022 
    # (menghitung jumlah barang dari variabel barang_ids)
    jml_item = fields.Char(compute='_compute_jml_item', string='Jumlah Item')
    
    @api.depends('barang_ids')
    def _compute_jml_item(self):
        for rec in self:
            a = self.env['njm.barang'].search([('kelompokbarang_id','=',rec.id)]).mapped('name')
            b = len(a)
            rec.jml_item = b
            rec.daftar = a

    daftar = fields.Char('Daftar Isi')
    # Akhir pDrubah Isian pada tanggal 30-08-2022 