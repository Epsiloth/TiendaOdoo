from odoo import models, fields, api

class Articulos(models.Model):
    _name = 'pablotienda.articulos'
    nombre = fields.Char('Nombre', required=True)
    precio = fields.Integer('Precio', required=True)
    proveedor = fields.Many2one('pablotienda.proveedores', 'Proveedor', required=True)

    def name_get(self):
        res=[]
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res