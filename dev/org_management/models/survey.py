from odoo import models, fields, api

class FeedbackSurvey(models.Model):
    _inherit = 'survey.survey'
    event_id = fields.Many2one(comodel_name='management.event', string="Linked event")

    @api.onchange('event_id')
    def only_my_events(self):
        uid = self.env.user.id
        for rec in self:
            return {'domain': {'event_id': [('organizer_ids', 'in', [uid])]}}
