from odoo import api, fields, models
class Event(models.Model):
    _name = "management.event"

    _description = "Event information"

    name = fields.Char(string="Name", required=True)
    place = fields.Char(string="Place")
    start = fields.Datetime(string="Start")
    number_of_guests = fields.Integer(string="Number of guests")
    duration = fields.Float(string="Duration")
    address = fields.Char(string="Address")