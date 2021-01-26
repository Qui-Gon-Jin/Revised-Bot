# Revised Bot
## Discord bot for WoD tabletops.

To run bot on your own, first download or clone repository, then create [discord bot token](https://discord.com/developers/applications) and put it to new file "Token.txt" near to Bot.py.
Bot primary uses "discord" libruary, so before starting it make shure you installed it with
```
pip install discord
```
____
Rolls are looking the same as they presented in a corebook
```markdown
!roll ***number***d***dice*** ***threshold***
```
Also it's include a default difficulty as 6, so roll without **threshold** would be count so
```markdown
!roll ***number***d***dice***
```
And finnaly, as a WoD games uses only d10 dices, you can skip **dice** in your notation
```markdown
!roll ***number***
```
