from odoo import models, fields, api
import datetime

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Real Estate Property'

    ##########
    # FIELDS #
    ##########

    name = fields.Char(
        string='Title', 
        required=True)
    
    description = fields.Text(
        string='Description')
    
    postcode = fields.Char(
        string='Postcode')
    
    date_availability = fields.Date(
        string='Available From', 
        copy=False, 
        compute='_compute_date_availability', 
        store=True)
    
    expected_price = fields.Float(
        string='Expected Price', 
        required=True)
    
    selling_price = fields.Float(
        string='Selling Price', 
        readonly=True, copy=False)
    
    bedrooms = fields.Integer(
        string='Bedrooms', 
        default=2)
    
    living_area = fields.Integer(
        string='Living Area')
    
    facades = fields.Integer(
        string='Facades')
    
    garage = fields.Boolean(
        string='Garage')
    
    garden = fields.Boolean(
        string='Garden')
    
    garden_area = fields.Integer(
        string='Garden Area')
    
    garden_orientation = fields.Selection(
        [('north', 'North'), 
         ('south', 'South'), 
         ('east', 'East'), 
         ('west', 'West')], 
         string='Garden Orientation')
    
    active = fields.Boolean(
        string='Active', 
        default=True)
    
    state = fields.Selection(
        [('new', 'New'), 
         ('offer_received', 'Offer Received'), 
         ('offer_accepted', 'Offer Accepted'),
         ('sold', 'Sold'), 
         ('canceled', 'Canceled')], 
         string='Status', 
         default='new')
    
    estate_property_type_id = fields.Many2one(
        comodel_name = 'estate.property.type', 
        string='Property Type')
    
    buyer_id = fields.Many2one(
        comodel_name = 'res.partner', 
        string='Buyer', 
        copy=False)
    
    salesperson_id = fields.Many2one(
        comodel_name = 'res.users', 
        string='Salesperson')
    
    offer_ids = fields.One2many(
        comodel_name = 'estate.property.offer', 
        inverse_name='property_id', 
        string='Offers')

    ###########
    # METHODS #
    ###########

    def _compute_date_availability(self):
        value = datetime.date.today() + datetime.timedelta(days=90)
        for record in self:
            if record.date_availability:
                # Aproximadamente 3 meses a partir da data atual.
                record.write({'date_availability': value})