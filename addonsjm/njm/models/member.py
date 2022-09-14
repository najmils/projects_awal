from odoo import api, models, fields
# 31 Aug 2022 sesi 2

class konsumen(models.Model):
    _inherit = 'res.partner'
    _description = 'New Description'

    poin = fields.Integer(string='Poin')
    level = fields.Char(string='Level')