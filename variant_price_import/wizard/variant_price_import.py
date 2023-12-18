# -*- coding: utf-8 -*-
from odoo import fields, models, _, api
import tempfile
from odoo.exceptions import UserError
import binascii
import logging
_logger = logging.getLogger(__name__)
try:
    import xlrd
except ImportError:
    _logger.debug('Cannot `import xlrd`.')


class VariantPriceImport(models.Model):
    _name = 'variant.price.import'

    data = fields.Binary(string='File')

    def import_variant_price(self):
        print("\n\n\n import_variant_price")
        try:
            fp = tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx")
            fp.write(binascii.a2b_base64(self.data))
            fp.seek(0)
            values = {}
            workbook = xlrd.open_workbook(fp.name)
            sheet = workbook.sheet_by_index(0)
        except:
            raise UserError(_("Invalid file!"))

        for row_no in range(sheet.nrows):
            if row_no <= 0:
                fields = map(lambda row: row.value.encode('utf-8'), sheet.row(row_no))
            else:
                line = list(map(
                    lambda row: isinstance(row.value, bytes) and row.value.encode('utf-8') or str(
                        row.value), sheet.row(row_no)))
                print("\n\n\n line----", line)
                if line[1]:
                    product = self.env['product.product'].search([('barcode', '=', line[1])], limit=1)
                    if product:
                        product.write({'imported_price_extra': float(line[2]) or 0.0})

