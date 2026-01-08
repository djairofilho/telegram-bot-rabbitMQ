
# RabbitMQ Telegram Notifier

Este projeto consome mensagens de uma fila RabbitMQ e envia notificações para um chat do Telegram usando Python.

## Como funciona o sistema

1. **Publicação:** Uma mensagem é publicada em uma fila do RabbitMQ.
2. **Consumo:** O consumidor Python (run.py) lê as mensagens dessa fila.
3. **Notificação:** Cada mensagem consumida é enviada automaticamente para um chat/grupo do Telegram via bot.

Esse fluxo permite automatizar alertas, notificações ou integrações entre sistemas usando filas e o Telegram.

## Requisitos

- Python 3.8+
- Docker (para rodar o RabbitMQ)
- Conta e bot no Telegram

## Como rodar

1. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

2. Copie o arquivo `.env.example` para `.env` e preencha com suas configurações do RabbitMQ e Telegram.

3. Suba o RabbitMQ com Docker:
   ```
   docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
   ```

4. Execute o consumidor:
   ```
   python run.py
   ```

## Estrutura

- `src/drivers/telegram_sender.py`: Envia mensagens para o Telegram.
- `src/main/rabbitmq_configs/consumer.py`: Consome mensagens do RabbitMQ.
- `.env.example`: Exemplo de configuração de variáveis de ambiente.

## Como obter o token do Telegram Bot

1. No Telegram, procure por "@BotFather" e inicie uma conversa.
2. Envie o comando `/newbot` e siga as instruções para criar um novo bot.
3. Após criar, o BotFather enviará uma mensagem com o token de acesso do seu bot (exemplo: `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`).
4. Copie esse token e coloque na variável `TELEGRAM_TOKEN` do seu arquivo `.env`.

Para saber o `TELEGRAM_CHAT_ID`, adicione o bot ao grupo ou envie uma mensagem para ele e utilize ferramentas como @userinfobot ou consulte a documentação do Telegram para obter o chat ID.

## Sobre a API do Telegram

O endpoint usado para enviar mensagens é:

```
https://api.telegram.org/bot<SEU_TOKEN>/sendMessage
```

No código:

```
url = f"https://api.telegram.org/bot{token}/sendMessage"
```

O `{token}` é substituído pelo token do seu bot, permitindo autenticação e envio de mensagens via API do Telegram. O endpoint `/sendMessage` é utilizado para enviar textos para um chat ou grupo.
