from odoo import _, api, fields, models, tools

class EstatePropertyType (models.Model):

    _name = 'estate.property.type'
    _description = 'Real estate property type'

    name = fields.Char(string="Libellé", required=True)

