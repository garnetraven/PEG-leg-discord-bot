![PEGLeg - Discord Bot.](/assets/images/PEGLeg.png)
# PEGLeg discord bot

Discord bot build for a SoDA discord workshop. Written in python, this is a Discord bot that listens for messages with PDF attachments and converts the PDFs to JPEGs. The images are then sent back to the channel. 

## Features

- Listens for new messages in specified channel(s)
- Converts PDF attachments to images
- Sends the images back to the channel

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/garnetraven/PEGLeg-DiscordBot.git
   ```
3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```
4. Install Poppler:
- On Ubuntu/Debian:
  ```
  sudo apt-get install -y poppler-utils
  ```
- On other systems, see the [Poppler website](https://poppler.freedesktop.org/).

## Usage

1. Set your Discord bot tokens in the `.env` file:
   ```
   DISCORD_BOT_TOKEN=<YOUR_DISCORD_TOKEN>
   GUILD_ID=<YOUR_GUID_ID>
   TARGET_CHANNEL_ID=<TARGET_CHANNEL_ID>
   ```
3. Run the bot:
   ```
   python main.py
   ```
## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
