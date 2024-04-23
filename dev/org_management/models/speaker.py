from odoo import api, fields, models, _
class Speaker(models.Model):
    _name = "management.speaker"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Speaker information"

    name = fields.Char(string="Name*", required=True)
    surname = fields.Char(string="Surname*", required=True)
    second_name = fields.Char(string="Second name", required=False)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string="Gender")
    phone_number = fields.Char(string="Phone number")
    email = fields.Char(string="Email")
    speech_title = fields.Char(string="Speech title", required=True)
    speech_description = fields.Char(string="Speech description")
    user_id = fields.Many2one(comodel_name='res.users',
                              string='Connected User')
    event_id = fields.Many2one(comodel_name='management.event', string="Event")
    ref = fields.Char(string="Reference", default=lambda self: _('New'))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('management.speaker')
        return super(Speaker, self).create(vals_list)

    def action_send_invitation(self):
        template = self.env.ref('org_management.event_speaker_invitation_template')
        for rec in self:
            if rec.email:
                template.send_mail(rec.id, force_send=True)
                self.message_post(body='Invitation sent')


