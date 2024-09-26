
# Capítulo 2 - Modelos e Campos

Este módulo define um modelo Odoo e seus campos, utilizando a estrutura ORM (Object-Relational Mapping) do Odoo.

## Modelos

- Um modelo em Odoo é uma classe Python que herda de `models.Model`. Ele representa uma tabela no banco de dados.
- Cada instância do modelo representa um registro na tabela.

## Sintaxe Modelos:

```python
class NomeModulo(models.Model):
    _name = 'nome.tecnico'
    _description = 'Descrição do Módulo'
```

## Campos

- Campos são atributos do modelo que representam colunas na tabela do banco de dados.
- Tipos de campos comuns incluem:
    - `Char`: Representa uma string de texto.
    - `Integer`: Representa um número inteiro.
    - `Float`: Representa um número de ponto flutuante.
    - `Boolean`: Representa um valor booleano (True/False).
    - `Date`: Representa uma data.
    - `Datetime`: Representa uma data e hora.
    - `Many2one`: Representa uma relação muitos-para-um com outro modelo.
    - `One2many`: Representa uma relação um-para-muitos com outro modelo.
    - `Many2many`: Representa uma relação muitos-para-muitos com outro modelo.

## Sintaxe

- Para definir um campo, utiliza-se a sintaxe `nome_do_campo = fields.TipoDoCampo(string='Nome do Campo', required=True, default=valor_default, ...)`.

- Exemplos:
    - `name = fields.Char(string='Nome', required=True)`: Define um campo de texto obrigatório chamado "Nome".

    - `age = fields.Integer(string='Idade')`: Define um campo inteiro chamado "Idade".

    - `price = fields.Float(string='Preço', default=0.0)`: Define um campo de ponto flutuante chamado "Preço" com valor padrão 0.0.

    - `is_active = fields.Boolean(string='Ativo', default=True)`: Define um campo booleano chamado "Ativo" com valor padrão True.
    
    - `birthdate = fields.Date(string='Data de Nascimento')`: Define um campo de data chamado "Data de Nascimento".
    
    - `created_at = fields.Datetime(string='Criado em')`: Define um campo de data e hora chamado "Criado em".
    
    - `partner_id = fields.Many2one('res.partner', string='Parceiro')`: Define uma relação muitos-para-um com o modelo `res.partner`.
    
    - `order_lines = fields.One2many('sale.order.line', 'order_id', string='Linhas do Pedido')`: Define uma relação um-para-muitos com o modelo `sale.order.line`.
    
    - `tags = fields.Many2many('res.partner.category', string='Tags')`: Define uma relação muitos-para-muitos com o modelo `res.partner.category`.
