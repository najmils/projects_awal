from odoo import api, fields, models
# mulai 01 Sept sesi 1

class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'New Description'

    is_konsumen = fields.Boolean(string='Is Konsumen')
    is_direksi = fields.Boolean(string='Is Direksi')
    poin = fields.Integer(string='Poin')
    level = fields.Char(string='Level')

# jangan lupa tambahkan file ini ke _init_.py