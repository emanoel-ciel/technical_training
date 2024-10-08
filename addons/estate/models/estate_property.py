from odoo import models, fields, api


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Real Estate Property'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Available From', copy=False, compute='_compute_date_availability', store=True)
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(string='Selling Price', readonly=True, copy=False)
    bedrooms = fields.Integer(string='Bedrooms', default=2)
    living_area = fields.Integer(string='Living Area')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area')
    garden_orientation = fields.Selection(
        [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        string='Garden Orientation')
    active = fields.Boolean(string='Active', default=True)
    state = fields.Selection(
        [('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'),
         ('sold', 'Sold'), ('canceled', 'Canceled')],
        string='Status', default='new')
    estate_property_type_id = fields.Many2one('estate.property.type', string='Property Type')





    @api.onchange('date_availability')
    def _compute_date_availability(self):
        toDay = fields.Date.today()
        three_months_later = fields.Date.add(toDay, months=3)

        for record in self:
            if record.date_availability:
                record.date_availability = three_months_later