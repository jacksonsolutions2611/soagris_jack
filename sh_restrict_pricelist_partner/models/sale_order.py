# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.
from odoo import fields, models, api


class SalePricelist(models.Model):
    _inherit = 'sale.order'

    partner_pricelist_ids = fields.Many2many(
        "product.pricelist", compute='_compute_partner_pricelist_ids')

    pricelist_id = fields.Many2one(
        "product.pricelist", string='Pricelist', check_company=True,  # Unrequired company
        required=True, readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        domain="[('id', 'in', partner_pricelist_ids),'|',('company_id', '=', False), ('company_id', '=', company_id)]",
        help="If you change the pricelist, only newly added lines will be affected.")

    @api.depends('partner_id')
    def _compute_partner_pricelist_ids(self):
        for rec in self:
            if rec.partner_id and rec.partner_id.pricelist_ids:
                rec.partner_pricelist_ids = rec.partner_id.pricelist_ids
            else:
                rec.partner_pricelist_ids = self.env['product.pricelist'].search([
                ])
