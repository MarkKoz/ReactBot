# Discord Reaction Bot
### Description
Listens for messages on a specified channel and reacts to each one with
specified emojis. Both Unicode and custom emojis are supported. Due to the
emoji package's shortcomings, not all of Discord's Unicode emoji aliases are
supported; it is recommended to use the full name.

### Configuration
A file named `config.json`, located in `/src/` (same directory as `bot.py`), is
used as the configuration of the bot. This file must be created manually. The
following is a base for the file's contents:

```json
{
    "token": "",
    "name": "",
    "channel_id": "",
    "emojis": [
        "",
        ""
    ]
}
```

* `token` - The bot's token.
* `name` - The bot's name. This can be anything; only used for logging purposes.
* `channel_id` - The ID of the channel in which to listen for messages.
* `emojis` - A list of case-sensitive names of the emojis with which to react.
Do _not_ surround the names in colons.

### Requirements
#### Binaries
* [Python 3.6](https://www.python.org/downloads/) or higher
    * Make sure the python directory and python/Scripts directory are in your
    system's `PATH` environment variable.

#### Packages
* [discord.py](https://github.com/Rapptz/discord.py) async, _not_ rewrite
* [emoji](https://github.com/carpedm20/emoji)

### Running
Run `bot.py` to run the bot.

```bash
python bot.py
```
