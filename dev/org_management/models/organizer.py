from odoo import api, fields, models
class Organizer(models.Model):
    _name = "management.organizer"
    _description = "Organizer information"

    name = fields.Char(string="Name", required=True)
    surname = fields.Char(string="Surname", required=True)
    second_name = fields.Char(string="Second name", required=False)
    is_adult = fields.Boolean(string="Is over 18?")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string="Gender")
    phone_number = fields.Char(string="Phone number")
    email = fields.Char(string="Email")
    # event_ids = fields.Many2many(comodel_name="management.event", relation="organizers_events_rel", column1="organizer_id", column2="event_id", string="Events")
