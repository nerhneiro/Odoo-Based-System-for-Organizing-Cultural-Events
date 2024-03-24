from odoo import api, fields, models, _
class EventAppUser(models.Model):
    _inherit='res.users'
    org_event_ids = fields.Many2many(comodel_name="management.event", relation="organizers_events_rel",
                                 column1="organizer_id", column2="event_id", string="Organizer Events")
    guest_event_ids = fields.One2many(comodel_name="management.guest", inverse_name="user_id", string="Connected guests")