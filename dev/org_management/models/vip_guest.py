from odoo import api, fields, models, _
class VIPguest(models.Model):
    _name = "management.vip_guest"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "VIP guest information"

    name = fields.Char(string="Name", required=True, tracking=True)
    surname = fields.Char(string="Surname", required=True, tracking=True)
    second_name = fields.Char(string="Second name", required=False, tracking=True)
    is_adult = fields.Boolean(string="Is over 18?", tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string="Gender", tracking=True)
    phone_number = fields.Char(string="Phone number", tracking=True)
    email = fields.Char(string="Email", tracking=True)
    passport = fields.Char(string="Passport info", tracking=True)
    visa = fields.Char(string="Visa info", tracking=True)
    country_id = fields.Many2one('res.country', 'Country', tracking=True)
    ref = fields.Char(string="Reference", default=lambda self: _('New'))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('management.vip_guest')
        return super(VIPguest, self).create(vals_list)
