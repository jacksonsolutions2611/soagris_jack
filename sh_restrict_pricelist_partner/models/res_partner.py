# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.
from odoo import fields, models


class ResPartnerPricelist(models.Model):
    _inherit = 'res.partner'

    pricelist_ids = fields.Many2many(
        "product.pricelist", string='Allowed Pricelists')
