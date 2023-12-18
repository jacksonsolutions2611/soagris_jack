# -*- coding: utf-8 -*-
from odoo import fields, models, _, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    imported_price_extra = fields.Float(string='Imported Price Extra')

    def _compute_product_price_extra(self):
        for product in self:
            product.price_extra = product.imported_price_extra


# class ProductTemplate(models.Model):
#     _inherit = 'product.template'

    # def _get_combination_info(self, combination=False, product_id=False, add_qty=1, pricelist=False,
    #                           parent_combination=False, only_template=False):
    #     values = super()._get_combination_info(combination=combination, product_id=product_id, add_qty=add_qty,
    #                                            pricelist=False, parent_combination=parent_combination,
    #                                            only_template=only_template)
        # if values['product_id']:
        #     product_id = self.env['product.product'].browse(values['product_id'])
        #     values['price_extra'] = product_id.price_extra
        # print("\n\n\n values----~~~~~~--", values)
        # return values
