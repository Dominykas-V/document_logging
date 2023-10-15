# -*- coding: utf-8 -*-

from odoo import models, fields


class document_logging(models.Model):
    _name = 'document_logging.document_logging'
    _description = 'Document Logging'

    name = fields.Char()
    description = fields.Text()
    company = fields.Many2one('res.company')
