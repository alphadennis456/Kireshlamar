from odoo import models, fields

class PendingPayment(models.Model):
    _name = 'hybrid.bar.pending'
    _description = 'Pending Payments for Bar'

    customer_name = fields.Char(string='Customer Name')
    amount = fields.Float(string='Amount')
    assigned_products = fields.Many2many('product.product', string='Products')
    state = fields.Selection([
        ('pending', 'Pending'),
        ('assigned', 'Assigned'),
        ('completed', 'Completed')
    ], default='pending')

    def assign_products(self):
        for record in self:
            record.state = 'assigned'
