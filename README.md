# Hackaton XP - Open Finance

## Features
- Adquire token de autenticação da API da xp
- Recebe autorização do usuario para uso dos dados
- Busca informações historicas do usuário na API da XP
- Cria blocos na block chain interna
- Minera blocos e grava informações a partir da mem pool
- Monitora novas operações dos usuários 

## Download
```bash
$ git clone https://github.com/GustavoFortti/hackathon-XP.git
```

## Executar o servidor
```bash
$ python3 app.py
```

## API
#### Recebe autorização do usuário para uso dos dados referentes à seus investimentos

-- Rota
```
/user_auth
```
-- Método
```
POST
```
-- Body
```
{
	"authorized": true,
	"user_name": "JOSE",
	"bank": "xp"
}
```

## API
#### Recebe autorização do usuário para uso dos dados referentes à seus investimentos

-- Rota
```
/user_auth
```
-- Método
```
POST
```
-- Body
```
{
	"authorized": true,
	"user_name": "JOSE",
	"bank": "xp"
}
```

#### Simula recebimento de dados atualizados
-- Rota
```
/simulate_stream_operations
```
-- Método
```
GET
```
