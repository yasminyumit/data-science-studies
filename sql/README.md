---

# 🗄️ Repositório de Scripts Oracle SQL (DDL, DML & DQL)

[![Oracle](https://img.shields.io/badge/Oracle-F80000?style=for-the-badge&logo=oracle&logoColor=white)](https://www.oracle.com/database/)
[![SQL](https://img.shields.io/badge/Language-SQL-blue?style=for-the-badge&logo=sqlite&logoColor=white)](#)
[![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-success?style=for-the-badge)](#)

Documentação e organização dos scripts SQL desenvolvidos para o banco de dados **Oracle Database 21c**, contemplando definições de estrutura (DDL), carga de dados (DML) e consultas de dados (DQL/DRS).

---

## 📌 Sumário
- [🚀 Visão Geral](#-visão-geral)
- [📂 Estrutura de Arquivos](#-estrutura-de-arquivos)
- [🧩 Módulos e Tabelas](#-módulos-e-tabelas)
  - [1. Módulo SIP (Gestão de Implantação e Projetos)](#1-módulo-sip-gestão-de-implantação-e-projetos)
  - [2. Módulo SPV (Sistema de Ponto de Venda)](#2-módulo-spv-sistema-de-ponto-de-venda)
- [🛠️ Boas Práticas e Recursos Aplicados](#️-boas-práticas-e-recursos-aplicados)
- [⚙️ Sequência de Execução](#️-sequência-de-execução)
- [💻 Como Executar](#-como-executar)

---

## 🚀 Visão Geral

Este repositório reúne os scripts SQL referentes a dois domínios de negócio estruturados no Oracle Database:
1. **SIP (Sistema de Implantação e Projetos):** Focado no controle de setores, colaboradores, dependentes, projetos de TI e alocação de equipes (implantações).
2. **SPV (Sistema de Ponto de Venda):** Modelado via Oracle SQL Developer Data Modeler para gerenciamento de clientes, produtos, unidades comerciais, classificações fiscais (CFOP) e faturamento de notas fiscais.

---

## 📂 Estrutura de Arquivos

```text
.
├── 📁 sql/
│   ├── 01_ddl_sip.sql       # DDL do sistema SIP (Criação de tabelas, PKs, FKs, CHECKS e Comentários)
│   ├── 02_ddl_spv.sql       # DDL do sistema SPV (Gerado no Data Modeler 24.3 para Oracle 21c)
│   └── 03_dml_dql_sip.sql   # Carga inicial de dados (INSERT) e consultas de verificação (SELECT)
└── README.md                # Documentação do projeto
