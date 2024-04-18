from odoo import api, fields, models, _
class EventAppUser(models.Model):
    _inherit='res.users'
    org_event_ids = fields.Many2many(comodel_name="management.event", relation="organizers_events_rel",
                                 column1="organizer_id", column2="event_id", string="Organizer Events")
    guest_event_ids = fields.One2many(comodel_name="management.guest", inverse_name="user_id", string="Connected guests")
    guest_usr_event_ids = fields.Many2many(comodel_name="management.event", relation="guests_events_rel", column1="guest_id", column2="event_id", string="Events")
    vip_guest_event_ids = fields.One2many(comodel_name="management.vip_guest", inverse_name="user_id",
                                      string="Connected vip guests")
    speaker_ids = fields.One2many(comodel_name="management.speaker", inverse_name="user_id",
                                      string="Connected speakers")