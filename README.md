# Discord Reaction Bot
### Description
Listens for messages on a specified channel and reacts to each one with a
specified emoji. Both Unicode and custom emojis are supported. Due to the
emoji package's shortcomings, not all of Discord's Unicode emoji aliases are
supported; it is recommended to use the full name.

### Configuration
A file named `config.json`, located in `/src/` (same directory as `bot.py`), is
used as the configuration of the bot. Below is the base configuration for the
bot:

```json
{
    "token": "",
    "name": "",
    "channel_id": "",
    "emoji": ""
}
```

* `token` - The bot's token.
* `name` - The bot's name. This can be anything; only used for logging purposes.
* `channel_id` - The ID of the channel in which to listen for messages.
* `emoji` - The name of the emoji with which to react.

### Requirements
#### Binaries
* [Python 3.6](https://www.python.org/downloads/) or higher
    * Make sure the python directory and python/Scripts directory are in your
    system's `PATH` environment variable.
    * For Windows users especially,
    [Anaconda](https://www.anaconda.com/download/) is recommended over the
    standard installer from python.org.

#### Packages
* [discord.py](https://github.com/Rapptz/discord.py) async, _not_ rewrite
* [emoji](https://github.com/carpedm20/emoji)

### Running
Run `bot.py` to run the bot.

```bash
python bot.py
```
