# Capítulo 4 - Arquivos de Regra de Segurança

## O que são os arquivos de segurança do Odoo?

Os arquivos de segurança no Odoo, especificamente os arquivos `ir.model.access` em formato CSV, são utilizados para definir as regras de acesso aos modelos de dados. Eles determinam quais grupos de usuários têm permissão para criar, ler, escrever e excluir registros em cada modelo.

## Como usar os arquivos de segurança?

Para usar os arquivos de segurança, você deve criar um arquivo CSV com as regras de acesso e incluí-lo no módulo Odoo. O arquivo deve ser referenciado no manifesto do módulo (`__manifest__.py`) para que seja carregado corretamente.

### Estrutura do arquivo CSV

O arquivo CSV deve conter as seguintes colunas:

- **id**: Identificador único da regra de acesso.
- **name**: Nome descritivo da regra de acesso. 
- **model_id:id**: Referência ao modelo ao qual a regra se aplica.
- **group_id:id**: Referência ao grupo de usuários que a regra afeta.
- **perm_read**: Permissão de leitura (1 para permitir, 0 para negar).
- **perm_write**: Permissão de escrita (1 para permitir, 0 para negar).
- **perm_create**: Permissão de criação (1 para permitir, 0 para negar).
- **perm_unlink**: Permissão de exclusão (1 para permitir, 0 para negar).

### Exemplo de arquivo `ir.model.access.csv`

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_model_example_user,access.model.example.user,model_example,base.group_user,1,1,1,1
access_model_example_manager,access.model.example.manager,model_example,base.group_system,1,1,1,1
```

Neste exemplo, duas regras de acesso são definidas: uma para usuários comuns (`base.group_user`) e outra para administradores (`base.group_system`), ambas com permissões completas sobre o modelo `model_example`.

## Conclusão

Os arquivos de segurança são essenciais para controlar o acesso aos dados no Odoo. Compreender a estrutura e o uso desses arquivos permite configurar corretamente as permissões e garantir a segurança dos dados no sistema.
