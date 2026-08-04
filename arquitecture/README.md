# Arquitecture

Este diretório contém a infraestrutura e os componentes necessários para orquestração de workflows de dados utilizando o Apache Airflow. Aqui você encontrará arquivos de configuração, scripts de DAGs, exemplos de plugins e instruções para execução local via Docker.

## Estrutura da Pasta

```
arquitecture/
├── airflow/
│   ├── .env
│   ├── docker-compose.yaml
│   ├── config/
│   │   └── airflow.cfg
│   ├── dags/
│   │   ├── 01_Minha_primeira_DAG.py
│   │   ├── 02_Anatomia_de_uma_DAG.py
│   │   ├── 03_DAG_com_operador_python.py
│   │   ├── 04_DAG_email_operator.py
│   │   └── ...
│   ├── Data Architechture, Analytics and NoSQL Solutions_-_Aula_06_-_Airflow_DAGs/
│   ├── logs/
│   └── plugins/
```

### airflow/

Contém toda a configuração e código relacionado ao Apache Airflow.

- **.env**  
  Variáveis de ambiente utilizadas pelo Docker Compose e pelo Airflow.

- **docker-compose.yaml**  
  Arquivo para subir o ambiente do Airflow utilizando Docker. Inclui serviços como webserver, scheduler, e banco de dados.

- **config/airflow.cfg**  
  Arquivo de configuração principal do Airflow. Permite customizar parâmetros como executor, conexões, paths, etc.

- **dags/**  
  Diretório onde ficam as DAGs (Directed Acyclic Graphs) do Airflow. Cada arquivo `.py` representa um workflow de dados. Exemplos:
  - `01_Minha_primeira_DAG.py`: Exemplo básico de DAG.
  - `02_Anatomia_de_uma_DAG.py`: Explica a estrutura de uma DAG.
  - `03_DAG_com_operador_python.py`: Demonstra uso do PythonOperator.
  - `04_DAG_email_operator.py`: Exemplo de envio de e-mail via Airflow.

- **Data Architechture, Analytics and NoSQL Solutions_-_Aula_06_-_Airflow_DAGs/**  
  Materiais e exemplos complementares da aula 06, focados em Airflow e soluções de arquitetura de dados.

- **logs/**  
  Diretório onde o Airflow armazena os logs de execução das DAGs.

- **plugins/**  
  Plugins customizados para estender funcionalidades do Airflow.

## Como executar o Airflow localmente

1. **Pré-requisitos:**  
   - Docker e Docker Compose instalados.

2. **Configuração:**  
   - Edite o arquivo `.env` conforme necessário para ajustar variáveis de ambiente (como senhas, portas, etc).

3. **Subindo o ambiente:**  
   No terminal, navegue até o diretório `arquitecture/airflow` e execute:
   ```sh
   docker-compose up
   ```

4. **Acessando o Airflow:**  
   - Interface Web: [http://localhost:8080](http://localhost:8080)
   - Usuário e senha padrão podem ser definidos no `.env` ou conforme instruções do `docker-compose.yaml`.

5. **Gerenciando DAGs:**  
   - Coloque seus arquivos `.py` de DAGs na pasta `dags/`.
   - Os logs de execução ficam disponíveis em `logs/`.

## Recomendações

- Consulte os exemplos em `dags/` para aprender a criar e agendar seus próprios workflows.
- Utilize o diretório `plugins/` para adicionar operadores, sensores ou hooks customizados.
- Mantenha o arquivo `airflow.cfg` versionado para garantir reprodutibilidade do ambiente.

---

> Para dúvidas ou sugestões, consulte o [README principal](../README.md) do projeto ou abra uma issue.
