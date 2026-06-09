# Heart Health API

## Arquitetura

O projeto foi desenvolvido utilizando FastAPI e segue uma arquitetura modular dividida em camadas.

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