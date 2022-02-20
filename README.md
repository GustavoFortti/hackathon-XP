# Hackaton XP - Open Finance

## Features
- Adquire token de autenticação da API da xp
- Recebe autorização do usuario para uso dos dados
- Busca informações historicas do usuário na API da XP
- Cria blocos na block chain interna
- Minera blocos e grava informações a partir da mem pool
- Produz mock de dados para novas operações
- Monitora novas operações dos usuários (mock)

## Download
```bash
$ git clone https://github.com/GustavoFortti/hackathon-XP.git
```

## Executar o servidor
```bash
export CLIENT_ID=<client_id>
export CLIENT_SECRET=<client_secret>
$ python3 app.py
```

## API
#### Recebe autorização do usuário para uso dos dados referentes à seus investimentos

- Rota
```
/user_auth
```
- Método
```
POST
```
- Body
```
{
	"authorized": true,
	"user_name": "JOSE",
	"bank": "xp"
}
```
#### Recebe autorização do usuário para uso dos dados referentes à seus investimentos

- Rota
```
/user_auth
```
- Método
```
POST
```
- Body
```
{
	"authorized": true,
	"user_name": "JOSE",
	"bank": "xp"
}
```

#### Simula recebimento de dados atualizados
- Rota
```
/simulate_stream_operations
```
- Método
```
GET
```
#### Minera um bloco para inserir informações presentes na mem pool
- Rota
```
/mine_block
```
- Método
```
GET
```
#### Busca toda a chain
- Rota
```
/get_chain
```
- Método
```
GET
```