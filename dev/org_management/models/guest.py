from odoo import api, fields, models, _
class Guest(models.Model):
    _name = "management.guest"

    _description = "Guest information"

    name = fields.Char(string="Name", required=True)
    surname = fields.Char(string="Surname", required=True)
    second_name = fields.Char(string="Second name", required=False)
    is_adult = fields.Boolean(string="Is over 18?")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string="Gender")
    phone_number = fields.Char(string="Phone number")
    email = fields.Char(string="Email")
    ref = fields.Char(string="Reference", default=lambda self: _('New'))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('management.guest')
        return super(Guest, self).create(vals_list)
