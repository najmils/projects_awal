from odoo import api, fields, models


class kamarKos(models.Model):
    _name = 'rukosme.kamarkos'
    _description = 'New Description'

    name = fields.Char(string='Nama Kamar')
    id_kamar = fields.Char(String='ID Kamar')
    # kos_id = fields.Many2one(comodel_name='rukosme.kos',
    #                                    string='List Kos',
    #                                    ondelete='cascade')