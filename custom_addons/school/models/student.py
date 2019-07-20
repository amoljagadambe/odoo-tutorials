from odoo import fields,models,api,_
from datetime import date
from odoo.exceptions import UserError

class StudentInfo(models.Model):
    
    _name='student.student'
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
    class_id = fields.Many2one('class.class','Class')
    student_display_name = fields.Char('Student Name')
    class_strength = fields.Integer(related="class_id.max_class_strength",string='Total Class Strength')
    class_line = fields.Many2many('class.class','student_class_rel','class_id','student_id','Class')
    
    
    
    @api.onchange('birth_date')
    def onchange_date(self):
        res = {}
        if self.birth_date:
            today = date.today()
            age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
#             if age < 3:
#                 raise UserError(_('Student Age should be more than 3 years.'))
            self.age = age
            warning = {
                    'title': _("Warning for Student Age"),
                    'message': "Student age Cannot be greater than 3 year"
                    }
            if age < 3:
                res['warning'] = warning
            res['age'] = age
            return res
    
    @api.model
    def create(self,create_values): #only 2 params, self will be empty recordset and fields is dict with all field values
        class_obj = self.env['class.class']
        if not create_values.get('gender'):
            raise UserError(_('Gender Value Cannot be duplicated'))
        res = super(StudentInfo,self).create(create_values)
        display_name = create_values.get('name') + '(Roll No - ' + str(create_values.get('roll_no')) + ' )'
        res.student_display_name = display_name
        class_students = self.search([('class_id','=',res.class_id.id)])
        for student in class_students:
            if student.roll_no == res.roll_no and student.id != res.id:
                raise UserError(_('Roll No Cannot be duplicated'))
        return res
    
    
    @api.multi
    def write(self,changed_values):
        res = super(StudentInfo,self).write(changed_values)
        return res
    
    @api.model
    def default_get(self,default_values):
        context = self._context
        res = super(StudentInfo,self).default_get(default_values)
        res['roll_no'] = 20
        return res
    
    @api.constrains('roll_no')
    def class_constraint(self):
        for rec in self:
            if rec.roll_no > rec.class_strength:
                raise UserError(_('Roll No should not exceed class Strength'))
    
    @api.multi
    def unlink(self):
        for rec in self:
            if rec.active_student:
                raise UserError(_('Name - %s , Is an Active Student, You cannot remove it') % rec.name)
        return super(StudentInfo,self).unlink()
    
    
    
    
    
    
    
    