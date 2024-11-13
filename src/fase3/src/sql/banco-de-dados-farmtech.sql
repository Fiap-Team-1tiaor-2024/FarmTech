CREATE TABLE Fazenda (
    id_fazenda INTEGER PRIMARY KEY,
    nome_fazenda VARCHAR2(255),
    estado_fazenda VARCHAR2(2),
    cidade_fazenda VARCHAR2(255)
);

CREATE TABLE Plantio (
    id_plantio INTEGER PRIMARY KEY,
    cultura_plantio VARCHAR2(255),
    area_total NUMBER,
    latitude_plantio VARCHAR2(255),
    longitude_plantio VARCHAR2(255),
    fazenda_id_fazenda INTEGER,
    CONSTRAINT fk_fazenda FOREIGN KEY (fazenda_id_fazenda) REFERENCES Fazenda(id_fazenda)
);

CREATE TABLE Sensor (
    id_sensor INTEGER PRIMARY KEY,
    nome_sensor VARCHAR2(255)
);

CREATE TABLE Medicao (
    id_valores INTEGER PRIMARY KEY,
    valor_medido NUMBER,
    data_medicao TIMESTAMP,
    plantio_id_plantio INTEGER,
    sensor_id_sensor INTEGER,
    CONSTRAINT fk_plantio FOREIGN KEY (plantio_id_plantio) REFERENCES Plantio(id_plantio),
    CONSTRAINT fk_sensor FOREIGN KEY (sensor_id_sensor) REFERENCES Sensor(id_sensor)
);

CREATE TABLE Insumo (
    id_insumo INTEGER PRIMARY KEY,
    nome_insumo VARCHAR2(255)
);

CREATE TABLE AplicacaoInsumo (
    id_aplicacao INTEGER PRIMARY KEY,
    data_aplicacao TIMESTAMP,
    medicao_id_valores INTEGER,
    insumo_id_insumo INTEGER,
    CONSTRAINT fk_medicao FOREIGN KEY (medicao_id_valores) REFERENCES Medicao(id_valores),
    CONSTRAINT fk_insumo FOREIGN KEY (insumo_id_insumo) REFERENCES Insumo(id_insumo)
);

CREATE TABLE Valores (
    id_valores INTEGER PRIMARY KEY,
    qtde_insumo_total NUMBER,
    qtde_horas_gasta NUMBER,
    qtde_insumo_metro NUMBER,
    valor_custo_aplicacao NUMBER,
    data_valores TIMESTAMP,
    aplicacao_id_aplicacao INTEGER,
    CONSTRAINT fk_aplicacao_insumo FOREIGN KEY (aplicacao_id_aplicacao) REFERENCES AplicacaoInsumo(id_aplicacao)
);


// ---------------------------

SELECT * FROM Plantio;
SELECT * FROM Fazenda;
SELECT * FROM Medicao;

COMMIT;
