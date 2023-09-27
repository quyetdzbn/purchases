# -*- coding: utf-8 -*-


from odoo import models, fields, api


class InheritDepartment(models.Model):
    _inherit = 'hr.department'
    _description = 'extend department'

    spending_limit_month = fields.Char()
