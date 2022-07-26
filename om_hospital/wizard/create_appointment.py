from email.policy import default
import string
from pkg_resources import require
from odoo import api, fields, models, api,_
from datetime import datetime, date


class CreateAppointmentWizard(models.TransientModel):
    _name = 'create.appointment.wizard'
    _description = 'Create Appointment Wizard'


    date_appointment = fields.Date(string='Date', required=False, tracking=True)
    patient_id = fields.Many2one('hospital.patient',string='Patient', required=True)
    doctor_id = fields.Many2one('hospital.doctor',string='Doctor', required=True)

    # recuper la valeur de field dans le form et info de ce form (lang,uid,modele,activ_id)
    @api.model
    def default_get(self, fields):
        res = super(CreateAppointmentWizard, self).default_get(fields)
        print("------------",self._context)
        if self._context.get('active_id'):
            res['patient_id'] = self._context.get('active_id')
        return res


    def action_create_appointment(self):
        print("click Me")
        vals = {
            'patient_id': self.patient_id.id,
            'doctor_id': self.doctor_id.id,
            'date_appointment': self.date_appointment
                }
        appointment_rec = self.env['hospital.appointment'].create(vals)
        print("VALS====>",vals)
        print("APP_REC====>",appointment_rec.id)
        return {
            'name': _('Appointments'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hospital.appointment',
            'res_id': appointment_rec.id,
            # 'target': 'new',
        }

    def action_view_appointment(self):
        # (target:new --> afficher sous forme wizard et permet de modifier, target:current --> afficher sous forme view form)

        # Method 1
        # action = self.env.ref('om_hospital.action_hospital_appointment').read()[0]
        # print("ACTION====>",action)
        # action['domain'] = [('patient_id', '=', self.patient_id.id)]
        # return action

        # Method 2
        # action = self.env['ir.actions.actions']._for_xml_id('om_hospital.action_hospital_appointment')
        # action['domain'] = [('patient_id', '=', self.patient_id.id)]
        # return action

        # Method 3
        return {
            'type': 'ir.actions.act_window',
            'name': 'Appointments',
            'res_model': 'hospital.appointment',
            'view_type': 'form',
            'domain': [('patient_id', '=', self.patient_id.id)],
            'context': {'default_patient_id': self.id},
            'view_mode': 'tree,form',
            'target': 'current',
        }