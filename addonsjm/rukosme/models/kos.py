from odoo import models, fields, api

class kos(models.Model):
    _name='rukosme.kos'
    _description = 'New Description'

    kode_rukos = fields.Char('Kode Kos')
    name = fields.Char('Nama Kos')
    alamat = fields.Char('Alamat Kos')
    jml_lantai = fields.Integer('Jumlah Lantai')
    jml_kamar = fields.Integer('Jumlah Kamar')
    harga_sewa = fields.Integer(String='Harga Sewa')
    fasilitas = fields.Char(String='Fasilitas')
    stok = fields.Integer(string='Stok')

    tiperukos_ids= fields.Many2one(comodel_name='rukosme.tiperukos',
                                    string='Tipe Rukos',
                                    ondelete='cascade')
    
    # kamar_id = fields.One2many(comodel_name='rukosme.kamarkos',
    #                            inverse_name='kos_id',
    #                            string='Daftar Kamar')