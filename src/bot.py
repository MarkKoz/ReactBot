from typing import Optional, Pattern, Union
import json
import re

import discord
import emoji

from src import logger

with open("config.json") as file:
    config = json.load(file)

client: discord.Client = discord.Client()

@client.event
async def on_ready():
    """
    Called when the :class:`client<discord.Client>` is done preparing the data
    received from Discord. Usually after login is successful and the
    Client.servers and co. are filled up.

    Note
    -------
    This function is not guaranteed to be the first event called. Likewise, this
    function is not guaranteed to only be called once. This library implements
    reconnection logic and thus will end up calling this event whenever a RESUME
    request fails.

    Returns
    -------
    None
    """
    log.info(f"{config['name']} logged in as {client.user} ({client.user.id})")

@client.event
async def on_resumed():
    """
    Called when the :class:`client<discord.Client>` has resumed a session.

    Returns
    -------
    None
    """
    log.info(f"{config['name']} resumed.")

@client.event
async def on_message(msg: discord.Message):
    """Listens to messages.

    Called when a :class:`message<discord.Message>` is created and sent to a
    server.

    Parameters
    ----------
    msg: discord.Message
        The message the creation of which called this event.

    Returns
    -------
    None
    """
    # Ignores bot's messages and direct/private messages.
    if msg.author == client.user or msg.server is None:
        return

    # Only processes messages in the channel specified in the config.
    if msg.channel.id == config["channel_id"]:
        await react(msg, config['emoji'])

async def react(msg: discord.Message, emoji_name: str) -> None:
    """Reacts to a message.

    Reacts to a :any:`message` with an emoji corresponding to :any:`emoji_name`.

    Parameters
    ----------
    msg: discord.Message
        The message to which to react.
    emoji_name: str
        The name of the emoji with which to react. Case sensitive;
        no delimiters.

    Returns
    -------
    None
    """
    # Unicode emoji.
    if await try_react(msg, emoji.emojize(f":{emoji_name}:",
                                          use_aliases = True)):
        return

    # Custom emoji.
    if await try_react(msg, await get_custom_emoji(emoji_name)):
        return

    log.warning(f"Invalid emoji '{emoji_name}'.")

async def try_react(msg: discord.Message,
                    emj: Union[bytes, str, discord.Emoji]) -> bool:
    """Tries to react to a message.

    Attempts to react to a :class:`~discord.Message` with the :any:`Emoji<emj>`,
    returning a boolean indicative of success.

    Parameters
    ----------
    msg: discord.Message
        The message to which to react.
    emj: Union[bytes, str, discord.Emoji]
        The emoji with which to react. Either a Unicode code for standard
        Unicode emojis or an :class:`~discord.Emoji` object for custom emojis.

    Returns
    -------
    bool
        :keyword:`True` if successful; :keyword:`False` otherwise.
    """
    try:
        await client.add_reaction(msg, emj)
        return True
    except (discord.errors.HTTPException, discord.errors.InvalidArgument):
        return False

async def get_custom_emoji(name: str) -> Optional[discord.Emoji]:
    """Finds a custom emoji from a name.

    Retrieves a :class:`~discord.Emoji` object from an emoji name which
    corresponds to a custom guild emoji.

    Parameters
    ----------
    name: str
        The name of the emoji to retrieve.

    Returns
    -------
    discord.Emoji
        The :class:`~discord.Emoji` object which corresponds to the :any:`name`.
    None
        Returned when no corresponding emoji could be found.

    """
    return next((e for e in client.get_all_emojis() if e.name == name), None)

if __name__ == "__main__":
    # Creates loggers.
    format_str: str = "%(asctime)s - [%(levelname)s] %(name)s: %(message)s"
    pattern: Pattern = re.compile(r"Unhandled event", re.IGNORECASE)
    handler: logger.StreamFiltered = logger.StreamFiltered(pattern)

    logger_bot: logger.LoggerProxy = logger.LoggerProxy("bot", format_str)
    logger_discord: logger.LoggerProxy = logger.LoggerProxy("discord",
                                                            format_str,
                                                            handler)
    log = logger_bot.log

    client.run(config["token"]) # Starts the bot.

    # Closes and removes logging handlers.
    logger_bot.close()
    logger_discord.close()
