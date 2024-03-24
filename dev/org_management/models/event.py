from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class Event(models.Model):
    _name = "management.event"
    _inherit = 'mail.thread'
    _description = "Event information"

    name = fields.Char(string="Name", required=True)
    place = fields.Char(string="Place", tracking=True)
    start = fields.Datetime(string="Start", tracking=True)
    number_of_guests = fields.Integer(string="Number of guests", tracking=True)
    duration = fields.Float(string="Duration", tracking=True)
    address = fields.Char(string="Address", tracking=True)
    organizer_ids = fields.Many2many('res.users', relation="organizers_events_rel",
                                     column1="event_id", column2="organizer_id", string="Organizers",
                                     domain=lambda self: [("groups_id", "=",
                                                           self.env.ref("org_management.group_event_organizer").id)])
    guest_ids = fields.One2many(comodel_name='management.guest', inverse_name="event_id", string="Guests")
                                # domain=lambda self: [("groups_id", "=",
                                #                       self.env.ref("org_management.group_event_guest").id)])

    @api.constrains('place', 'address')
    def _check_adress(self):
        for rec in self:
            if (rec.place and not rec.address):
                raise ValidationError(_("Address has to be recorded"))
