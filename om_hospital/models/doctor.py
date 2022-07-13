from email.policy import default
from odoo import fields,models,api,_

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'HospitalDoctor'
    _rec_name = 'doctor_name'

    doctor_name = fields.Char(string="Name",required=True,tranking=True)
    # copy=False: si on duplique(copie) la valeur de age=0
    age = fields.Integer(string="Age",tranking=True, copy=False)
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female'),
        ('auther','auther')],string='Gender',default='male',tracking=True)
    note = fields.Text(string="Description")
    image = fields.Binary(string="Doctor Image")
    appointment_count = fields.Integer(string="Appointement Count", compute="_compute_appointment_count")
    active = fields.Boolean(string="Active", default=True)


    # Dupliquer et renomer
    def copy(self, default=None):
        print("Successfully")
        if default is None:
            default = {}
        if not default.get('doctor_name'):
            default['doctor_name'] = _("%s (copy)",self.doctor_name)
            default['note'] = "Copied record"
        return super(HospitalDoctor, self).copy(default)

    def _compute_appointment_count(self):
        for rec in self:
            appointment_count = self.env['hospital.appointment'].search_count([('doctor_id', '=',rec.id)])
            rec.appointment_count = appointment_count