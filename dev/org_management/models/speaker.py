from odoo import api, fields, models
class Speaker(models.Model):
    _name = "management.speaker"

    _description = "Speaker information"

    name = fields.Char(string="Name", required=True)
    surname = fields.Char(string="Surname", required=True)
    second_name = fields.Char(string="Second name", required=False)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string="Gender")
    phone_number = fields.Char(string="Phone number")
    email = fields.Char(string="Email")
    speech_title = fields.Char(string="Speech title", required=True)
    speech_description = fields.Char(string="Speech description")


