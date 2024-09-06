import discord
from discord.ext import commands

# İzinleri ayarlama (intents)
intents = discord.Intents.default()
intents.message_content = True  # Mesaj içeriğini okuyabilmesi için gerekli

# Botu başlatma
bot = commands.Bot(command_prefix="!", intents=intents)

# Bot hazır olduğunda mesaj verir
@bot.event
async def on_ready():
    print(f"{bot.user} olarak giriş yapıldı!")

# !kaynak komutu ile çevre hakkında bilgi veren sitelere yönlendirir
@bot.command()
async def kaynak(ctx):
    message = (
        "Çevre kirliliği hakkında daha fazla bilgi edinmek için aşağıdaki sitelere göz atabilirsiniz:\n"
        "- [Greenpeace](https://www.greenpeace.org/)\n"
        "- [WWF - Dünya Doğayı Koruma Vakfı](https://www.wwf.org/)\n"
        "- [Birleşmiş Milletler Çevre Programı (UNEP)](https://www.unep.org/)\n"
        "- [Doğa Derneği](https://www.dogadernegi.org/)\n"
        "- [TEMA Vakfı](https://www.tema.org.tr/)\n"
    )
    await ctx.send(message)

# Botu çalıştırma (token'ini buraya ekle)
bot.run("TOKEN)
