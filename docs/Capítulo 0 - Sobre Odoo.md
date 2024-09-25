# Odoo: Estrutura em Três Camadas

Odoo é uma plataforma de gestão empresarial que adota uma arquitetura em três camadas, proporcionando flexibilidade e escalabilidade. As três camadas principais são:

## 1. Camada de Apresentação
A camada de apresentação é responsável pela interface do usuário e pela interação com o sistema. As ferramentas utilizadas nesta camada incluem:

- **HTML/CSS**: Para a estrutura e o estilo das páginas.

- **JavaScript**: Para a interatividade e dinamismo das interfaces.

- **QWeb**: O motor de templates do Odoo, que permite a renderização de páginas dinâmicas.

## 2. Camada de Lógica de Negócio
Esta camada contém a lógica de negócios e as regras que governam o funcionamento do sistema. As ferramentas e tecnologias utilizadas incluem:

- **Python**: A linguagem principal para o desenvolvimento de módulos e funcionalidades.

- **Odoo ORM (Object-Relational Mapping)**: Facilita a interação com o banco de dados, permitindo manipulação de dados de forma abstrata e eficiente.

- **Serviços Web (XML-RPC/JSON-RPC)**: Para integração com outros sistemas e serviços.

## 3. Camada de Persistência
A camada de persistência é responsável pelo armazenamento e recuperação de dados. As ferramentas utilizadas nesta camada incluem:

- **PostgreSQL**: O banco de dados relacional utilizado pelo Odoo para armazenar dados de forma segura e eficiente.

- **Odoo ORM**: Também atua nesta camada, mapeando objetos Python para tabelas do banco de dados.

Essa arquitetura em três camadas permite que o Odoo seja altamente modular e extensível, facilitando a personalização e a integração com outras soluções empresariais.


