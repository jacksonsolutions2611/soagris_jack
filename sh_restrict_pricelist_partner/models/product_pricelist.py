# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.
from odoo import models, api


class PricelistInherit(models.Model):
    _inherit = 'product.pricelist'

    @api.model
    def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        if self.env.user.has_group('base.group_portal') and self.env.user.partner_id.pricelist_ids.ids:
            args.append(
                ('id', 'in', self.env.user.partner_id.pricelist_ids.ids))
        res = super(PricelistInherit, self)._search(args, offset=offset, limit=limit,
                                                    order=order, count=count, access_rights_uid=access_rights_uid)
        return res
