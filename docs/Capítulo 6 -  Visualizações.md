# Capítulo 6 - Visualizações

## Tipos de Visualizações

### Tree View
**Descrição:** A Tree View (ou List View) exibe registros em formato de tabela, permitindo visualizar múltiplos registros de uma só vez.

**Quando Usar:** Utilize a Tree View quando precisar listar registros de forma compacta e permitir ações em massa.

**Sintaxe do Registro:**
```xml
<record id="view_model_tree" model="ir.ui.view">
    <field name="name">model.tree</field>
    <field name="model">model.name</field>
    <field name="arch" type="xml">
        <tree>
            <field name="field1"/>
            <field name="field2"/>
            <!-- Adicione mais campos conforme necessário -->
        </tree>
    </field>
</record>
```

### Form View
**Descrição:** A Form View exibe um único registro em um formato detalhado, permitindo a edição de seus campos.

**Quando Usar:** Utilize a Form View quando precisar visualizar ou editar detalhes de um único registro.

**Sintaxe do Registro:**
```xml
<record id="view_model_form" model="ir.ui.view">
    <field name="name">model.form</field>
    <field name="model">model.name</field>
    <field name="arch" type="xml">
        <form>
            <group>
                <field name="field1"/>
                <field name="field2"/>
                <!-- Adicione mais campos conforme necessário -->
            </group>
        </form>
    </field>
</record>
```

### Search View
**Descrição:** A Search View permite a busca e filtragem de registros, incluindo opções de agrupamento (group by) e filtros personalizados.

**Quando Usar:** Utilize a Search View para facilitar a localização de registros específicos e aplicar filtros ou agrupamentos.

**Sintaxe do Registro:**
```xml
<record id="view_model_search" model="ir.ui.view">
    <field name="name">model.search</field>
    <field name="model">model.name</field>
    <field name="arch" type="xml">
        <search>
            <field name="field1"/>
            <field name="field2"/>
            <!-- Adicione mais campos conforme necessário -->
            <filter string="Filtro Personalizado" name="custom_filter" domain="[('field', '=', 'value')]"/>
            <group string="Agrupar por Campo" name="group_by_field" context="{'group_by':'field'}"/>
        </search>
    </field>
</record>
```