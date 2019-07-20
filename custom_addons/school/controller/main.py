from odoo import http
from odoo.http import request

class RegistrationForm(http.Controller):


    # Check and insert values from the form on the model <model>
    @http.route('/registration_form', type='http', auth="public", website=True)
    def website_form(self, **kwargs):
        values={}
        class_obj = request.env['class.class'].search([])
        values['classes'] = class_obj
        return request.render('school.registration_id',values)
    
    @http.route('/complete/registration', type='http', auth="public", website=True)
    def website_form_complete(self, **kwargs):
        values={}
        print(kwargs,'=======================')
        return request.render('school.registration_complete_id',values)
        