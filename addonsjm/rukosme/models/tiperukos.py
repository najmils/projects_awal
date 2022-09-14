from odoo import api, fields, models


class tipeRukos(models.Model):
    _name = 'rukosme.tiperukos'
    _description = 'New Description'
    
    name = fields.Selection([
        ('executive', 'Executive'), 
        ('reguler', 'Reguler')
    ], string = 'Tipe Kos')
    kode_tipe = fields.Char(onchange='_compute_kode_tipe', string='Kode Tipe Kos')
    
    @api.onchange('name')
    def _compute_kode_tipe(self):
        if (self.name == 'executive'):
            self.kode_tipe = 'exc'
        elif (self.name == 'reguler'):
            self.kode_tipe = 'reg'
    
    rukos_ids = fields.One2many(comodel_name='rukosme.kos',
                                inverse_name='tiperukos_ids',
                                string='Daftar Kos')

    jml_kos = fields.Char(compute='_compute_jml_kos', string='Jumlah Kos')
    
    @api.depends('rukos_ids')
    def _compute_jml_kos(self):
        for rec in self:
            a = self.env['rukosme.kos'].search([('tiperukos_ids','=',rec.id)]).mapped('name')
            b = len(a)
            rec.jml_kos = b
            rec.daftar = a

    daftar = fields.Char('Daftar Isi')
    