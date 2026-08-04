-- Gerado por Oracle SQL Developer Data Modeler 24.3.1.351.0831
--   em:        2026-08-04 09:05:47 BRT
--   site:      Oracle Database 21c
--   tipo:      Oracle Database 21c



DROP TABLE T_SPV_CLASSIF_FISCAL CASCADE CONSTRAINTS 
;

DROP TABLE T_SPV_CLIENTE CASCADE CONSTRAINTS 
;

DROP TABLE T_SPV_ITEM_NF CASCADE CONSTRAINTS 
;

DROP TABLE T_SPV_NOTA_FISCAL CASCADE CONSTRAINTS 
;

DROP TABLE T_SPV_PRODUTO CASCADE CONSTRAINTS 
;

DROP TABLE T_SPV_UNID_CML CASCADE CONSTRAINTS 
;

-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE T_SPV_CLASSIF_FISCAL 
    ( 
     nr_cfop          NUMBER (4)  NOT NULL , 
     nr_tipo_operacao NUMBER (1)  NOT NULL , 
     nm_natureza_op   VARCHAR2 (60)  NOT NULL , 
     ds_natureza_op   VARCHAR2 (500)  NOT NULL 
    ) 
;

COMMENT ON COLUMN T_SPV_CLASSIF_FISCAL.nr_cfop IS 'RN24-O número do CFOP é um número com quatro dígitos, que identifica a classificação fiscal.
' 
;

COMMENT ON COLUMN T_SPV_CLASSIF_FISCAL.nr_tipo_operacao IS 'RN29-O tipo de operação, especificado no código fiscal, deve ser 1- Entrada ou 2- Saída.
' 
;

COMMENT ON COLUMN T_SPV_CLASSIF_FISCAL.nm_natureza_op IS 'RN20- Natureza da operação, descrição da unidade de medida, descrição de um produto são informações que não se repetem dentro do nosso cadastro.
' 
;

ALTER TABLE T_SPV_CLASSIF_FISCAL 
    ADD CONSTRAINT CK_T_SPV_CLASSIF_TIPO 
    CHECK (NR_TIPO_OPERACAO = 1 OR NR_TIPO_OPERACAO = 2)
;
ALTER TABLE T_SPV_CLASSIF_FISCAL 
    ADD CONSTRAINT PK_T_SPV_CLASSIF_FISCAL PRIMARY KEY ( nr_cfop ) ;

ALTER TABLE T_SPV_CLASSIF_FISCAL 
    ADD CONSTRAINT UN_T_SPV_CLASSIF_DESC UNIQUE ( nm_natureza_op ) ;

CREATE TABLE T_SPV_CLIENTE 
    ( 
     cd_cliente    NUMBER (5)  NOT NULL , 
     nm_cliente    VARCHAR2 (60)  NOT NULL , 
     dt_nascimento DATE , 
     ds_genero     CHAR (2)  NOT NULL , 
     ds_endereco   VARCHAR2 (100)  NOT NULL , 
     nr_telefone   NUMBER (11) , 
     ds_email      VARCHAR2 (80) , 
     nr_cpf        NUMBER (9)  NOT NULL , 
     nr_cpf_digito NUMBER (2)  NOT NULL , 
     nr_rg         NUMBER (8)  NOT NULL , 
     nr_rg_digito  CHAR (1)  NOT NULL 
    ) 
;

COMMENT ON COLUMN T_SPV_CLIENTE.cd_cliente IS 'RN23 - Um cliente é identificado por um código numérico de cinco dígitos atribuído internamente.
' 
;

COMMENT ON COLUMN T_SPV_CLIENTE.dt_nascimento IS 'RN03- Pode informar data de nascimento (opcional) para descontos/brindes.
' 
;

COMMENT ON COLUMN T_SPV_CLIENTE.ds_genero IS 'RN05-Gêneros aplicados: Homem (H), Mulher (M) e não binário (NB).
' 
;

COMMENT ON COLUMN T_SPV_CLIENTE.ds_endereco IS 'RN01 - Deve possuir um endereço residencial (pode ser de entrega) e opcionalmente endereço diferenciado para entrega e cobrança.
' 
;

COMMENT ON COLUMN T_SPV_CLIENTE.nr_telefone IS 'RN02- Pode ter vários telefones (residencial, comercial, celular) ou nenhum. Armazenar DDD + número.

99 99999-9999' 
;

COMMENT ON COLUMN T_SPV_CLIENTE.ds_email IS 'RN04- Pode informar seu e-mail, caso tenha um.
' 
;

COMMENT ON COLUMN T_SPV_CLIENTE.nr_cpf IS 'RN30 - O CPF deve ser decomposto em duas partes: o número e o dígito verificador.

999.999.999-99' 
;

COMMENT ON COLUMN T_SPV_CLIENTE.nr_rg IS 'RN31- O RG deve ser decomposto em duas partes: o número e o dígito verificador (pode ser letra).

99.999.999-X

99.999.999-9
' 
;

ALTER TABLE T_SPV_CLIENTE 
    ADD CONSTRAINT CK_T_SPV_CLIENTE_GENERO 
    CHECK (UPPER(DS_GENERO) = 'H' OR UPPER(DS_GENERO) = 'M' OR UPPER(DS_GENERO) = 'NB'
)
;
ALTER TABLE T_SPV_CLIENTE 
    ADD CONSTRAINT PK_T_SPV_CLIENTE PRIMARY KEY ( cd_cliente ) ;

CREATE TABLE T_SPV_ITEM_NF 
    ( 
     nr_nota_fiscal    NUMBER (5)  NOT NULL , 
     cd_produto        NUMBER (5)  NOT NULL , 
     qt_comercializada NUMBER (3)  NOT NULL , 
     vl_preco_unitario NUMBER (7,2)  NOT NULL , 
     vl_total_item     NUMBER (10,2)  NOT NULL 
    ) 
;

COMMENT ON COLUMN T_SPV_ITEM_NF.qt_comercializada IS 'RN32-Quantidade vendida deve ser um número maior que zero.
' 
;

COMMENT ON COLUMN T_SPV_ITEM_NF.vl_preco_unitario IS 'RN33- Preço unitário do produto deve ser um número decimal maior que zero.
' 
;

COMMENT ON COLUMN T_SPV_ITEM_NF.vl_total_item IS 'RN34-Cálculo para o Preço (valor) total do Item = Quantidade Vendida * Preço Unitário (momento da venda).
' 
;

ALTER TABLE T_SPV_ITEM_NF 
    ADD CONSTRAINT CK_T_SPV_ITEM_NF_QTDE 
    CHECK (QT_COMERCIALIZADA > 0)
;


ALTER TABLE T_SPV_ITEM_NF 
    ADD CONSTRAINT CK_T_SPV_ITEM_NF_PREUNI 
    CHECK (VL_PRECO_UNITARIO > 0)
;
ALTER TABLE T_SPV_ITEM_NF 
    ADD CONSTRAINT PK_T_SPV_ITEM_NF PRIMARY KEY ( cd_produto, nr_nota_fiscal ) ;

CREATE TABLE T_SPV_NOTA_FISCAL 
    ( 
     nr_nota_fiscal NUMBER (5)  NOT NULL , 
     cd_cliente     NUMBER (5)  NOT NULL , 
     nr_cfop        NUMBER (4)  NOT NULL , 
     dt_emissao     DATE  NOT NULL , 
     dt_saida       DATE  NOT NULL , 
     vl_desconto    NUMBER (3,1) DEFAULT 0  NOT NULL , 
     vl_total_nf    NUMBER (11,2)  NOT NULL 
    ) 
;

COMMENT ON COLUMN T_SPV_NOTA_FISCAL.nr_nota_fiscal IS 'RN25-O número da nota fiscal é um número com cinco dígitos, que identifica uma nota fiscal.
' 
;

COMMENT ON COLUMN T_SPV_NOTA_FISCAL.dt_saida IS 'RN36-A data da saída da nota fiscal deve ser maior ou igual à data da emissão da nota fiscal.
' 
;

COMMENT ON COLUMN T_SPV_NOTA_FISCAL.vl_desconto IS 'RN06-Um cliente pode ter desconto em várias compras. O desconto praticado é informado na própria nota fiscal.

RN21-O valor do desconto varia de 0,0% a 25,0%, nunca ultrapassando este valor. Quando nenhum desconto for praticado, deve-se armazenar ZERO.

RN22-Deve-se armazenar o valor do desconto como um valor decimal. E durante o cálculo aplicar a ideia de percentual.
' 
;

COMMENT ON COLUMN T_SPV_NOTA_FISCAL.vl_total_nf IS 'RN35-Cálculo para o valor total da nota fiscal = Somatória de todos os preços totais de cada item comercializado na referida nota fiscal.
' 
;

ALTER TABLE T_SPV_NOTA_FISCAL 
    ADD CONSTRAINT CK_T_SPV_NOTA_FISCAL_DATA 
    CHECK (DT_SAIDA >= DT_EMISSAO)
;


ALTER TABLE T_SPV_NOTA_FISCAL 
    ADD CONSTRAINT CK_T_SPV_NOTA_FISCAL_DESC 
    CHECK (VL_DESCONTO >= 0 AND VL_DESCONTO <= 25)
;
ALTER TABLE T_SPV_NOTA_FISCAL 
    ADD CONSTRAINT PK_T_SPV_NOTA_FISCAL PRIMARY KEY ( nr_nota_fiscal ) ;

CREATE TABLE T_SPV_PRODUTO 
    ( 
     cd_produto          NUMBER (5)  NOT NULL , 
     cd_unid_cml         NUMBER (3)  NOT NULL , 
     ds_produto          VARCHAR2 (100)  NOT NULL , 
     ds_completa_produto VARCHAR2 (500)  NOT NULL , 
     qt_estoque          NUMBER (3)  NOT NULL , 
     vl_preco_unitario   NUMBER (7,2)  NOT NULL 
    ) 
;

COMMENT ON COLUMN T_SPV_PRODUTO.cd_produto IS 'RN28-Um produto é identificado por um código numérico de cinco dígitos atribuído internamente pela empresa.
' 
;

COMMENT ON COLUMN T_SPV_PRODUTO.ds_produto IS 'RN20-A descrição de um produto é uma informação que não se repete dentro do nosso cadastro.
' 
;

COMMENT ON COLUMN T_SPV_PRODUTO.vl_preco_unitario IS 'RN33-Preço unitário do produto deve ser um número decimal maior que zero.
' 
;

ALTER TABLE T_SPV_PRODUTO 
    ADD CONSTRAINT CK_T_SPV_PRODUTO_PREUNI 
    CHECK (VL_PRECO_UNITARIO > 0)
;
ALTER TABLE T_SPV_PRODUTO 
    ADD CONSTRAINT PK_T_SPV_PRODUTO PRIMARY KEY ( cd_produto ) ;

ALTER TABLE T_SPV_PRODUTO 
    ADD CONSTRAINT UN_T_SPV_PRODUTO_DESC UNIQUE ( ds_produto ) ;

CREATE TABLE T_SPV_UNID_CML 
    ( 
     cd_unid_cml NUMBER (3)  NOT NULL , 
     ds_unid_cml VARCHAR2 (25)  NOT NULL , 
     sg_unid_cml CHAR (6)  NOT NULL 
    ) 
;

COMMENT ON COLUMN T_SPV_UNID_CML.cd_unid_cml IS 'RN26-O código da unidade comercial (unidade de medida) é numérico com três dígitos, que identifica uma unidade comercial.
' 
;

COMMENT ON COLUMN T_SPV_UNID_CML.ds_unid_cml IS 'RN20-A descrição da unidade de medida é uma informação que não se repete dentro do nosso cadastro.
' 
;

ALTER TABLE T_SPV_UNID_CML 
    ADD CONSTRAINT PK_T_SPV_UNID_CML PRIMARY KEY ( cd_unid_cml ) ;

ALTER TABLE T_SPV_UNID_CML 
    ADD CONSTRAINT UN_T_SPV_UNID_CML_DESC UNIQUE ( ds_unid_cml ) ;

ALTER TABLE T_SPV_ITEM_NF 
    ADD CONSTRAINT FK_T_SPV_ITEM_NF_NOTA_FISCAL FOREIGN KEY 
    ( 
     nr_nota_fiscal
    ) 
    REFERENCES T_SPV_NOTA_FISCAL 
    ( 
     nr_nota_fiscal
    ) 
;

ALTER TABLE T_SPV_ITEM_NF 
    ADD CONSTRAINT FK_T_SPV_ITEM_NF_PRODUTO FOREIGN KEY 
    ( 
     cd_produto
    ) 
    REFERENCES T_SPV_PRODUTO 
    ( 
     cd_produto
    ) 
;

ALTER TABLE T_SPV_NOTA_FISCAL 
    ADD CONSTRAINT FK_T_SPV_NF_CLASSIF_FISCAL FOREIGN KEY 
    ( 
     nr_cfop
    ) 
    REFERENCES T_SPV_CLASSIF_FISCAL 
    ( 
     nr_cfop
    ) 
;

ALTER TABLE T_SPV_NOTA_FISCAL 
    ADD CONSTRAINT FK_T_SPV_NF_CLIENTE FOREIGN KEY 
    ( 
     cd_cliente
    ) 
    REFERENCES T_SPV_CLIENTE 
    ( 
     cd_cliente
    ) 
;

ALTER TABLE T_SPV_PRODUTO 
    ADD CONSTRAINT FK_T_SPV_PRODUTO_UNID_CML FOREIGN KEY 
    ( 
     cd_unid_cml
    ) 
    REFERENCES T_SPV_UNID_CML 
    ( 
     cd_unid_cml
    ) 
;



-- Relatório do Resumo do Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                             6
-- CREATE INDEX                             0
-- ALTER TABLE                             21
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
