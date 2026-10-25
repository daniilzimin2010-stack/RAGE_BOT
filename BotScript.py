import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ==================== НАСТРОЙКИ БОТА ====================
ROLE_ID = 1563852985509879849  
BOT_TOKEN = "MTU2Mzg0MzE3MTYyMzEwODczOA.GD4EPQ.tmc8RiP3RIz_PoDCrP3EfUA-So9FCkr3Qt0dDM"
# ========================================================

@bot.event
async def on_ready():
    print(f"Бот {bot.user.name} запущен")

@bot.command()
async def GW(ctx, *, message_text: str):
    role = ctx.guild.get_role(ROLE_ID)
    
    if not role:
        await ctx.send("Роль не найдена")
        return

    final_message = f"🐓🐓🐓🐓🐓 **Gang War alert!** 🐓🐓🐓🐓🐓 \n\n{ctx.author.display_name} Пинганул ГВ. Вот что  он приложил:\n\n> {message_text}\n\n  если нет ссылки, то перейди на <#1563638952743800905>"

    success_count = 0
    fail_count = 0

    for member in role.members:
        if member.bot: 
            continue 
            
        try:
            await member.send(final_message)
            success_count += 1
            await asyncio.sleep(1)
        except discord.Forbidden:
            fail_count += 1
        except Exception as e:
            print(f"Ошибка при отправке пользователю {member.name}: {e}")
            fail_count += 1

bot.run(BOT_TOKEN)