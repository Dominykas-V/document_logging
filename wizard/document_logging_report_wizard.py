# -*- coding: utf-8 -*-

from odoo import models, fields

class DocumentLoggingReportWizard(models.TransientModel):
    _name = 'document_logging.report_wizard'
    _description = 'Document Logging - Report Wizard'

    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)

    def generate_report(self):
        # Grabs data from db
        logging_records = self.env['document_logging.document_logging'].search([
            ('create_date', '>=', self.start_date),
            ('create_date', '<=', self.end_date)
        ])

        # Creates dynamic tree view from data
        view = {
            'name': 'Document Logging Report',
            'view_mode': 'tree',
            'res_model': 'document_logging.document_logging',
            'type': 'ir.actions.act_window',
            'target': 'new',
            'domain': [('id', 'in', logging_records.ids)],
            'context': {
                'default_name': self.start_date,
                'default_description': self.end_date,
                'create': False,
            },
            'views': [(False, 'tree')],
            # 'fields': ['name', 'description', 'create_date'],
        }
        return view
