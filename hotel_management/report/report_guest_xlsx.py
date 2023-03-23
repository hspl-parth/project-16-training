from odoo import models, fields, api

class HotelGuestXlsx(models.AbstractModel):
    _name = 'report.hotel_management.report_hotel_guest_detail_xlsx'
    _inherit = "report.report_xlsx.abstract"
    _description = 'Excel report of hotel guest'

    def generate_xlsx_report(self, workbook, data, guests):
        sheet = workbook.add_worksheet('Guest Details')
        format1 = workbook.add_format({"bold": True, 'align': 'center', 'valign' : 'center' , 'bg_color': 'cyan', 'font_size': '14'})
        bold = workbook.add_format({"bold": True, 'align': 'center', 'text_wrap' : True})
        sheet.write_comment(1, 2, 'Hotel Guests')
        sheet.merge_range(1, 1, 2, 1, '')
        sheet.merge_range(1, 2, 2, 2, '')
        sheet.merge_range(1, 3, 2, 3, '')
        sheet.merge_range(1, 4, 2, 4, '')
        sheet.merge_range(1, 5, 2, 5, '')
        sheet.freeze_panes(3, 0)
        sheet.set_tab_color('red')
        raw = 1
        col = 1
        srno = 1
        sheet.set_column('D:E', 13)
        sheet.set_column('C:C', 18)

        headers = ['Sr.No', 'Name', 'Referance', 'Birthdate', 'Age']
        for header in headers:
            sheet.write(raw, col, header, format1)
            col += 1

        raw = 3
        col = 1
        for rec in guests:
            values = [srno, rec.name, rec.reference, rec.dob, rec.age[0:8]]
            for val in values:
                sheet.write(raw, col, val, bold)
                col += 1
            # print('\n\n', col)
            col = 1
            srno += 1
            raw += 1


