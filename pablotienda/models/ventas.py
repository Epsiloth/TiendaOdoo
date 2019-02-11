from odoo import models, fields, api

class Ventas(models.Model):
    _name = 'pablotienda.ventas'
    articulo = fields.Many2one('pablotienda.articulos', 'Artículo', required=True)
    cliente = fields.Many2one('pablotienda.clientes', 'Cliente', required=True)
    cantidad = fields.Integer('Cantidad', required=True)
    total = fields.Integer('Total', compute='CalculaTotal')

    def CalculaTotal(self):
        self.total = self.articulo.precio * self.cantidad