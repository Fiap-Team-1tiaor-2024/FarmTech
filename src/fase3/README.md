# Sistema de Irrigação Automatizada

Este projeto tem como objetivo gerenciar dados relacionados a uma fazenda, incluindo informações sobre o plantio, sensores, medições e aplicações de insumos. O sistema utiliza um banco de dados Oracle para armazenar e manipular essas informações. O projeto é implementado em Python, utilizando a biblioteca `oracledb` para interagir com o banco de dados.

## Estrutura do Banco de Dados

O banco de dados é composto pelas seguintes tabelas:

- **Fazenda**: Armazena informações sobre a fazenda.
- **Plantio**: Contém os dados dos plantios realizados em cada fazenda.
- **Sensor**: Define os sensores utilizados para medir variáveis no ambiente da fazenda.
- **Medicao**: Armazena as medições feitas pelos sensores para cada plantio.
- **Insumo**: Registra os insumos utilizados nos plantios, como fertilizantes e pesticidas.
- **AplicacaoInsumo**: Relaciona as medições com a aplicação de insumos.
- **Valores**: Contém informações detalhadas sobre a aplicação de insumos, como quantidade total utilizada e custo.

Essa estrtura já foi desenvolvida na fase anterior do projeto, seguimos com ela para desenvolver essa atividade.

## Funcionalidades do Sistema

O sistema é capaz de realizar operações de CRUD (Criar, Ler, Atualizar e Deletar) em cada uma das tabelas acima. As principais operações são:

- **Criar**: Inserir novas fazendas, plantios, sensores, medições, insumos, aplicações de insumos e valores.
- **Ler**: Consultar os dados de uma fazenda pelo seu ID.
- **Atualizar**: Modificar o nome de um sensor, por exemplo.
- **Deletar**: Remover uma medição da tabela de medições.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para interagir com o banco de dados.
- **oracledb**: Biblioteca Python usada para conectar ao banco de dados Oracle e executar operações SQL.
- **Oracle Database**: Sistema de gerenciamento de banco de dados usado para armazenar as informações.

## Estrutura do Código

O código está estruturado em uma única classe Python chamada `IrrigacaoAutomatizadaDB`, que contém métodos para realizar as operações no banco de dados. Cada operação é realizada através de uma consulta SQL, que é executada no banco e, em seguida, o commit é feito para garantir que as mudanças sejam persistidas.

### Métodos Principais

- `criar_fazenda(id_fazenda, nome_fazenda, estado_fazenda, cidade_fazenda)`: Insere uma nova fazenda na tabela `Fazenda`.
- `criar_plantio(id_plantio, cultura_plantio, area_total, latitude_plantio, longitude_plantio, fazenda_id_fazenda)`: Insere um novo plantio na tabela `Plantio`.
- `criar_sensor(id_sensor, nome_sensor)`: Insere um novo sensor na tabela `Sensor`.
- `criar_medicao(id_valores, valor_medido, data_medicao, plantio_id_plantio, sensor_id_sensor)`: Insere uma nova medição na tabela `Medicao`.
- `criar_insumo(id_insumo, nome_insumo)`: Insere um novo insumo na tabela `Insumo`.
- `criar_aplicacao_insumo(id_aplicacao, data_aplicacao, medicao_id_valores, insumo_id_insumo)`: Insere uma aplicação de insumo na tabela `AplicacaoInsumo`.
- `criar_valores(id_valores, qtde_insumo_total, qtde_horas_gasta, qtde_insumo_metro, valor_custo_aplicacao, data_valores, aplicacao_id_aplicacao)`: Insere um novo registro de valores na tabela `Valores`.
- `ler_fazenda(id_fazenda)`: Consulta uma fazenda pelo seu ID.
- `atualizar_sensor(id_sensor, novo_nome_sensor)`: Atualiza o nome de um sensor.
- `deletar_medicao(id_valores)`: Deleta uma medição da tabela `Medicao`.
- `fechar_conexao()`: Fecha a conexão com o banco de dados e libera os recursos.

## Como Usar

### Instalação

1. **Instale a biblioteca `oracledb`**:

   ```bash
   pip install oracledb
