import discord
from deep_translator import MyMemoryTranslator

TOKEN = "MTU2NTUyMzgwOTE4MjgxNDM3OQ.Gr2vlB.x3MtUKWurmlTd75Strz3X3g5qLc1O69ujfzS48"

SPANISH_CHANNEL = 1395254621576101968
INDONESIAN_CHANNEL = 1565528085279936574

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Bot conectado con éxito como: {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    # Verificamos si el mensaje tiene texto o archivos adjuntos (imágenes / GIFs)
    tiene_texto = bool(message.content.strip())
    tiene_archivos = len(message.attachments) > 0

    if not tiene_texto and not tiene_archivos:
        return

    try:
        # Preparamos los archivos adjuntos (imágenes o GIFs) para reenviarlos si los hay
        archivos_para_enviar = []
        if tiene_archivos:
            for attachment in message.attachments:
                # Convertimos cada archivo adjunto en un archivo listo para enviar a Discord
                archivo = await attachment.to_file()
                archivos_para_enviar.append(archivo)

        # Canal Español -> Indonesio
        if message.channel.id == SPANISH_CHANNEL:
            canal_destino = client.get_channel(INDONESIAN_CHANNEL)
            if canal_destino:
                if tiene_texto:
                    traduccion = MyMemoryTranslator(source='es-ES', target='id-ID').translate(message.content)
                    await canal_destino.send(
                        f"🇮🇩 **{message.author.display_name}**:\n{traduccion}", 
                        files=archivos_para_enviar
                    )
                elif archivos_para_enviar:
                    # Si solo mandó la imagen/GIF sin texto
                    await canal_destino.send(
                        f"🇮🇩 **{message.author.display_name}** (Archivo adjunto):", 
                        files=archivos_para_enviar
                    )

        # Canal Indonesio -> Español
        elif message.channel.id == INDONESIAN_CHANNEL:
            canal_destino = client.get_channel(SPANISH_CHANNEL)
            if canal_destino:
                if tiene_texto:
                    traduccion = MyMemoryTranslator(source='id-ID', target='es-ES').translate(message.content)
                    await canal_destino.send(
                        f"🇪🇸 **{message.author.display_name}**:\n{traduccion}", 
                        files=archivos_para_enviar
                    )
                elif archivos_para_enviar:
                    # Si solo mandó la imagen/GIF sin texto
                    await canal_destino.send(
                        f"🇪🇸 **{message.author.display_name}** (Archivo adjunto):", 
                        files=archivos_para_enviar
                    )

    except Exception as e:
        print(f"Error al procesar el mensaje o archivo: {e}")

client.run(TOKEN)