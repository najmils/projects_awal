from asyncio import constants
from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools.misc import unique
# 01 Sept 2022 sesi 1

class penjualan(models.Model):
    _name = 'njm.penjualan'
    _description = 'Penjualan'

    name = fields.Char(string='No. Nota')
    nama_pembeli = fields.Char(string='Nama Pembeli')
    tgl_penjualan = fields.Datetime(
        string='Tanggal Transaksi',
        default=fields.Datetime.now())
    total_bayar = fields.Integer(
        string='Total Pembayaran',
        compute='_compute_totalbayar')
    detailpenjualan_ids = fields.One2many(
        comodel_name='njm.detailpenjualan',
        inverse_name='penjualan_id',
        string='Detail Penjualan')

    @api.depends('detailpenjualan_ids')
    # berfungsi gini, jadi nanti di tampilan odoo nya itu dia gabisa dipencet
    def _compute_totalbayar(self):
        for line in self:
            result = sum(self.env['njm.detailpenjualan'].search(
                [('penjualan_id', '=', line.id)]).mapped('subtotal'))
            line.total_bayar = result

    # 02 Sept 2022
    @api.ondelete(at_uninstall=False)
    def __ondelete_penjualan(self):
        if self.detailpenjualan_ids:
            penjualan = []
            for line in self:
                penjualan = self.env['njm.detailpenjualan'].search(
                    [('penjualan_id', '=', line.id)])
                print(penjualan)

            for ob in penjualan:
                print(ob.barang_id.name + ' ' + str(ob.qty))
                ob.barang_id.stok += ob.qty

    def unlink(self):
    # liat di localhostnya, kan ada kotak yg buat checklist itu di sebelah kiri nama, nah kalau 
    # kita pencet itu maka si unlink ini yg jalan
        if self.detailpenjualan_ids:
            a=[]
            for rec in self:
                a = self.env['njm.detailpenjualan'].search([('penjualan_id', '=', rec.id)])
                print(a)
            
            for ob in a:
                print(str(ob.barang_id.name) + ' ' + str(ob.qty))
                ob.barang_id.stok += ob.qty
        
        record = super(penjualan, self).unlink()
    # batas 02 Sept 2022

    # 05 Sept 2022 sesi 2
    # edit data penjualan pada nomor nota yg sama
    # kenapa ditambahin kode ini? biar kalau kita edit jumlah qty barang yg dibeli, 
    # maka akan berjalan normal (qty nya sesuai) tanpa error
    def write(self, vals):
        # kenapa pake vals? karena ada sesuatu yg disimpan. kalau link kenapa gaada vals? karna dia langsung hapus aja
        for rec in self: 
            a = self.env['njm.detailpenjualan'].search([('penjualan_id', '=',rec.id)])
                # self itu mencari sebuah object dari kelas detail penjualan
            print(a)
            for data in a:
                print(str(data.barang_id.name)+' '+str(data.qty)+' '+str(data.barang_id.stok))
                data.barang_id.stok += data.qty
        record = super(penjualan,self).write(vals)
        for rec in self: 
            b = self.env['njm.detailpenjualan'].search([('penjualan_id', '=',rec.id)])
                # self itu mencari sebuah object dari kelas detail penjualan
            print(a)
            print(b)
            for dataBaru in b:
                if dataBaru in a:
                    print(str(dataBaru.barang_id.name)+' '+str(dataBaru.qty)+' '+str(dataBaru.barang_id.stok))
                    dataBaru.barang_id.stok -= dataBaru.qty
        return record
        #05 Sept 2022 sesi 2 akhir

    #05 Sept 2022 sesi 1
    # contoh sql constraint
    _sql_constraints = [
        # struktur sql constrain
        # (<nama constants>, <constaintnya>, <pesan constraint>)
        # contohnya adalah nomor nota pada field yg ada pada transaksi penjualan
        ('no_nota_unik', 'unique(name)', 'Nomor nota tidak boleh sama!!')
        # bisa lebih dari 1 struktur, jadinya gini
        # ('no_nota_unik', 'unique(name)', 'Nomor nota tidak boleh sama!!') ,
        # (),(),()
    ]
    #05 Sept 2022 sesi 1 batas

    #12 Sept 2022
    state = fields.Selection(
        string='Status',
        selection=[('draft', 'Draft'), ('confirm', 'Confirm'), ('done', 'Done'), ('canceled', 'Canceled')],
        required=True, readonly=True, default='draft')

    def action_confirm(self):
        #berfungsi untuk mengubah draft menjadi sebuah confirm
        self.write({'state': 'confirm'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_canceled(self):
        self.write({'state': 'canceled'})
    #batas 12 Sept 2022, lanjut di penjualan_view.xml


class DetailPenjualan(models.Model):
    _name = 'njm.detailpenjualan'
    _description = 'Detail'

    name = fields.Char(string='Nama')
    penjualan_id = fields.Many2one(
        comodel_name='njm.penjualan',
        string='Detail Penjualan')
    barang_id = fields.Many2one(
        comodel_name='njm.barang',
        string='List Barang')
    harga_satuan = fields.Integer(
        string='Harga Satuan',
        onchange='_onchange_barang_id')
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Integer(compute='_compute_subtotal', string='Subtotal')

    @api.depends('harga_satuan', 'qty')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.qty * line.harga_satuan

    @api.onchange('barang_id')
    # nanti di odoo nya dia bisa dipencet, kebalikan dari depends
    def _onchange_barang_id(self):
        if self.barang_id.harga_jual:
            self.harga_satuan = self.barang_id.harga_jual

    # 02 Sept 2022, 1 sesi
    @api.model
    def create(self, vals):
    # pada sub menu penjualan kan ada tulisan "create" di sebelah kiri atas, nah nanti dia nih
    # yg jalan kalau si create nya itu dipencet
        line = super(DetailPenjualan, self).create(vals)
        if line.qty:
        # Mendapatkan data berdasarkan ID pada barang_id
            self.env['njm.barang'].search(
                [('id', '=', line.barang_id.id)]
            ).write({'stok': line.barang_id.stok - line.qty})

        return line

    #05 Sept 2022 sesi 1
    # python constrain
    @api.constrains('qty')
    def check_quantity(self):
        for rec in self:
            if rec.qty <1:
                raise ValidationError("Mau belanja {} berapa banyak sih..".format(rec.barang_id.name))
            elif (rec.barang_id.stok < rec.qty):
                raise ValidationError("Stok barang ini tidak mencukupi, hanya tersedia {} {}".format(rec.barang_id.stok,rec.barang_id.name))