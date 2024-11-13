import oracledb
from datetime import datetime

# Define a classe que irá gerenciar as operações no banco de dados
class IrrigacaoAutomatizadaDB:
    # Método de inicialização, estabelece uma conexão com o banco de dados Oracle
    def __init__(self, user, password, dsn):
        self.connection = oracledb.connect(user="rm559858", password="150306", dsn="oracle.fiap.com.br:1521/ORCL")
        self.cursor = self.connection.cursor()

    # Método para inserir uma nova fazenda na tabela 'Fazenda'
    def criar_fazenda(self, id_fazenda, nome_fazenda, estado_fazenda, cidade_fazenda):
        sql = """
        INSERT INTO Fazenda (id_fazenda, nome_fazenda, estado_fazenda, cidade_fazenda)
        VALUES (:1, :2, :3, :4)
        """
        # Executa a query com os dados passados como parâmetros e realiza o commit
        self.cursor.execute(sql, (id_fazenda, nome_fazenda, estado_fazenda, cidade_fazenda))
        self.connection.commit()

    # Método para inserir um novo plantio na tabela 'Plantio'
    def criar_plantio(self, id_plantio, cultura_plantio, area_total, latitude_plantio, longitude_plantio, fazenda_id_fazenda):
        sql = """
        INSERT INTO Plantio (id_plantio, cultura_plantio, area_total, latitude_plantio, longitude_plantio, fazenda_id_fazenda)
        VALUES (:1, :2, :3, :4, :5, :6)
        """
        # Executa a query com os dados do plantio e realiza o commit
        self.cursor.execute(sql, (id_plantio, cultura_plantio, area_total, latitude_plantio, longitude_plantio, fazenda_id_fazenda))
        self.connection.commit()

    # Método para inserir um novo sensor na tabela 'Sensor'
    def criar_sensor(self, id_sensor, nome_sensor):
        sql = """
        INSERT INTO Sensor (id_sensor, nome_sensor)
        VALUES (:1, :2)
        """
        # Executa a query para adicionar um sensor e realiza o commit
        self.cursor.execute(sql, (id_sensor, nome_sensor))
        self.connection.commit()

    # Método para inserir uma nova medição na tabela 'Medicao'
    def criar_medicao(self, id_valores, valor_medido, data_medicao, plantio_id_plantio, sensor_id_sensor):
        sql = """
        INSERT INTO Medicao (id_valores, valor_medido, data_medicao, plantio_id_plantio, sensor_id_sensor)
        VALUES (:1, :2, :3, :4, :5)
        """
        # Executa a query de inserção com os dados da medição e realiza o commit
        self.cursor.execute(sql, (id_valores, valor_medido, data_medicao, plantio_id_plantio, sensor_id_sensor))
        self.connection.commit()

    # Método para inserir um novo insumo na tabela 'Insumo'
    def criar_insumo(self, id_insumo, nome_insumo):
        sql = """
        INSERT INTO Insumo (id_insumo, nome_insumo)
        VALUES (:1, :2)
        """
        # Executa a query para adicionar o insumo e realiza o commit
        self.cursor.execute(sql, (id_insumo, nome_insumo))
        self.connection.commit()

    # Método para inserir uma nova aplicação de insumo na tabela 'AplicacaoInsumo'
    def criar_aplicacao_insumo(self, id_aplicacao, data_aplicacao, medicao_id_valores, insumo_id_insumo):
        sql = """
        INSERT INTO AplicacaoInsumo (id_aplicacao, data_aplicacao, medicao_id_valores, insumo_id_insumo)
        VALUES (:1, :2, :3, :4)
        """
        # Executa a query para adicionar a aplicação de insumo e realiza o commit
        self.cursor.execute(sql, (id_aplicacao, data_aplicacao, medicao_id_valores, insumo_id_insumo))
        self.connection.commit()

    # Método para inserir um novo registro na tabela 'Valores'
    def criar_valores(self, id_valores, qtde_insumo_total, qtde_horas_gasta, qtde_insumo_metro, valor_custo_aplicacao, data_valores, aplicacao_id_aplicacao):
        sql = """
        INSERT INTO Valores (id_valores, qtde_insumo_total, qtde_horas_gasta, qtde_insumo_metro, valor_custo_aplicacao, data_valores, aplicacao_id_aplicacao)
        VALUES (:1, :2, :3, :4, :5, :6, :7)
        """
        # Executa a query para adicionar o registro de valores e realiza o commit
        self.cursor.execute(sql, (id_valores, qtde_insumo_total, qtde_horas_gasta, qtde_insumo_metro, valor_custo_aplicacao, data_valores, aplicacao_id_aplicacao))
        self.connection.commit()

    # Método para consultar uma fazenda pelo ID na tabela 'Fazenda'
    def ler_fazenda(self, id_fazenda):
        sql = "SELECT * FROM Fazenda WHERE id_fazenda = :1"
        self.cursor.execute(sql, (id_fazenda,))
        # Retorna o primeiro resultado encontrado
        return self.cursor.fetchone()

    # Exemplo de método para atualizar dados, nesse caso, o nome de um sensor na tabela 'Sensor'
    def atualizar_sensor(self, id_sensor, novo_nome_sensor):
        sql = """
        UPDATE Sensor
        SET nome_sensor = :1
        WHERE id_sensor = :2
        """
        # Executa a query de atualização com os novos dados e realiza o commit
        self.cursor.execute(sql, (novo_nome_sensor, id_sensor))
        self.connection.commit()

    # Método para deletar um registro de medição da tabela 'Medicao'
    def deletar_medicao(self, id_valores):
        sql = "DELETE FROM Medicao WHERE id_valores = :1"
        # Executa a query de exclusão e realiza o commit
        self.cursor.execute(sql, (id_valores,))
        self.connection.commit()

    # Método para fechar a conexão com o banco de dados e liberar os recursos
    def fechar_conexao(self):
        self.cursor.close()
        self.connection.close()


# Exemplo de uso da classe IrrigacaoAutomatizadaDB
# if __name__ == "__main__":, a classe é instanciada e métodos de exemplo são chamados para demonstrar a funcionalidade.
if __name__ == "__main__":
    # Conecta ao banco de dados com as credenciais fornecidas
    db = IrrigacaoAutomatizadaDB("user", "password", "dsn")
    
    # Inserir uma nova fazenda
    db.criar_fazenda(1, "Fazenda Verde", "SP", "Ribeirão Preto")

    # Inserir um plantio associado à fazenda
    db.criar_plantio(1, "Soja", 100, "-21.174", "-47.810", 1)

    # Inserir um sensor
    db.criar_sensor(1, "Sensor de Umidade DHT22")

    # Inserir uma medição para o plantio e sensor definidos
    db.criar_medicao(1, 78.5, datetime.now(), 1, 1)

    # Fechar a conexão ao finalizar as operações
    db.fechar_conexao()
