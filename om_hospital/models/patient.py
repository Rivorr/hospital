from email.policy import default
from re import sub
import string
from unittest import result
from odoo.exceptions import ValidationError
from pkg_resources import require
from odoo import api, fields, models, api,_
from datetime import datetime, date


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'
    _order = "id desc"


    name = fields.Char(string='Nom', required=True, tracking=True)
    reference = fields.Char(string="Order Reference",required=True,copy=False,readonly=True,default=lambda self: _('New'))
    age = fields.Integer(string='Age',tracking=True)
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female'),
        ('auther','auther')],string='Gender',required=True,default='male',tracking=True)
    note = fields.Text(string="Description")
    state = fields.Selection([
            ('draft', 'Draft'),
            ('confirm', 'Confirmed'),
            ('done', 'Done'),
            ('cancel', 'Cancelled'),], default='draft', string='Status',tracking=True)
    responsible_id = fields.Many2one('res.partner',string='Responsible')
    appointment_count = fields.Integer(string="Appointement Count", compute="_compute_appointment_count")
    image = fields.Binary(string="Patient Image")
    appointment_ids = fields.One2many('hospital.appointment','patient_id', string="Appointments")


    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    # (Donner la valeur apres clic sur btn create ou sauvegarder)
    @api.model
    def create(self,vals):
        if not vals.get('note'):
            vals['note' ]= 'New Patient'
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
        res = super(HospitalPatient,self).create(vals)
        return res

    # (Donner un valeur d'un champs)
    def _compute_appointment_count(self):
        for rec in self:
            # select count(*) from hospital_appointment where patient_id = 5 (self.env=5)
            # appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=',self.id)])
            appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=',rec.id)])
            rec.appointment_count = appointment_count

    # (Donner et recuperer la valeur par defaut d'un field avent de creer ou sauvegarder)
    @api.model
    def default_get(self,fields):
        res = super(HospitalPatient, self).default_get(fields)
        print("Overide====>",fields)
        print("RES=====>",res)
        if not  res.get('gender'):
            res['gender'] = 'female'
        res['age'] = 50
        res['note'] = 'Test Default Get Methode'
        return res

    @api.constrains('name')
    def check_name(self):
        for rec in self:
            patients = self.env['hospital.patient'].search([('name', '=', rec.name),('id', '!=', rec.id)])
            if patients:
                raise ValidationError("Name %s already existes" % rec.name)

    @api.constrains('age')
    def check_age(self):
        for rec in self:
            if rec.age == 0:
                raise ValidationError("Age cannot be zero...!")

    # Fonction name, combiner ou concatenaion de valeur
    def name_get(self):
        result = []
        for rec in self:
            name = '[ '+ rec.reference + ']' + rec.name + ' ' + rec.gender
            result.append((rec.id, name))
        return result


    def action_open_appointments(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Appointments',
            'res_model': 'hospital.appointment',
            'domain': [('patient_id', '=', self.id)],
            'view_mode': 'tree,form',
            'target': 'current',
        }