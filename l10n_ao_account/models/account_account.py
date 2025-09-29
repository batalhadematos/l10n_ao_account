# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.osv import expression


class AccountAccount(models.Model):
    _inherit = 'account.account'
    
    account_type = fields.Selection(selection_add=[('view', 'View')], ondelete={'view': 'cascade'})
    internal_group = fields.Selection(selection_add=[('view', 'View')], ondelete={'view': 'cascade'})
    
    
    @api.model
    def _search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None):
        # Casos específicos onde SEMPRE devem aparecer contas view
        always_show_cases = (
            self._context.get('show_view_accounts') or
            self._is_specific_case_that_needs_views()
        )
        if always_show_cases:
            return super()._search(domain, offset=offset, limit=limit, order=order, access_rights_uid=access_rights_uid)
        
        # Para outros casos, excluir contas view
        if not self._contains_view_account_filter(domain):
            domain = expression.AND([domain, [('account_type', '!=', 'view')]])
        
        return super()._search(domain, offset=offset, limit=limit, order=order, access_rights_uid=access_rights_uid)
    
    
    @api.model
    def _contains_view_account_filter(self, domain):
        #Verifica se o domain já contém algum filtro relacionado com account_type 'view'
        for element in domain:
            if isinstance(element, (list, tuple)) and len(element) == 3:
                field, operator, value = element
                if field == 'account_type':
                    # Verificar diferentes operadores que podem afectar contas view
                    if operator == '=' and value == 'view':
                        return True
                    elif operator == '!=' and value == 'view':
                        return True
                    elif operator == 'in' and isinstance(value, (list, tuple)) and 'view' in value:
                        return True
                    elif operator == 'not in' and isinstance(value, (list, tuple)) and 'view' not in value:
                        return True
            elif isinstance(element, (list, tuple)):
                # Recursivamente verificar sub-domínios
                if self._contains_view_account_filter(element):
                    return True
        return False

    
    def _is_specific_case_that_needs_views(self):
        #Identifica casos específicos conhecidos que precisam de contas view
        # 1. Exportação de traduções
        #contexto = self.env.context
        #print('CONTEXTO:', contexto)
        if self._context.get('check_translations'):
            return True
        
        # 2. Geração de relatórios específicos: exemplo de contexto...
        if self._context.get('print_chart_of_accounts'):
            return True
            
        # 3. Ações administrativas conhecidas
        return False
    
    