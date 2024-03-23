from odoo import api, fields, models, _
class EventAppUser(models.Model):
    _inherit='res.users'
    event_ids = fields.Many2many(comodel_name="management.event", relation="organizers_events_rel",
                                 column1="organizer_id", column2="event_id", string="Events")
