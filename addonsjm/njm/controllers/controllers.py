# 06 Sept 2022 sesi 2

from odoo import http, models, fields
from odoo.http import request
import json

class njmMart(http.Controller):
    @http.route('/njm/getbarang', auth='public', method=['GET'])
    # kode di bawah ini berdasarkan isi di barang.py yg ada di folder model
    def getBarang(self, **kw):
        barang = request.env['njm.barang'].search([])
        isi = []
        for bb in barang:
            isi.append({
                'nama_barang' : bb.name,
                'harga_jual' : bb.harga_jual,
                'stok' : bb.stok
            })
        return json.dumps(isi)

    @http.route('/njm/getsupplier', auth='public', method=['GET'])
    def getSupplier(self,**kw):
        supplier = request.env['njm.supplier'].search([supplier])
        sup = []
        for s in supplier:
            sup.append({
                'nama_perusahaan' : s.name,
                'alamat' : s.alamat,
                'no_telepon' : s.no_telp,
                'barang' : s.barang_id[0].name
            })
        return json.dumps(sup)