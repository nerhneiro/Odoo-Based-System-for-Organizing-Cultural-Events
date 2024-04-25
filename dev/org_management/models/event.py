from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
class Event(models.Model):
    _name = "management.event"
    _inherit = 'mail.thread'
    _description = "Event information"

    name = fields.Char(string="Name*", required=True)
    place = fields.Char(string="Place*", tracking=True)
    description = fields.Char(string="Description", tracking=True)
    start = fields.Datetime(string="Start*", required=True, tracking=True)
    end = fields.Datetime(string="End*", required=True, tracking=True)
    attachment_id = fields.Many2one('ir.attachment', string="Additional information in file", required=False)
    number_of_guests = fields.Integer(string="Max number of guests", tracking=True)
    # duration = fields.Float(string="Duration", tracking=True)
    address = fields.Char(string="Address*", tracking=True)
    organizer_ids = fields.Many2many('res.users', relation="organizers_events_rel",
                                     column1="event_id", column2="organizer_id", string="Organizers",
                                     domain=lambda self: [("groups_id", "=",
                                                           self.env.ref("org_management.group_event_organizer").id)])
    guest_ids = fields.One2many(comodel_name='management.guest', inverse_name="event_id", string="Guests")
    org_ids = fields.One2many(comodel_name='management.organizer', inverse_name="event_id", string="Organizers")
                                # domain=lambda self: [("user_id.groups_id", "=",
                                #                       self.env.ref("org_management.group_event_guest").id)])
    guest_user_ids = fields.Many2many('res.users', relation="guests_events_rel",
                                     column1="event_id", column2="guest_id", string="Guests Attend")
    vip_guest_user_ids = fields.Many2many('res.users', relation="vip_guests_events_rel",
                                      column1="event_id", column2="vip_guest_id", string="VIP Guests Attend")
    speaker_user_ids = fields.Many2many('res.users', relation="speakers_events_rel",
                                          column1="event_id", column2="speaker_id", string="Speakers Attend")
    speaker_ids = fields.One2many(comodel_name='management.speaker', inverse_name="event_id", string="Speakers")
    vip_guest_ids = fields.One2many(comodel_name='management.vip_guest', inverse_name="event_id", string="VIP guests")
    meeting_url = fields.Char(string="link")
    surveys = fields.One2many(comodel_name='survey.survey', inverse_name="event_id", string="Surveys")
    #guest_emails

    @api.constrains('place', 'address')
    def _check_adress(self):
        for rec in self:
            if (rec.place and not rec.address):
                raise ValidationError(_("Address has to be recorded"))

    @api.constrains('start', 'end')
    def start_date_check(self):
        today = fields.Datetime.today()
        for rec in self:
            if rec.end and rec.end < today:
                raise ValidationError(_('You\'ve entered the date that had already passed'))
            if rec.start and rec.start < today:
                raise ValidationError(_('You\'ve entered the date that had already passed'))
            if rec.start and rec.end and rec.end < rec.start:
                raise ValidationError(_('You\'ve entered end thar is earlier than start'))

    @api.model_create_multi
    def create(self, values):
        values[0]['organizer_ids'] = [self.env.user.id]
        print(values)
        return super(Event, self).create(values)

    def add_organizer(self):
        name = _('Add Organizer')
        view_mode = 'form'
        return {
            'name': name,
            'view_type': 'form',
            'view_mode': view_mode,
            'res_model': 'management.organizer',
            'type': 'ir.actions.act_window',
            'target': 'current'
        }
    def create_survey(self):
        name = _('Create survey')
        view_mode = 'form'
        return {
            'name': name,
            'view_type': 'form',
            'view_mode': view_mode,
            'res_model': 'survey.survey',
            'type': 'ir.actions.act_window',
            'target': 'current'
        }