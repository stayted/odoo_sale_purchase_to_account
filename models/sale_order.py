# -*- coding: utf-8 -*-
# Al momento della creazione di una fattura:
#   prende sale_order.x_studio_incoterms e lo copia in account_move.x_da_incoterms


from odoo import models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _prepare_invoice(self):
        res = super()._prepare_invoice()
        res["x_studio_incoterms"] = self.x_studio_incoterms
        return res

    def _prepare_invoice_line(self, **optional_values):
        res = super()._prepare_invoice_line( optional_values )
        res["x_studio_da_n_pezzi"] = self.x_studio_da_n_pezzi
        return res
