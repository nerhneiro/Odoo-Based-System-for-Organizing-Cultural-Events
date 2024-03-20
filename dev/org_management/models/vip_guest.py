from odoo import api, fields, models, _
class VIPguest(models.Model):
    _name = "management.vip_guest"

    _description = "VIP guest information"

    name = fields.Char(string="Name", required=True)
    surname = fields.Char(string="Surname", required=True)
    second_name = fields.Char(string="Second name", required=False)
    is_adult = fields.Boolean(string="Is over 18?")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string="Gender")
    phone_number = fields.Char(string="Phone number")
    email = fields.Char(string="Email")
    passport = fields.Char(string="Passport info")
    visa = fields.Char(string="Visa info")
    country_id = fields.Many2one('res.country', 'Country')
    ref = fields.Char(string="Reference", default=lambda self: _('New'))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('management.vip_guest')
        return super(VIPguest, self).create(vals_list)
