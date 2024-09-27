# Capítulo 3 - Introdução de Dados

## Arquivos de Dados no Odoo

Os arquivos de dados no Odoo são utilizados para carregar informações iniciais e realizar testes. Eles são geralmente escritos em formato XML ou CSV e contêm registros que serão inseridos no banco de dados. Esses arquivos são essenciais para a configuração inicial do sistema e para garantir que os módulos funcionem corretamente durante o desenvolvimento e testes.

### Estrutura de Diretórios

Abaixo está uma ilustração da estrutura de diretórios partindo do addon onde fica o diretório `data`:

```
addon_name/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── model.py
├── views/
│   ├── view.xml
│   └── another_view.xml
├── data/
│   ├── data_file.xml
│   └── another_data_file.xml
└── tests/
    ├── __init__.py
    └── test_file.py
```

### Utilização dos Arquivos de Dados

1. **Carga Inicial**: Arquivos de dados são usados para carregar dados iniciais, como configurações padrão, categorias de produtos, ou qualquer outro dado necessário para o funcionamento do módulo.

2. **Testes**: Durante o desenvolvimento, arquivos de dados são usados para criar cenários de teste. Isso garante que o módulo funcione corretamente em diferentes situações.

### Exemplo de Arquivo XML

```xml
<odoo>
    <data>
        <record id="example_record" model="res.partner">
            <field name="name">Example Partner</field>
        </record>
    </data>
</odoo>
```

### Exemplo de Arquivo CSV

```csv
id,name
example_record,Example Partner
```

Esses exemplos mostram como os arquivos de dados podem ser estruturados para inserir registros no banco de dados do Odoo.
