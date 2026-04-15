# Charla python

## Preparacion
- Docs
- requirements (discord.py[voice], python-dotenv)
- venv
- DISCORD_TOKEN
- https://discord.com/developers/applications
- new/bot/reset Token
- oauth/bot

### Intents
- Presence: Saber estado y que esta haciendo los usuarios
- Server Members: eventos (como entrar al servidor)
- Message Content: Permiso de mensajes


## Funciones interesantes
### Funciones
- delete
- send (privado si es directamente, si es channel.send por el canal que reciba el mensaje)
- process_commands (hacer que no pare al recibir solo un mensaje)
### Eventos
- on_member_join
- on_message
- on_ready
- hybrid_command
- command
- commands.has_role(<rol>)
- discord.utils.get(message.author.roles, name="prueba")
- reply