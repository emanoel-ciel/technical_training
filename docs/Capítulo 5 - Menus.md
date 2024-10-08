"""
# Menus do Odoo

Os menus no Odoo são utilizados para navegar por diferentes visualizações e funcionalidades da aplicação. Eles são definidos em arquivos XML e podem ser categorizados em três tipos: menus principais, submenus e ações. Cada menu pode ser vinculado a uma ação, que pode ser uma ação de janela, um relatório ou qualquer outro tipo de ação.

### Como Gerar Menus no Odoo

Para criar um menu no Odoo, você precisa defini-lo em um arquivo XML dentro do seu módulo. A sintaxe básica envolve o uso da tag `<menuitem>`, especificando atributos como `id`, `name`, `parent` e `action`.

### Exemplo de Sintaxe

```xml
<menuitem id="menu_main" name="Menu Principal" sequence="1"/>
<menuitem id="submenu_example" name="Submenu Exemplo" parent="menu_main" action="action_example" sequence="1"/>
```

