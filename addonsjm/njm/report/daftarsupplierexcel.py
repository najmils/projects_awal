from odoo import models, fields

# 06 sept 2022 sesi 1
# diambil dai website https://apps.odoo.com/apps/modules/15.0/report_xlsx/
class PartnerXlsx(models.AbstractModel):
    # format name ditulis dalam bentuk: 'report.module_name.report_name'
    _name = 'report.njm.report_supplier_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_lap = fields.Date.today()

    # kalau kaya gini, berarti bakalan 1 1 gitu diprintnya
    # def generate_xlsx_report(self, workbook, data, supplier):
    #    for obj in supplier:
    #        report_name = obj.name
    #        sheet = workbook.add_worksheet(report_name[:31])
    #        bold = workbook.add_format({'bold': True})
    #        # formatnya gini sheet.write(role, column, obj.nama_objek), ini buat nampilin di excelnya
    #        sheet.write(2, 0, obj.name)

    def generate_xlsx_report(self, workbook, data, supplier):
        sheet = workbook.add_worksheet('Daftar Supplier')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        row = 1
        col = 0
        for obj in supplier:
            col = 0
            # formatnya gini sheet.write(role, column, obj.nama_objek), ini buat nampilin di excelnya
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.alamat)
            sheet.write(row, col+2, obj.no_telp)
            for xxx in obj.barang_id:
                sheet.write(row, col+3, xxx.name)
                col += 1
            row += 1

# sesi 2 lanjut di folder controller > file controllers.py