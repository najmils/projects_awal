# 30 Aug 2022 sesi 2
# membuat model baru yaitu person
# melakukan inherit dari person, dimana person akan di-inherit oleh pegawai minimarketnya

from odoo import api, fields, models

class person(models.Model):
    _name = 'njm.person'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    tgl_lahir = fields.Datetime(string='Tanggal Lahir')

class kasir(models.Model):
    #kalau ada name, berarti butuh tabel baru
    #tanpa ada name, cuma ada inherit berarti ga perlu tabel baru 
    #tapi menambah kolom (field) dari kelas person (misalnya) dengan id_kasir (misalnya)
    _name = 'njm.kasir'
    _inherit = 'njm.person'
    _description = 'New Description'
    
    id_kasir = fields.Char('ID Kasir')

class cleaningService(models.Model):
    _name = 'njm.cleaningservice'
    _inherit = 'njm.person'
    _description = 'New Description'

    id_cln = fields.Char(string='ID Cleaning Service')
    
# batas 30-08-2022 sesi 2, ada lanjuatan pada file di security baris 4-6