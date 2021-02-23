# Revised Bot
## Discord bot for World Of Darkness tabletop games

Bot created to do play World Of Darkness tabletop RPGs over Discord more natively, by supporting throw mechanics and counting rules from them. By the moment bot can properly count successes, failures and crit failures. Also it provides abilitie of choosing difficulty of throw, number of dices, different dice types.

To add bot to your discord server click [here](https://discord.com/api/oauth2/authorize?client_id=729593204176977971&permissions=2048&scope=bot), then choose server.
___

Rolls are looking the same as they presented in a corebook:
```
!roll *number_of_dices* *roll_threshold*
```
As bot supports default  **roll_threshold** as 6, you can skip this part and type 
```
!roll *number_of_dices*
```
Add -e in the end of comand to roll with explosive option (every 10 on roll will be reroled extra time)
```
!roll *number_of_dices* *roll_threshold* -e
```
If you need some extra of d10 dices, type

```
!roll *number_of_dices*d*dice_type* *roll_threshold*
```
Or skip **roll_threshold**, and it will counted as 6
```
!roll *number_of_dices*d*dice_type*
```
____
## Bot installation

To run bot on your own, first download or clone repository, then create [discord bot token](https://discord.com/developers/applications) and put it to new file "Token.txt" near to Bot.py.
Bot primary uses "discord" libruary, so before starting it make shure you installed it with
```
pip install discord
```
____
## In development

- [ ] Set explosive dices option
- [ ] Make the settings changeable for each individual server