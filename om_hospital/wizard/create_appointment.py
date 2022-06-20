from email.policy import default
import string
from pkg_resources import require
from odoo import api, fields, models, api,_
from datetime import datetime, date


class CreateAppointmentWizard(models.TransientModel):
    _name = 'create.appointment.wizard'
    _description = 'Create Appointment Wizard'


    name = fields.Char(string='Nom', required=True, tracking=True)
    patient_id = fields.Many2one('hospital.patient',string='Patient', required=True)
    

    def action_create_appointment(self):
        print("click Me")
        vals = {
            'patient_id': self.patient_id.id,
            'date_appointment': self.date_appointment
                }
        self.env['hospital.appointment'].create(vals)