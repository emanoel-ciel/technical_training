"""
# Ações do Odoo

## Visão Geral
As ações no Odoo são uma parte fundamental do framework que permitem aos desenvolvedores definir vários tipos de operações que podem ser desencadeadas por interações do usuário ou outros eventos. As ações podem ser usadas para abrir visualizações, executar ações no servidor, exibir relatórios e mais.

## Tipos de Ações

1. **Ações de Janela**: Essas ações são usadas para abrir diferentes visualizações (formulário, árvore, kanban, etc.) de um modelo. Elas são tipicamente desencadeadas por itens de menu ou botões.
    - Exemplo: Abrir uma visualização de formulário de um registro específico.
    - Sintaxe:
      ```xml
      <record id="action_form_view" model="ir.actions.act_window">
          <field name="name">Form View Action</field>
          <field name="res_model">model.name</field>
          <field name="view_mode">form</field>
      </record>
      ```

2. **Ações de Servidor**: Essas ações executam código Python no lado do servidor. Elas podem ser usadas para vários propósitos, como atualizar registros, enviar e-mails ou chamar APIs externas.
    - Exemplo: Enviar automaticamente um e-mail quando um registro é criado.
    - Sintaxe:
      ```xml
      <record id="action_server" model="ir.actions.server">
          <field name="name">Server Action</field>
          <field name="model_id" ref="model.model_name"/>
          <field name="state">code</field>
          <field name="code">
              <![CDATA[
              # Python code here
              ]]>
          </field>
      </record>
      ```

3. **Ações de Cliente**: Essas ações são executadas no lado do cliente e podem ser usadas para realizar operações como abrir uma URL, exibir uma mensagem ou executar código JavaScript.
    - Exemplo: Redirecionar o usuário para um site externo.
    - Sintaxe:
      ```xml
      <record id="action_client" model="ir.actions.client">
          <field name="name">Client Action</field>
          <field name="tag">your_custom_tag</field>
          <field name="params">{}</field>
      </record>
      ```

4. **Ações de Relatório**: Essas ações são usadas para gerar e exibir relatórios. Elas podem ser desencadeadas por botões ou itens de menu e podem produzir vários formatos como PDF, Excel, etc.
    - Exemplo: Gerar um relatório de vendas em formato PDF.
    - Sintaxe:
      ```xml
      <record id="action_report" model="ir.actions.report">
          <field name="name">Sales Report</field>
          <field name="model">sale.order</field>
          <field name="report_type">qweb-pdf</field>
          <field name="report_name">module.report_name</field>
      </record>
      ```

## Como Usar Ações

### Definindo uma Ação de Janela
Para definir uma ação de janela, você precisa criar um registro no modelo `ir.actions.act_window`. Aqui está um exemplo:
```xml
<record id="action_form_view" model="ir.actions.act_window">
    <field name="name">Form View Action</field>
    <field name="res_model">model.name</field>
    <field name="view_mode">form</field>
</record>
```