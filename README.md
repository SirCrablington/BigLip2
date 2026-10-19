# 💋 Miss Attitude — Chaotic Discord Bot

A playful Discord bot built with Python and `discord.py`. It has chaotic scripted chat, friendly roasts, and quick mini-games.

## Features and commands

### Chat & sass
- `/chat message` — Responds with playful, scripted chaotic replies. This does **not** connect to an external AI service.
- `/hello` — Chaotic greeting.
- `/roast @member` — Playful roast.
- `/comeback` — Random comeback.
- `/mood` — Current mood.

### Games
- `/wyr` — Random Would You Rather prompt with A/B reactions.
- `/trivia` — Multiple-choice trivia prompt.
- `/coinflip` — Flip a coin.

### Other
- `/help` — Command menu.
- Optional join welcome message when `WELCOME_CHANNEL_ID` is configured.

## 1. Create your Discord bot

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Create an application and add a bot under **Bot**.
3. Copy its token. Keep it private.
4. Under **OAuth2 → URL Generator**, select `bot` and `applications.commands`. Give only the permissions needed, such as View Channels, Send Messages, and Add Reactions.
5. Use the generated invite URL to add the bot to your server.
6. For welcome messages, enable **Server Members Intent** under Bot settings.

## 2. Run it locally

Python 3.10+ is recommended.

```bash
python -m venv .venv
```

Activate the environment:
- Windows PowerShell: `.\.venv\Scripts\Activate.ps1`
- macOS/Linux: `source .venv/bin/activate`

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Copy `.env.example` to `.env` and put your token in the `DISCORD_TOKEN` field. Do not commit `.env`.

Optional: set `WELCOME_CHANNEL_ID` to the channel ID for join announcements. To copy a channel ID, enable Developer Mode in Discord, right-click a channel, and select **Copy Channel ID**.

Run:

```bash
python bot.py
```

Slash commands sync at startup and may take a short time to show up.

## 3. Upload to GitHub

Create a repository and upload:
- `bot.py`
- `requirements.txt`
- `.env.example`
- `.gitignore`
- `README.md`

Never upload `.env` or your token. If a token is exposed, reset it immediately in the Developer Portal.

## 4. Hosting

GitHub stores the source code; it does not keep the bot running. Run it on your computer or deploy it to a host that supports persistent Python processes. Configure `DISCORD_TOKEN` as a secret/environment variable on the host. Check the host's current free-tier and sleep policies.

## Customise

Edit `ROASTS`, `COMEBACKS`, `MOODS`, `CHAT_REPLIES`, `WOULD_YOU_RATHER`, and `TRIVIA` in `bot.py` to change the personality and content.
