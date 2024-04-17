from odoo import http
from odoo.http import request
from odoo.addons.auth_signup.controllers.main import AuthSignupHome


class BecomeOrganizerOnSignUp(AuthSignupHome):  # это override sign up page

    def do_signup(self, *args):
        super(BecomeOrganizerOnSignUp, self).do_signup(*args)  # совершается регистрация пользователя
        env = request.env
        env.user.sudo().write({'groups_id': [
            (3, env.ref('base.group_portal').id),
            # удаляю пользователя из группы (типа) "Portal user", так как по дефолту приписывается она, и "User can't have two group types"
            (4, env.ref('base.group_user').id),  # добавляю пользователя в группу "Internal user"
            (4, env.ref('org_management.group_event_organizer').id),
            # приписываю группу "group_event_organizer" при регистрации
        ]
        })
        request.env.cr.commit()

class ParametersController(http.Controller):
    @http.route(route='/redirect_info', auth='public')
    def create_info(self, **kwargs):
        guest_id = kwargs.get('guest_id')
        email = kwargs.get('email')
        event_id = kwargs.get('event_id')
        person = request.env['res.users'].sudo().search([('email', '=', email)])
        guest = request.env['management.guest'].sudo().search([('id', '=', guest_id)])
        name = guest.name
        event = request.env['management.event'].sudo().search([('id', '=', event_id)])
        #добавить user'у guest_id
        if person:
            print("SUCCESS")
            # redirect to login page
        else:
            # create new user and redirect to change password page
            print("NOT FOUND")
            http.request.env['res.users'].sudo().create({
                'name': name,
                'login': email,
                'email': email,
                'guest_event_ids': guest
            })
            user = request.env['res.users'].sudo().search([('login', '=', email)])

            print("NEW USER CREATED")
        print(name, email, event_id)
