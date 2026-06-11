# app/schemas/api_responses.py

REGISTER_RESPONSES = {
    201: {"description": "Usuário criado"},
    400: {"description": "Campo obrigatório não informado"},
    409: {"description": "Usuário já cadastrado"},
    422: {"description": "Repetição da senha não confere"},
    500: {"description": "Erro interno do servidor"}
}

LOGIN_RESPONSES = {
    200: {"description": "Login realizado com sucesso"},  # corrigido de 201 para 200
    400: {"description": "Dados enviados incorretamente"},
    401: {"description": "Senha incorreta"},
    404: {"description": "Usuário não encontrado"},
    500: {"description": "Erro interno do servidor"}
}

HEART_HEALTH_RESPONSES = {
    201: {"description": "Dados registrados com sucesso"},
    400: {"description": "Dados enviados incorretamente"},
    401: {"description": "Falha na autenticação"},
    403: {"description": "Sem permissão"},
    404: {"description": "Usuário ou registro não encontrado"},
    429: {"description": "Limite de requisições atingido"},
    500: {"description": "Erro interno do servidor"},
    503: {"description": "Serviço indisponível"}
}

HEART_REPORT_RESPONSES = {
    200: {"description": "Relatório gerado com sucesso"},
    400: {"description": "Parâmetros de data inválidos"},
    401: {"description": "Falha na autenticação"},
    403: {"description": "Sem permissão"},
    404: {"description": "Relatório não encontrado para o período informado"},
    429: {"description": "Limite de requisições atingido"},
    500: {"description": "Erro interno do servidor"},
    503: {"description": "Serviço indisponível"}
}
