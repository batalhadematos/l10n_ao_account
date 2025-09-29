# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields


class AccountJournal(models.Model):
    _inherit = "account.journal"
    
    saft_invoice_type= fields.Selection([
                        ('FT', 'Factura/Nota de Crédito (Vendas e Compras)'), 
                        ('FG', 'Factura Global (Vendas e Compras)'), 
                        ('FR', 'Factura/Recibo (Vendas)'),
                        ('AF', 'Factura/Recibo de Autofacturação (Compras)'),
                        ('ND', 'Nota de Débito (Vendas e Compras)'),
                        ('TV', 'Talão de Venda (Vendas)'),
                        ('AC', 'AC - Aviso de Cobrança (Vendas e Compras)'),
                        ('AR', 'AR - Aviso de Cobrança/recibo (Vendas e Compras)'),
                        ], default=False, string='Invoice Type', copy=True, help="Categorias para classificar os documentos comerciais na exportação do SAFT e para determinação do tipo de documento no sistema.\nAlguns tipos se aplicam apenas a determinado tipo de diário.")
    
    saft_receipt_type= fields.Selection([
                        ('RC', 'Recibo Emitido'), 
                        ], 
                        default='RC', string='Receipt Type', copy=False, help="Categorias para classificar os recibos de pagamento na exportação do SAFT e para determinação do tipo de documento no sistema.")
    
    invoice_sequence_id = fields.Many2one('ir.sequence', ondelete='restrict', string='Invoice sequence number', copy=False)
    credit_sequence_id = fields.Many2one('ir.sequence', ondelete='restrict', string='Credit Note sequence number', copy=False)
    inbound_receipt_sequence_id = fields.Many2one('ir.sequence', ondelete='restrict', string='Sequência para Recibos de Clientes', copy=False)
    
    payment_debit_account_id = fields.Many2one("account.account", ondelete='restrict', string="Conta a Débito - Abertura", copy=False,)
    payment_credit_account_id = fields.Many2one("account.account", ondelete='restrict', string="Conta a Crédito - Abertura", copy=False,)
    
    saft_transaction_type = fields.Selection([('N', 'Normal'), 
                                       ('R', 'Regularizações'),
                                       ('A', 'Apuramento de Resultados'), 
                                       ('J', 'Ajustamentos/Resultados')], default="N", string='Transaction Type', copy=False, help="Categorias para classificar os movimentos contabilísticos ao exportar o SAFT")
    