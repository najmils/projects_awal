from asyncio import constants
from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools.misc import unique

class penyewaan(models.Model):
    _name = 'rukosme.penyewaan'
    _description = 'Penyewaan'

    name = fields.Char(string='No. Nota')
    nama_penyewa = fields.Char(string='Nama Penyewa')
    tgl_bayar = fields.Datetime(
        string='Tanggal Deposit',
        default=fields.Datetime.now())
    tgl_expired = fields.Datetime(
        string='Tanggal Jatuh Tempo Berikutnya'
    )
    total_bayar = fields.Integer(
        string='Total Pembayaran',
        compute='_compute_totalbayar')
    detailpenyewaan_ids = fields.One2many(
        comodel_name='rukosme.detailpenyewaan',
        inverse_name='penyewaan_id',
        string='Detail Penyewaan')

    @api.depends('detailpenyewaan_ids')
    def _compute_totalbayar(self):
        for line in self:
            result = sum(self.env['rukosme.detailpenyewaan'].search(
                [('penyewaan_id', '=', line.id)]).mapped('subtotal'))
            line.total_bayar = result

    @api.ondelete(at_uninstall=False)
    def __ondelete_penyewaan(self):
        if self.detailpenyewaan_ids:
            penyewaan = []
            for line in self:
                penyewaan = self.env['rukosme.detailpenyewaan'].search(
                    [('penyewaan_id', '=', line.id)])
                print(penyewaan)

            for ob in penyewaan:
                print(ob.kamarkosmu.name + ' ' + str(ob.qty))
                ob.kamarkosmu.stok += ob.qty

    def unlink(self):
        if self.detailpenyewaan_ids:
            a=[]
            for rec in self:
                a = self.env['rukosme.detailpenyewaan'].search([('penyewaan_id', '=', rec.id)])
                print(a)
            
            for ob in a:
                print(str(ob.kamarkosmu.name) + ' ' + str(ob.qty))
                ob.kamarkosmu.stok += ob.qty
        
        record = super(penyewaan, self).unlink()
    
    def write(self, vals):
        for rec in self: 
            a = self.env['rukosme.detailpenyewaan'].search([('penyewaan_id', '=',rec.id)])
            print(a)
            for data in a:
                print(str(data.kamarkosmu.name)+' '+str(data.qty)+' '+str(data.kamarkosmu.stok))
                data.kamarkosmu.stok += data.qty
        record = super(penyewaan,self).write(vals)
        for rec in self: 
            b = self.env['rukosme.detailpenyewaan'].search([('penyewaan_id', '=',rec.id)])
            print(a)
            print(b)
            for dataBaru in b:
                if dataBaru in a:
                    print(str(dataBaru.kamarkosmu.name)+' '+str(dataBaru.qty)+' '+str(dataBaru.kamarkosmu.stok))
                    dataBaru.kamarkosmu.stok -= dataBaru.qty
        return record

    _sql_constraints = [
        ('no_nota_unik', 'unique(name)', 'Nomor nota tidak boleh sama!!')
    ]
    
    state = fields.Selection(
        string='Status',
        selection=[('draft', 'Draft'), ('confirm', 'Confirm'), ('done', 'Done'), ('canceled', 'Canceled')],
        required=True, readonly=True, default='draft')

    def action_confirm(self):
        self.write({'state': 'confirm'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_canceled(self):
        self.write({'state': 'canceled'})


class Detailpenyewaan(models.Model):
    _name = 'rukosme.detailpenyewaan'
    _description = 'Detail'

    penyewaan_id = fields.Many2one(
        comodel_name='rukosme.penyewaan',
        string='Detail penyewaan')
    kamarkosmu = fields.Many2one(
        comodel_name='rukosme.kos',
        string='List kos')
    harga_satuan = fields.Integer(
        string='Harga Satuan',
        onchange='_onchange_kamarkosmu')
    jml_jaminan = fields.Integer(
        string='Jumlah Deposit',
        onchange='_onchange_kamarkosmu')
    qty = fields.Integer(string='Jumlah Orang/Kamar')
    subtotal = fields.Integer(compute='_compute_subtotal', string='Subtotal')

    @api.depends('harga_satuan', 'qty', 'jml_jaminan')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.jml_jaminan + (line.qty * line.harga_satuan)

    @api.onchange('kamarkosmu')
    def _onchange_kamarkosmu(self):
        if self.kamarkosmu.harga_sewa:
            self.harga_satuan = self.kamarkosmu.harga_sewa

    @api.model
    def create(self, vals):
        line = super(Detailpenyewaan, self).create(vals)
        if line.qty:
            self.env['rukosme.kos'].search(
                [('id', '=', line.kamarkosmu.id)]
            ).write({'stok': line.kamarkosmu.stok - line.qty})

        return line
        
    @api.constrains('qty')
    def check_quantity(self):
        for rec in self:
            if rec.qty <1:
                raise ValidationError("Harus memasukkan minimal 1 penyewa pada {}".format(rec.kamarkosmu.name))
            elif (rec.qty > 2):
                raise ValidationError("1 kamar pada kos {} maksimal 2 orang!".format(rec.kamarkosmu.name))