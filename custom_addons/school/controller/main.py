from odoo import http
from odoo.http import request

class RegistrationForm(http.Controller):


    # Check and insert values from the form on the model <model>
    @http.route('/registration_form', type='http', auth="user", website=True)
    def website_form(self, **kwargs):
        values={}
        class_obj = request.env['class.class'].search([])
        values['classes'] = class_obj
        for val in class_obj:
            print(val.id)
            print(val.name)
        return request.render('school.registration_id',values)
    
    @http.route('/complete/registration', type='http', auth="public", website=True)
    def website_form_complete(self, **kwargs):
        values={}
        create_values = {}
        student_obj = request.env['student.student']
        mail_template_obj = request.env['mail.template']
        create_values['gender'] = kwargs.get('gender')
        create_values['name'] = kwargs.get('name')
        create_values['class_id'] = kwargs.get('class')
        create_values['student_email'] = kwargs.get('email')
        try:
            student_id = student_obj.create(create_values)
            values['enrolment_no'] = student_id.enrolment_no
            template_id = request.env.ref('school.send_student_registration_id')
            template_id.send_mail(student_id.id, force_send=True)
        except Exception as e:
            print(e)
            return request.render('school.registration_exception_id',{'error_reason':e})
        return request.render('school.registration_complete_id',values)
        