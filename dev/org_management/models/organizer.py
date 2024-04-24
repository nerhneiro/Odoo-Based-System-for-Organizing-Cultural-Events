from odoo import api, fields, models
class Organizer(models.Model):
    _name = "management.organizer"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Organizer information"

    name = fields.Char(string="Name*", required=True)
    surname = fields.Char(string="Surname*", required=True)
    second_name = fields.Char(string="Second name", required=False)
    is_adult = fields.Boolean(string="Is over 18?")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string="Gender")
    phone_number = fields.Char(string="Phone number")
    email = fields.Char(string="Email")
    user_id = fields.Many2one(comodel_name='res.users',
                              string='Connected User')
    event_id = fields.Many2one(comodel_name='management.event', string="Event")
    # domain = lambda self: [("groups_id", "=",self.env.ref("org_management.group_event_organizer").id)]
    # event_ids = fields.Many2many(comodel_name="management.event", relation="organizers_events_rel", column1="organizer_id", column2="event_id", string="Events")

    @api.onchange('event_id')
    def only_my_events(self):
        uid = self.env.user.id
        for rec in self:
            return {'domain': {'event_id': [('organizer_ids', 'in', [uid])]}}

    def action_send_invitation(self):
        print("Here ")
        template = self.env.ref('org_management.event_organizer_invitation_template')
        for rec in self:
            if rec.email:
                template.send_mail(rec.id, force_send=True)
                self.message_post(body='Invitation sent')
