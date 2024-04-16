from odoo import http
from odoo.http import request
from odoo.addons.auth_signup.controllers.main import AuthSignupHome

class BecomeOrganizerOnSignUp(AuthSignupHome): #это override sign up page

    def do_signup(self, *args):
        super(BecomeOrganizerOnSignUp, self).do_signup(*args) #совершается регистрация пользователя
        env = request.env
        env.user.sudo().write({'groups_id': [
            (3, env.ref('base.group_portal').id), #удаляю пользователя из группы (типа) "Portal user", так как по дефолту приписывается она, и "User can't have two group types"
            (4, env.ref('base.group_user').id), #добавляю пользователя в группу "Internal user"
            (4, env.ref('org_management.group_event_organizer').id), #приписываю группу "group_event_organizer" при регистрации
        ]
        })
        request.env.cr.commit()

class ParametersController(http.Controller):
    @http.route(route='/redirect_info', auth='public')
    def create_info(self, **kwargs):
        name = kwargs.get('name')
        print(name)
