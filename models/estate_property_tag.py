from odoo import _, api, fields, models, tools

class EstatePropertyTag (models.Model):

    _name = 'estate.property.tag'
    _description = 'Real estate property tags'

    name = fields.Char(string="Libellé", required=True)
