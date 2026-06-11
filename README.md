# Heart Health API

## Arquitetura

O projeto foi desenvolvido utilizando FastAPI, um framework web de criação de APIs com Python, e segue uma arquitetura modular dividida em camadas.

### Estrutura

```text
app/
├── database/
├── models/
├── routes/
├── schemas/
├── services/
├── utils/
```

### Camadas

**Routes**

* Responsáveis pelos endpoints da API.
* Recebem requisições e retornam respostas HTTP.

**Services**

* Contêm as regras de negócio da aplicação.
* Realizam o processamento dos dados.

**Models**

* Representam as entidades persistidas no banco de dados.

**Schemas**

* Definem validações e formatos de entrada e saída utilizando Pydantic.

**Database**

* Responsável pela configuração e conexão com o banco de dados.

**Utils**

* Funções auxiliares utilizadas em diferentes partes do sistema.

---

## Funcionalidades

1. Cadastro de usuário
2. Login
3. Acompanhamento da saúde cardíaca
4. Relatório de saúde cardíaca

---

## Testes

O projeto possui testes unitários e testes de integração.

### Testes Unitários

Validam componentes isolados da aplicação:

* test_unit_auth.py
* test_unit_login.py
* test_unit_heart_health.py
* test_unit_heart_report.py

### Testes de Integração

Validam a comunicação entre rotas, serviços e banco de dados:

* test_integration_auth.py
* test_integration_login.py
* test_integration_heart_health_1.py
* test_integration_heart_health_2.py
* test_integration_heart_report.py

### Execução dos testes

```bash
pytest
```

Resultado esperado:

```text
13 passed
```

## Acessando a documentação da API (Swagger UI)

> **Observação:** este tutorial foi elaborado considerando o uso do Visual Studio Code (VS Code) como ambiente de desenvolvimento. Caso utilize outro editor, os passos podem variar.

Para visualizar a documentação da API e testar seus endpoints de forma interativa através do **Swagger UI**, siga as instruções abaixo:

1. Faça o download do arquivo `.zip` e extraia seu conteúdo em uma pasta de sua preferência.

2. Abra o **Visual Studio Code** e selecione a pasta do projeto.

3. No VS Code, acesse **Terminal > New Terminal** para abrir um novo terminal na raiz do projeto.

4. Crie e ative um ambiente virtual (recomendado)

  4.1. Crie o ambiente virtual:

```bash
python -m venv venv
```

  4.2. Ative o ambiente virtual:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

5. Execute o comando abaixo para instalar todas as dependências listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

6. Com as dependências instaladas, execute o seguinte comando para inicilizar a aplicação:

```bash
uvicorn main:app --reload
```

7. Abra o navegador de sua preferência e acesse:

```text
http://localhost:8000/docs
```

Com isso, você terá acesso ao Swagger UI, onde poderá consultar a documentação da API e testar os endpoints diretamente pelo navegador.
