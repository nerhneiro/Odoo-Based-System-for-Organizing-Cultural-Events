from odoo import api, fields, models, _
class EventAppUser(models.Model):
    _inherit='res.users'
    org_event_ids = fields.Many2many(comodel_name="management.event", relation="organizers_events_rel",
                                 column1="organizer_id", column2="event_id", string="Organizer Events")
    org_invited_ids = fields.One2many(comodel_name="management.organizer", inverse_name="user_id", string="Connected organizers")
    guest_event_ids = fields.One2many(comodel_name="management.guest", inverse_name="user_id", string="Connected guests")
    guest_usr_event_ids = fields.Many2many(comodel_name="management.event", relation="guests_events_rel", column1="guest_id", column2="event_id", string="Events I am guest at")
    speaker_usr_event_ids = fields.Many2many(comodel_name="management.event", relation="speakers_events_rel",
                                           column1="speaker_id", column2="event_id", string="Events I am speaker at")
    speaker_ids = fields.One2many(comodel_name="management.speaker", inverse_name="user_id",
                                  string="Connected speakers")
    vip_guest_usr_event_ids = fields.Many2many(comodel_name="management.event", relation="vip_guests_events_rel",
                                           column1="vip_guest_id", column2="event_id", string="Events I am VIP-guest at")
    vip_guest_event_ids = fields.One2many(comodel_name="management.vip_guest", inverse_name="user_id",
                                      string="Connected vip guests")