from odoo import models, fields

class PartnerXlsx(models.AbstractModel):
    _name = 'report.rukosme.report_penyewaan_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_lap = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, penyewaan):
        sheet = workbook.add_worksheet('Daftar Penyewaan Kos')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        row = 1
        col = 0
        for obj in penyewaan:
            col = 0
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.tgl_bayar)
            sheet.write(row, col+2, obj.tgl_expired)
            sheet.write(row, col+3, obj.nama_penyewa)
            for xxx in obj.detailpenyewaan_ids:
                sheet.write(row, col+4, xxx.kamarkosmu)
                col += 1
            row += 1