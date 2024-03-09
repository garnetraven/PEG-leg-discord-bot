import os
import io
import discord
from discord.ext import commands
from PyPDF2 import PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class PDFConverter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == int(os.getenv('TARGET_CHANNEL_ID')) and message.attachments:
            for attachment in message.attachments:
                if attachment.filename.lower().endswith('.pdf'):
                    await self.convert_pdf_to_jpeg(message, attachment)

    async def convert_pdf_to_jpeg(self, message, attachment):
        # Download the PDF attachment
        pdf_content = await attachment.read()

        # Convert the PDF to a JPEG image
        image_bytes = self.pdf_to_jpeg(pdf_content)

        # Send the converted image back to the channel
        await message.channel.send(f"Converted PDF: {attachment.filename}", file=discord.File(io.BytesIO(image_bytes), 'converted_image.jpeg'))

    def pdf_to_jpeg(self, pdf_content):
        # Convert PDF to JPEG using reportlab library
        pdf_reader = PdfFileReader(io.BytesIO(pdf_content))
        image_bytes = io.BytesIO()

        # Create a canvas to draw PDF content on an image
        pdf_canvas = canvas.Canvas(image_bytes, pagesize=letter)
        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            pdf_canvas.setPageSize((page.mediaBox[2], page.mediaBox[3]))
            pdf_canvas.drawImage(pdf_reader.getPage(page_num), 0, 0)
            pdf_canvas.showPage()

        pdf_canvas.save()
        image_bytes.seek(0)
        return image_bytes.read()


def setup(bot):
    bot.add_cog(PDFConverter(bot))
