from odoo import fields, models, api


class ClassInfo(models.Model):
    
    _name='class.class'
    _rec_name = 'class_display_name'
    
    name = fields.Char('Class Name', required=True)
    teacher_name = fields.Char('Teacher Name')
    division_name = fields.Char('Division Name')
    monitor_name = fields.Char('Monitor Name')
    class_display_name = fields.Char(compute="_class_display_name",store=True)
    student_ids = fields.One2many('student.student','class_id','Students')
    class_strength = fields.Integer(compute="_count_strength",string='Class Strength')
    max_class_strength = fields.Integer('Maximum Class Strength',default=60)
    class_line = fields.Many2many('student.student','student_class_rel','student_id','class_id','Class')
    
    @api.depends('student_ids')
    def _count_strength(self):
        for rec in self:
            rec.class_strength = len(rec.student_ids.ids)
    
    
    @api.depends('name','division_name')
    def _class_display_name(self):
        for rec in self:
            if rec.name and rec.division_name:
                display_rec_name = rec.name + ' - Div ' + rec.division_name
                rec.class_display_name = display_rec_name
    
    _sql_constraints = [
        ('class_display_name_uniq', 'unique(class_display_name)', 'Class Name and Division must be unique !'),
    ]
    
#     @api.multi
#     def name_get(self):
#         name_list = []
#         for rec in self:
#             display_rec_name = rec.name + ' - Div ' + rec.division_name
#             name_list.append(((rec.id, display_rec_name)))
#             print(name_list,'================')
#         return name_list
#             