from odoo import _, api, fields, models, tools
from datetime import datetime
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):

    _name = 'estate.property'
    _description = 'Real estate property'

    def _default_date_availability(self):
        today = datetime.today()
        three_months_later = today + relativedelta(months=3)
        return three_months_later.date()

    name = fields.Char(string="Libellé", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Code postal")
    date_availability = fields.Date(string="Date availability", copy=False, default=_default_date_availability)
    expected_price = fields.Float(string="expected_price", required=True)
    selling_price = fields.Float(string="selling_price", readonly=True, copy=False)
    bedrooms = fields.Integer(string="Nombre de lits", default=2)
    living_area = fields.Integer(string="Salon")
    facades = fields.Integer(string="facades")
    garage = fields.Boolean(string="garage")
    garden = fields.Boolean(string="Jardin")
    garden_area = fields.Boolean(string="Superficie du jardin")
    active = fields.Boolean(string="Active", default=True)
    garden_orientation = fields.Selection(
        string="Orientation du jardin",
        selection=[('north', 'North'),('south', 'South'),('east', 'East'),('west', 'West')],
        help='Choisir l\'orientation du jardin'
    )
    state = fields.Selection(
        string="State",
        selection=[('new', 'New'), ('offer recieved', 'Offer Recieved'), ('offer accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')],
        help='Choisir le statut du bien',
        copy=False,
        default='new'
    )
    property_type_id = fields.Many2one(
        'estate.property.type',
        string='Property Type',
    )
    buyer_id = fields.Many2one("res.partner", string="Client", copy=False)
    seller_id = fields.Many2one("res.users", string="Vendeur", default=lambda self: self.env.user)
    tag_ids =  fields.Many2many("estate.property.tag", string="Étiquettes", copy=False)