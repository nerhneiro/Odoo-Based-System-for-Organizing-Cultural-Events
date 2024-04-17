from odoo import http
from odoo.http import request
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
import random

PASSWORD_LENGTH = 10


def generate_password():
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    special = "$#@!()*^%&"
    all_symbols = upper_letters + lower_letters + numbers + special
    generated_password = "".join(random.sample(all_symbols, PASSWORD_LENGTH))
    return generated_password


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
        user_email = kwargs.get('user_email')
        event_id = kwargs.get('event_id')
        person = request.env['res.users'].sudo().search([('email', '=', email)])
        guest = request.env['management.guest'].sudo().search([('id', '=', guest_id)])
        name = guest.name
        event = request.env['management.event'].sudo().search([('id', '=', event_id)])
        print(name, email, event_id)
        if person:
            # добавить user'у guest_id
            print("SUCCESS")
            print(len(person.guest_event_ids), person.guest_event_ids)

            # redirect to login page
            return request.redirect_query('/web/login', query=request.params)

        else:
            # create new user and redirect to change password page
            print("NOT FOUND")
            groups_id = [request.env.ref('base.group_user').id,
                         request.env.ref('org_management.group_event_guest').id]
            password = generate_password()
            http.request.env['res.users'].sudo().create({
                'name': name,
                'login': email,
                'email': email,
                'password': password,
                'groups_id': groups_id
            })
            user = request.env['res.users'].sudo().search([('login', '=', email)])
            # вот тут нужно user'у на email отправить письмо с просьбой поменять пароль с password на свой
            message = (f"Hello, your login: {email}\n Your password: {password}\n Please, click the link from the previous mail again and use this data")
            vals = {'state': 'outgoing',
                    'subject': 'CVs',
                    'body_html': '<pre>%s</pre>' % message,
                    'email_to': email,
                    'email_from': user_email,
                    }
            total_emails = http.request.env['mail.mail'].sudo().browse()
            total_emails = total_emails + http.request.env['mail.mail'].sudo().create(vals)
            total_emails.send()
            print("NEW USER CREATED", password)
            return "We have sent you an email with login and password."
