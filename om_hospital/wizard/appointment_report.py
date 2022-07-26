import string
from odoo import models,fields,api


class AppointmentReportWizard(models.Model):
    _name = "appointment.report.wizard"
    _description = "Print appointment wizard"

    patient_id = fields.Many2one("hospital.patient", string="Patient")
    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")

    def action_print_report(self):

        # Recuperer patient id dans le field
        """
        domain = []
        patient_id = self.read()[0].get('patient_id')
        if patient_id:
            domain += [('patient_id', '=', patient_id)]
        """

        # Pour simplifier le code (avec l'objet)
        domain = []
        patient_id = self.patient_id
        if patient_id:
            domain += [('patient_id', '=', patient_id.id)]
        date_from = self.date_from
        if date_from:
            domain += [('date_appointment', '>=', date_from)]
        date_to = self.date_to
        if date_to:
            domain += [('date_appointment', '<=', date_to)]
        print("DOMAIN ================>", domain)
        appointments = self.env['hospital.appointment'].search_read(domain)
        print("Appointments============>",appointments)
        print("AFF READ============>",self.read()[0])
        data = {
            'form_data': self.read()[0],
            'appointments': appointments
        }
        return self.env.ref('om_hospital.action_report_appointment').report_action(self, data=data)


        # Autre methode
        """
        appointments = self.env['hospital.appointment'].search(domain)
        print("Appointment=============>",appointments)
        appointment_list = []
        for appointment in appointments:
            vals  = {
                'name': appointment.name,
                'note': appointment.note,
                'age': appointment.age,
            }
        appointment_list.append(vals)
        data = {
            'form_data': self.read()[0],
            'appointments': appointments
        }
        return self.env.ref('om_hospital.action_report_appointment').report_action(self, data=data)
        """
