# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models

class AccountTaxGroup(models.Model):
    _inherit = "account.tax.group"

    tax_group_type = fields.Selection([('iva', 'Imposto Sobre Valor Acrescentado'),
                                ('selo', 'Imposto de Selo'),
                                ('ipu', 'Imposto Predial Urbano'),
                                ('retencao', 'Retenção na Fonte'),
                              ], string='Group Tax Type', copy=False)
    
    
class AccountTax(models.Model):
    _inherit = "account.tax"
    
    tax_type = fields.Selection([('iva', 'IVA Normal'),
                                 ('iva_cativo', 'Cativação do IVA'),
                                 ('outro', 'Outro')
                              ], string='Internal Tax Type', copy=False)
    
    main_tax = fields.Many2many(comodel_name="account.tax",  relation="related_taxes",  column1="main_tax",  column2="related_tax_ids")
    related_tax_ids = fields.Many2many(comodel_name='account.tax', string="Related Tax", copy=False,  relation="related_taxes", column1='related_tax_ids', column2='main_tax',
                                       help="Related tax for correct IVA Cativo attribution. Only for IVA Cativo tax type")
    tax_country_region = fields.Selection([('AO', 'Geral'),
                                           ('CAB', 'Cabinda')], 
                                           string="Fiscal Region", default="AO")
    saft_tax_type = fields.Selection([('IVA', 'IVA'),
                                      ('SELO', 'SELO'),
                                      ('NS','Não Sujeito a IVA/SELO')], 
                                     string="SAF-T tax Type", default=False, copy=False)
    saft_tax_code = fields.Selection([('NOR', 'Taxa Normal'),
                                      ('RED', 'Taxa Reduzida'),
                                      ('INT', 'Taxa Intermédia'),
                                      ('ISE', 'Isento'), 
                                      ('OUT', 'Outro')], 
                                     string="SAF-T Tax Code", default=False, copy=False)
    is_saft_included = fields.Boolean('Include in Saft Export', default=False, copy=False)
    saft_tax_description = fields.Char('SAF-T Description', copy=False)
    