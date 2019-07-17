from odoo import fields,models,api,_
from datetime import date
from odoo.exceptions import UserError

class StudentInfo(models.Model):
    
    _name='stud.stud'
    _rec_name="name"
    
    name = fields.Char('Student Name', required=True)
    roll_no = fields.Integer('Roll No', required=True)
    class_name = fields.Char('Class',help="Present class student is in",copy=False)
    div_name = fields.Char('Division Name')
    gender = fields.Selection([('male','Male'),('female','Female')], required=True,string="Gender",copy=False)
    active_student= fields.Boolean('Is Active ?')
    image = fields.Binary('Student Image')
    description = fields.Text('Student Description')
    stay_at = fields.Selection([('parent','Parent'),('guardian','Guardian'),('hostel','Hostel')],default="parent",string="Accomodation At")
    parent_id = fields.Many2one('res.partner','Parent')
    parent_name = fields.Char(related="parent_id.name",string='Parent Name')
    parent_ph_no = fields.Char(related="parent_id.mobile",string='Parent Mobile No')
    parent_address = fields.Char(related="parent_id.street",string='Parent Address')
    guardian_name = fields.Char('Guardian Name')
    guardian_ph_no = fields.Char('Guardian Mobile No')
    guardian_address = fields.Char('Guardian Address')
    hostel_name = fields.Char('Hostel Name')
    hostel_ph_no = fields.Char('Hostel Contact No')
    hostel_address = fields.Char('Hostel Address')
    birth_date = fields.Date('Birth Date')
    age = fields.Integer('Age')
    class_id = fields.Many2one('cl.cl','Class')
    
    @api.onchange('birth_date')
    def onchange_date(self):
        if self.birth_date:
            today = date.today()
            age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
            if age < 3:
                raise UserError(_('Student Age should be more than 3 years.'))
            self.age = age
    