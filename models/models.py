# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ExtendsInvoice(models.Model):
	_name = 'account.invoice'
	_inherit = 'account.invoice'

	cuenta_id = fields.Selection([('indistinto', 'Indistinto'), ('cuenta1', 'Cuenta 1'), ('cuenta2', 'Cuenta 2')], string='Aplica a', select=True, default='indistinto')

class ExtendsPaymentGroup(models.Model):
	_name = 'account.payment.group'
	_inherit = 'account.payment.group'

	cuenta_id = fields.Selection([('indistinto', 'Indistinto'), ('cuenta1', 'Cuenta 1'), ('cuenta2', 'Cuenta 2')], string='Aplica a', select=True, default='indistinto')

class ExtendsMoveLine(models.Model):
	_name = 'account.move.line'
	_inherit = 'account.move.line'
	cuenta_id = fields.Selection([('indistinto', 'Indistinto'), ('cuenta1', 'Cuenta 1'), ('cuenta2', 'Cuenta 2')], string='Aplica a', readonly=True)

	@api.model
	def create(self, values):
		rec = super(ExtendsMoveLine, self).create(values)
		if len(rec.invoice_id) > 0:
			rec.cuenta_id = rec.invoice_id.cuenta_id
		elif len(rec.payment_id) > 0:
			rec.cuenta_id = rec.payment_id.payment_group_id.cuenta_id
		return rec
