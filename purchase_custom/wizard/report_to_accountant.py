import re
from datetime import datetime, date, timedelta

from odoo import models, fields, api


class ReportToAccountant(models.TransientModel):
    _name = 'report.to.accountant'

    select_month = fields.Selection(
        [('thang1', 'Tháng 1'), ('thang2', 'Tháng 2'), ('thang3', 'Tháng 3'), ('thang4', 'Tháng 4'),
         ('thang5', 'Tháng 5'), ('thang6', 'Tháng 6'), ('thang7', 'Tháng 7'), ('thang8', 'Tháng 8'),
         ('thang9', 'Tháng 9'), ('thang10', 'Tháng 10'), ('thang11', 'Tháng 11'),
         ('thang12', 'Tháng 12')], default='thang1')
    department_ids = fields.Many2many('hr.department')

    def get_data(self):
        if self.select_month:
            x = re.sub(r'\D', '', self.select_month)
            current_year = date.today().year - 2000
            date_begin = datetime.strptime("01" + x + str(current_year), '%d%m%y')
            date_end = (date_begin + timedelta(days=31)).replace(day=1) - timedelta(days=1)

            action = self.env['ir.actions.act_window']._for_xml_id('purchase_custom.report_to_accountant_action_wizard')
            if self.department_ids:
                action['domain'] = [('create_date', '>', date_begin), ('create_date', '<=', date_end),
                                    ('department', 'in', self.department_ids.ids)]
            else:
                action['domain'] = [('create_date', '>', date_begin), ('create_date', '<=', date_end)]
            return action
