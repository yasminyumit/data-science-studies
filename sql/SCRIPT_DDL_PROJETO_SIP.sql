-- SCRIPT (PASSO A PASSO) DDL
-- SQL -> LINGUAGEM ESTRUTURADA PARA CONSULTA
-- DIVISÃO DDL -> LINGUAGEM DE DEFINIÇÃO DE DADOS
-- COMANDOS: CREATE, ALTER E DROP TABLE
-- PARA MANTER A ESTRUTURA DO BANCO DE DADOS

-- BOAS PRÁTICAS DE PROGRAMAÇÃO
-- 1) COMANDOS DE DELEÇÃO NO INICIO DO ARQUIVO OU EM UM ARQUIVO SEPARADO, QUE
--    PODEMOS CHAMAR DE APAGA.SQL
-- 2) CRIAÇÃO DA TABELA (CREATE), ONDE INFORMAMOS CAMPOS, TIPO DE DADO, TAMANHO,
--    E OBRIGATORIEDADE ( E DEFAULT QUANDO SE APLICAR)
-- 3) ALTERAMOS AS TABELAS INSERINDO AS CONSTRAINTS: PK, UNIQUE, CHECK
-- 4) ALTERAMOS AS TABELAS INSERINDO AS CHAVES ESTRANGEIRAS-
--    AS CHAVES ESTRANGEIRAS SÃO INSERIDAS TODAS DE UMA VEZ NO FINAL DO ARQUIVO
--    PORQUE PRECISAMOS DAS TABELAS CRIADAS PARA PODER RELACIONAR


-- COMANDOS PARA DELEÇÃO DA ESTRUTURA DA TABELA
-- DROP TABLE --> APAGA A TABELA INTEIRA, INCLUINDO DADOS SE EXISTIR
-- OPÇÃO: CASCADE CONSTRAINT -> APAGA O RELACIONAMENTO, ANTES DE APAGAR A
-- TABELA. SENÃO NÃO É POSSIVEL DELETAR A TABELA RELACIONADA
/*
DROP TABLE T_SIP_DEPARTAMENTO CASCADE CONSTRAINTS ;
DROP TABLE T_SIP_DEPENDENTE CASCADE CONSTRAINTS ;
DROP TABLE T_SIP_FUNCIONARIO CASCADE CONSTRAINTS ;
DROP TABLE T_SIP_IMPLANTACAO CASCADE CONSTRAINTS ;
DROP TABLE T_SIP_PROJETO CASCADE CONSTRAINTS ;
*/

-- COMENTARIO DE BLOCO
-- /* ....BLOCO .... */
-- COMENTARIO DE LINHA É --

-- CRIAÇÃO DA TABELA
CREATE TABLE T_SIP_DEPARTAMENTO 
    ( 
     cd_departamento NUMBER (3)     NOT NULL , 
     nm_departamento VARCHAR2 (30)  NOT NULL , 
     sg_departamento CHAR (3)       NOT NULL 
    ) 
;

-- COMENTÁRIOS
COMMENT ON TABLE T_SIP_DEPARTAMENTO IS 
'Refere-se aos setores da empresa onde os funcionários 
estão alocados para exercerem suas funções.';

COMMENT ON COLUMN T_SIP_DEPARTAMENTO.cd_departamento IS 
'RN16 - Um departamento é identificado por um código numérico de três dígitos.';

COMMENT ON COLUMN T_SIP_DEPARTAMENTO.nm_departamento IS 'RN21 - Não existem nomes de departamentos repetidos.
' 
;

COMMENT ON COLUMN T_SIP_DEPARTAMENTO.sg_departamento IS 'sigla com três letras
' 
;

-- ADICIONAR A CHAVE PRIMARIA
   ALTER TABLE T_SIP_DEPARTAMENTO 
ADD CONSTRAINT PK_T_SIP_DEPARTAMENTO PRIMARY KEY ( cd_departamento ) ;

   ALTER TABLE T_SIP_DEPARTAMENTO 
ADD CONSTRAINT UN_T_SIP_DEPTO_NOME UNIQUE ( nm_departamento ) ;

-- CRIAÇÃO DA TABELA DEPENDENTE
CREATE TABLE T_SIP_DEPENDENTE 
    ( 
     nr_matricula  NUMBER (5)       NOT NULL , 
     cd_dependente NUMBER (2)       NOT NULL , 
     nm_dependente VARCHAR2 (60)    NOT NULL , 
     dt_nascimento DATE             NOT NULL 
    ) 
;

COMMENT ON TABLE T_SIP_DEPENDENTE IS 'São pessoas que possuem um grau de parentesco com o funcionário, por exemplo: filhos, esposa ou marido.
'
;

COMMENT ON COLUMN T_SIP_DEPENDENTE.cd_dependente IS 'RN18 - Um dependente é identificado pelo código numérico de até dois dígitos e o número de matrícula do funcionário que ele depende.
' 
;

COMMENT ON COLUMN T_SIP_DEPENDENTE.dt_nascimento IS 'RN 28 - A data de nascimento é obrigatória (não pode ser nula).
' 
;

-- CONSTRAINT CHAVE PRIMARIA
   ALTER TABLE T_SIP_DEPENDENTE 
ADD CONSTRAINT PK_T_SIP_DEPENDENTE PRIMARY KEY ( cd_dependente, nr_matricula ) ;
-- CHAVE PRIMARIA COMPOSTA --> CAMPOS SEPARADOS POR VÍRGULA

CREATE TABLE T_SIP_FUNCIONARIO 
    ( 
     nr_matricula      NUMBER (5)  NOT NULL , 
     cd_departamento   NUMBER (3)  NOT NULL , 
     nm_funcionario    VARCHAR2 (60)  NOT NULL , 
     dt_nascimento     DATE  NOT NULL , 
     dt_admissao       DATE  NOT NULL , 
     ds_endereco       VARCHAR2 (100)  NOT NULL , 
     vl_salario_mensal NUMBER (7,2)  NOT NULL 
    ) 
;

COMMENT ON TABLE T_SIP_FUNCIONARIO IS 'Representa os colaboradores contratados pela empresa para atuar nos projetos e departamentos.
'
;

COMMENT ON COLUMN T_SIP_FUNCIONARIO.nr_matricula IS ' RN 17 - Um funcionário é identificado por uma matrícula numérica de cinco dígitos.
 RN 03 - Um funcionário possui um único número de matrícula.

' 
;

COMMENT ON COLUMN T_SIP_FUNCIONARIO.dt_nascimento IS 'RN28 - A data de nascimento é obrigatória.
' 
;

COMMENT ON COLUMN T_SIP_FUNCIONARIO.dt_admissao IS 'RN02 - Um funcionário possui apenas uma data de admissão.
' 
;

COMMENT ON COLUMN T_SIP_FUNCIONARIO.ds_endereco IS 'RN01 - Um funcionário possui apenas um endereço, o endereço residencial.
' 
;

COMMENT ON COLUMN T_SIP_FUNCIONARIO.vl_salario_mensal IS 'RN 22- O salário deve ser maior ou igual ao salário mínimo (R$ 1.412,00).

|------7-----| PRECISAO
  99.999,99
              |2| ESCALA
' 
;
-- CONSTRAINT CHECK
   ALTER TABLE T_SIP_FUNCIONARIO 
ADD CONSTRAINT CK_T_SIP_FUNC_SALARIO 
         CHECK (VL_SALARIO_MENSAL >= 1621); -- REGRA DE VALIDAÇÃO

-- CONSTRAINT PRIMARY KEY
   ALTER TABLE T_SIP_FUNCIONARIO 
ADD CONSTRAINT PK_T_SIP_FUNCIONARIO 
   PRIMARY KEY ( nr_matricula ) ;

-- CRIAÇÃO DA TABELA IMPLANTACAO
CREATE TABLE T_SIP_IMPLANTACAO 
    ( 
     cd_projeto     NUMBER (5)  NOT NULL , 
     cd_implantacao NUMBER (3)  NOT NULL , 
     nr_matricula   NUMBER (5)  NOT NULL , 
     dt_entrada     DATE        NOT NULL , 
     dt_saida       DATE            NULL   -- CAMPO OPCIONAL
    ) 
;

COMMENT ON TABLE T_SIP_IMPLANTACAO IS 'Refere-se aos projetos desenvolvidos ou que estão em desenvolvimento, bem como os funcionários que estão desempenhando tarefas nestes projetos e em qual período.
Cada implantação refere-se a um período, em que um funcionário atuou em um determinado projeto.

'
;

COMMENT ON COLUMN T_SIP_IMPLANTACAO.cd_implantacao IS 'RN20 - Uma implantação é identificada pelo código da implantação, numérico com até três dígitos e pelo código do projeto que esta implantação pertence.

' 
;

COMMENT ON COLUMN T_SIP_IMPLANTACAO.dt_saida IS 'RN 25 - A data de saída da implantação deve ser maior que a data de entrada.
RN 30 - Funcionários ainda atuando no projeto não possuem data de saída preenchida.
' 
;
-- CONSTRAINT CHECK
ALTER TABLE T_SIP_IMPLANTACAO 
    ADD CONSTRAINT CK_T_SIP_IMPLANT_DATA 
    CHECK (DT_SAIDA > DT_ENTRADA)
;
-- CONSTRAINT PRIMARY KEY
ALTER TABLE T_SIP_IMPLANTACAO 
    ADD CONSTRAINT PK_T_SIP_IMPLANTACAO 
    PRIMARY KEY ( cd_implantacao, cd_projeto ) ;
    -- CHAVE PRIMARIA COMPOSTA

CREATE TABLE T_SIP_PROJETO 
    ( 
     cd_projeto NUMBER (5)              NOT NULL , 
     nm_projeto VARCHAR2 (40)           NOT NULL , 
     dt_inicio  DATE DEFAULT SYSDATE    NOT NULL , -- CONSTRAINT DEFAULT
     dt_termino DATE                        NULL   -- CAMPO OPCIONAL
    ) 
;

COMMENT ON TABLE T_SIP_PROJETO IS 'Somos uma empresa que desenvolvemos soluções de TI. Desenvolvemos projetos para todas as áreas da TI.
'
;

COMMENT ON COLUMN T_SIP_PROJETO.cd_projeto IS 'RN19 - Um projeto é identificado por um código numérico de cinco caracteres.
' 
;

COMMENT ON COLUMN T_SIP_PROJETO.nm_projeto IS 'RN 23 - Não pode haver dois projetos com o mesmo nome.
' 
;

COMMENT ON COLUMN T_SIP_PROJETO.dt_termino IS 'RN 24- A data de término de um projeto deve ser maior que a data de início.
RN 29 - Projetos em andamento não possuem data de término preenchida.

' 
;
-- CONSTRAINT CHECK
ALTER TABLE T_SIP_PROJETO 
    ADD CONSTRAINT CK_T_SIP_PROJETO_DATA 
    CHECK (DT_TERMINO > DT_INICIO)
;
-- CONSTRAINT PRIMARY KEY
ALTER TABLE T_SIP_PROJETO 
    ADD CONSTRAINT PK_T_SIP_PROJETO PRIMARY KEY ( cd_projeto ) ;

-- CHAVES ESTRANGEIRAS -- ATENÇÃO: APÓS A CRIAÇÃO DE TODAS AS TABELAS
-- E RESPECTIVAS CHAVES PRIMARIAS
-- RELACIONAMENTO ENTRE DEPENDENTE (DESTINO) E FUNCIONARIO (ORIGEM)
ALTER TABLE T_SIP_DEPENDENTE 
    ADD CONSTRAINT FK_T_SIP_DEPENDENTE_FUNC FOREIGN KEY 
    ( 
     nr_matricula -- NOME DO CAMPO FK NA TABELA DEPENDENTE
    ) 
    REFERENCES T_SIP_FUNCIONARIO -- TABELA ORIGEM DO RELACIONAMENTO
    ( 
     nr_matricula -- NOME DO CAMPO PK NA TABELA ORIGEM FUNCIONARIO
    ) 
;

-- RELACIONAMENTO ENTRE FUNCIONARIO E DEPARTAMENTO
ALTER TABLE T_SIP_FUNCIONARIO 
    ADD CONSTRAINT FK_T_SIP_FUNC_DEPTO FOREIGN KEY 
    ( 
     cd_departamento
    ) 
    REFERENCES T_SIP_DEPARTAMENTO 
    ( 
     cd_departamento
    ) 
;

-- RELACIONAMENTO ENTRE IMPLANTACAO E FUNCIONARIO
ALTER TABLE T_SIP_IMPLANTACAO 
    ADD CONSTRAINT FK_T_SIP_IMPLANT_FUNC FOREIGN KEY 
    ( 
     nr_matricula
    ) 
    REFERENCES T_SIP_FUNCIONARIO 
    ( 
     nr_matricula
    ) 
;
-- RELACIONAMENTO ENTRE IMPLANTACAO E PROJETO
ALTER TABLE T_SIP_IMPLANTACAO 
    ADD CONSTRAINT FK_T_SIP_IMPLANT_PROJETO FOREIGN KEY 
    ( 
     cd_projeto
    ) 
    REFERENCES T_SIP_PROJETO 
    ( 
     cd_projeto
    ) 
;



-- Relatório do Resumo do Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                             5
-- CREATE INDEX                             0
-- ALTER TABLE                             13
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
