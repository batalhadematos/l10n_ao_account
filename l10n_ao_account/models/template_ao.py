# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, Command, fields, api, _
from odoo.addons.account.models.chart_template import template


class AccountChartTemplate(models.AbstractModel):
    _inherit = 'account.chart.template'
    
    @template('ao')
    def _get_ao_template_data(self):
        return {
            'code_digits': '1',
            'property_account_receivable_id': 'ao_31121001',
            'property_account_payable_id': 'ao_32121001',
            'property_account_expense_categ_id': 'ao_212111',
            'property_account_income_categ_id': 'ao_6111',
        }
    
    
    @template('ao', 'account.journal')
    def _get_ao_account_journal(self):
        return {
            'sale': {'refund_sequence': False},
            'purchase': {'refund_sequence': False},
            'bank': {'payment_sequence': False},
            'cash': {'payment_sequence': False},
        }
    
    
    @template('ao', 'res.company')
    def _get_ao_res_company(self):
        return {
            self.env.company.id: {
                'account_fiscal_country_id': 'base.ao',
                'anglo_saxon_accounting': True,
                'cash_account_code_prefix': '4510', 
                'bank_account_code_prefix': '4311', 
                'transfer_account_code_prefix': '471', 
                'income_currency_exchange_account_id': 'ao_6621', 
                'expense_currency_exchange_account_id': 'ao_7621', 
                'account_journal_early_pay_discount_loss_account_id': 'ao_7631', 
                'account_journal_early_pay_discount_gain_account_id': 'ao_6631',
                'account_default_pos_receivable_account_id': 'ao_31121001', 
                'default_cash_difference_income_account_id': 'ao_6382',
                'default_cash_difference_expense_account_id': 'ao_7582',
                'account_sale_tax_id': 'iva_bens_sales',
                'account_purchase_tax_id': 'iva_bens_purchase',
            },
        }

    
    @api.model
    def _get_country_codes(self):
        """ Load for Angolan COmpanies """
        return ["AO"]
    
    
    @template(model='account.journal')
    def _get_account_journal(self, template_code):
        if self.env.company.country_id.code in self._get_country_codes():
            return {
                "sale": {
                    'name': _('Customer Invoices'),
                    'type': 'sale',
                    'code': _('INV'),
                    'show_on_dashboard': True,
                    'color': 11,
                    'sequence': 1,
                    'restrict_mode_hash_table': False,
                    'saft_invoice_type': 'FT',
                    'default_account_id': 'ao_6111',
                },
                "invoice_receipt": {
                    'name': _('Sales Invoice/Receipt'),
                    'type': 'sale',
                    'code': _('FR'),
                    'show_on_dashboard': True,
                    'color': 11,
                    'sequence': 6,
                    'restrict_mode_hash_table': False,
                    'saft_invoice_type': 'FR',
                    'default_account_id': 'ao_6111',
                },
                "purchase": {
                    'name': _('Supplier Invoices'),
                    'type': 'purchase',
                    'code': _('BILL'),
                    'show_on_dashboard': True,
                    'color': 11,
                    'sequence': 7,
                    'restrict_mode_hash_table': False,
                    'saft_invoice_type': 'FT',
                    'default_account_id': 'ao_212111',
                },
                "bank": {
                    'name': _('Bank'),
                    'type': 'bank',
                    'show_on_dashboard': True,
                    'sequence': 8,
                    'restrict_mode_hash_table': False,
                    'saft_receipt_type': 'RC',
                },
                "cash": {
                    'name': _('Cash'),
                    'type': 'cash',
                    'show_on_dashboard': True,
                    'sequence': 9,
                    'restrict_mode_hash_table': False,
                    'saft_receipt_type': 'RC',
                },
                "general": {
                    'name': _('General'),
                    'type': 'general',
                    'code': _('MISC'),
                    'show_on_dashboard': True,
                    'sequence': 10,
                    'restrict_mode_hash_table': False,
                },
                "sale_debit": {
                    'name': _('Customer Debit Notes'),
                    'type': 'sale',
                    'code': _('NDV'),
                    'show_on_dashboard': True,
                    'color': 11,
                    'sequence': 11,
                    'restrict_mode_hash_table': False,
                    'saft_invoice_type': 'ND',
                    'default_account_id': 'ao_6111',
                },
                "purchase_debit": {
                    'name': _('Supplier Debit Notes'),
                    'type': 'purchase',
                    'code': _('NDF'),
                    'show_on_dashboard': True,
                    'color': 11,
                    'sequence': 12,
                    'restrict_mode_hash_table': False,
                    'saft_invoice_type': 'ND',
                    'default_account_id': 'ao_212111',
                },
                "autoinvoice": {
                    'name': _('Autofacturação'),
                    'type': 'purchase',
                    'code': _('AF'),
                    'show_on_dashboard': True,
                    'color': 11,
                    'sequence': 13,
                    'restrict_mode_hash_table': False,
                    'saft_invoice_type': 'AF',
                    'default_account_id': 'ao_212111',
                },
                "exch": {
                    'name': _('Exchange Difference'),
                    'type': 'general',
                    'code': _('EXCH'),
                    'show_on_dashboard': False,
                    'sequence': 14,
                    'restrict_mode_hash_table': False,
                },
                "caba": {
                    'name': _('Impostos de Fundo de Caixa'),
                    'type': 'general',
                    'code': _('CABA'),
                    'show_on_dashboard': False,
                    'sequence': 15,
                    'restrict_mode_hash_table': False,
                },
                "withholding_tax": {
                    'name': _('Withholding Tax'),
                    'type': 'general',
                    'code': _('RET'),
                    'show_on_dashboard': False,
                    'sequence': 20,
                    'saft_transaction_type': 'N',
                    'restrict_mode_hash_table': False,
                },
                "opening_journal": {
                    'name': _('Abertura'),
                    'type': 'general',
                    'code': _('ABT'),
                    'show_on_dashboard': False,
                    'sequence': 30,
                    'restrict_mode_hash_table': False,
                    'payment_debit_account_id': 'ao_911',
                    'payment_credit_account_id': 'ao_922',
                },
                "regularizacoes_journal": {
                    'name': _('Regularizações'),
                    'type': 'general',
                    'code': _('REG'),
                    'show_on_dashboard': False,
                    'sequence': 31,
                    'restrict_mode_hash_table': False,
                    'saft_transaction_type': 'R',
                },
                "apuramentos_journal": {
                    'name': _('Apuramentos'),
                    'type': 'general',
                    'code': _('APR'),
                    'show_on_dashboard': False,
                    'sequence': 32,
                    'restrict_mode_hash_table': False,
                    'saft_transaction_type': 'A',
                },
                "resultados_journal": {
                    'name': _('Resultados'),
                    'type': 'general',
                    'code': _('RST'),
                    'show_on_dashboard': False,
                    'sequence': 33,
                    'restrict_mode_hash_table': False,
                    'saft_transaction_type': 'J',
                },
            }
