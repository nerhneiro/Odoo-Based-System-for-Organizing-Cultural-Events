from odoo import api, fields, models, _
class Guest(models.Model):
    _name = "management.guest"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Guest information"

    name = fields.Char(string="Name", required=True, tracking=True)
    surname = fields.Char(string="Surname", required=True, tracking=True)
    second_name = fields.Char(string="Second name", required=False, tracking=True)
    is_adult = fields.Boolean(string="Is over 18?", tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string="Gender", tracking=True)
    phone_number = fields.Char(string="Phone number", tracking=True)
    email = fields.Char(string="Email", tracking=True)
    ref = fields.Char(string="Reference", default=lambda self: _('New'))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('management.guest')
        return super(Guest, self).create(vals_list)

    def action_send_invitation(self):
        template = self.env.ref('org_management.event_guest_invitation_template')
        for rec in self:
            if rec.email:
                template.send_mail(rec.id, force_send=True)
                self.message_post(body='Invitation sent')
