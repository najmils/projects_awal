from odoo import api, models, fields
# lanjutan 31 Aug 2022 sesi 1

class konsumen(models.Model):
    _inherit = 'res.partner'
    _description = 'New Description'
    # kalau pake primary, maka akan mengganti nama field atau mengubah view atau tampilan. ini tuh ga diizinkan di odoo 15
    # karna gabole pake primary, maka gunakan extension. view dari res.partner nya ga berubah cuma di konsumen_view nya aja yg berubah (bisa diliat di file konsumen_view.xml)
    # pokonya kalau pake model dari odoo nya itu ga bisa pake primary, jadi pakein extension aja di bagian mode nya

    poin = fields.Integer(string='Poin')
    
# dilanjut tambahin ke _init_.py nya (baris ke-7)
# trus lanjut lagi ke file konsumen_view.xml di folder views