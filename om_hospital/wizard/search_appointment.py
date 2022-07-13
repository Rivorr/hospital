import string
from pyparsing import srange
from odoo import fields,models,api,_


class SearchAppointmentWizard(models.Model):
    _name = 'search.appointment.wizard'
    _description = 'Search Appointment'

    patient_id = fields.Many2one('hospital.patient', string='Patient',required=True)


    def action_search_appointment_m1(self):
        action = self.env.ref('om_hospital.action_hospital_appointment').read()[0]
        action['domain'] = [('patient_id', '=', self.patient_id.id)]
        return action

    def action_search_appointment_m2(self):
        action = self.env['ir.actions.actions']._for_xml_id("om_hospital.action_hospital_appointment")
        action['domain'] = [('patient_id', '=', self.patient_id.id)]
        return action

    def action_search_appointment_m3(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Appointments',
            'res_model': 'hospital.appointment',
            'view_type': 'form',
            'domain': [('patient_id', '=', self.patient_id.id)],
            'view_mode': 'tree,form',
            'target': 'current',
        }