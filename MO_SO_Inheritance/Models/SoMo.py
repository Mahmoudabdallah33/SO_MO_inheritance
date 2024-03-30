from odoo import api, models, fields


class ManufacturingInheritance(models.Model):
    _inherit = ['mrp.production']

    origin = fields.Many2one(comodel_name='sale.order', string="Source")

    sales_order_customer = fields.Char(related="origin.partner_id.name", string="Customer", readonly=True)

