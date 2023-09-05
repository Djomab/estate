from odoo import _, api, fields, models, tools

class EstatePropertyOffer(models.Model):

    _name = 'estate.property.offer'
    _description = 'Real estate property offer'

    price = fields.Float(string="Prix")
    status = fields.Selection(string="Statut", copy=False,  selection=[('accepted', 'Accepted'),('refused', 'Refused')])
    partner_id = fields.Many2one('res.partner', string='partner', required=True)
    property_id = fields.Many2one('estate.property', string='Propriété', required=True)

