import os
import discord
from discord.ext import commands
from pdf2image import convert_from_path

class PDFConverter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # Ignore messages sent by the bot itself
        if message.author == self.bot.user:
            return

        # Check if the message is in the target channel
        if message.channel.id != int(os.getenv('TARGET_CHANNEL_ID')):
            return

        # Check for attachments in the message
        for attachment in message.attachments:
            # Check if the attachment is a PDF file
            if attachment.filename.endswith('.pdf'):
                await self.convert(message, attachment)

    async def convert(self, message, attachment):
        print("PDF attachment found.")

        # Create a temporary directory if it doesn't exist
        if not os.path.exists('/tmp'):
            os.makedirs('/tmp')

        # Save the PDF attachment to a temporary file
        pdf_path = f'/tmp/{attachment.filename}'
        await attachment.save(pdf_path)
        print(f"PDF saved to {pdf_path}")

        print("Converting PDF to images...")
        try:
            images = convert_from_path(pdf_path)
            print(f"PDF converted to {len(images)} images.")
        except Exception as e:
            print(f"An error occurred while converting the PDF to images: {e}")
            return

        for i, image in enumerate(images):
            image_path = f'/tmp/image{i}.jpeg'
            image.save(image_path, 'JPEG')
            print(f"Image saved to {image_path}")

            # Send the image to the Discord channel
            with open(image_path, 'rb') as img:
                await message.channel.send(file=discord.File(img, 'image.jpeg'))
                print(f"Image sent to Discord.")

# Asynchronous setup function to add the cog to the bot
async def setup(bot):
    await bot.add_cog(PDFConverter(bot))
