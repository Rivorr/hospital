from odoo import models,fields,api


class AllPatientReport(models.AbstractModel):
    # method abstrait,_name = "report.module_name.template_name"
    _name = "report.om_hospital.report_all_patient_list"
    _description = "Patient report"

    @api.model
    def _get_report_values(self,docids,data=None):
        print("TESTING====================>",docids,"===========>",data)
        domain = []
        gender = data.get('form_data').get('gender')
        age = data.get('form_data').get('age')
        if gender:
            domain += [('gender', '=', gender)]
        if age != 0:
            domain += [('age', '=', age)]
        
        docs = self.env['hospital.patient'].search(domain)
        return {
            'docs': docs,
        }



class PatientDetailReport(models.AbstractModel):
    # method abstrait,_name = "report.module_name.template_name"
    _name = "report.om_hospital.report_patient_detail"
    _description = "Patient details report"


    @api.model
    def _get_report_values(self,docids,data=None):        
        # docs = self.env['hospital.patient'].search(['id', '=', docids])
        docs = self.env['hospital.patient'].browse(docids)

        return {
            'docs': docs,
        }