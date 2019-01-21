# Installation

- Just copy the entire repository to your Binaries folder (the folder containing Win32/Borderlands.exe)

> python genskill.py > mods-m/ffyl.txt
> java -jar BLCMM_Launcher.jar
    >> open zerokills-m.txt
    >> Import ffyl.txt
    >> Save

> ./Borderlands.exe
    >> exec assassin-m.txt  -- main menu/console 
    -- return to the outer menu (the one which connects and updates)
    >> exec assassin-m.txt  -- outer menu/console

## genskill.py
- CA
    - base duration                 1800s
    - no loss in menu
- Kunai
    - 2x speed
    - small spread cone
- CounterStrike [for RAIDING]
    - Melee hit in deception has a chance to give a stack of FRENZY
    - Stacks last 90s
    - Each FRENZY stack gives +150% Ambush damage, +33% cooldown rate
    - Chance without 'Slayer of Terra' com at 10 points: 12%
    - Chance with 'Slayer of Terra' com at 10 points: 112%
- Fearless
    - 0.3% health regen per point
    - lowers weapon fire delay
    - adds a bullet to sniper rifle shot, lowers velocity
    - not sure, but should add +100% shock damage on shock weapons (not sure because of how values are calculated)
- Execute
    - no longer needs a target under crosshair
- Deception
    - fast animation by default

## Infinity
- adds +200% melee damage to the infinity (because a pistol is _wayyyy_ more assassin-y than an assault rifle)

## Dagger
- modifies the 1340 shield to become the DAGGER
- always at 0 shield
- +25% move speed
- +50% base armor
- 1.75M roid damage on OP8
- -50% status damage

## Mustang / Sally
- NOT ENABLED BY DEFAULT (see assassin-m.txt)
- modifies the hornet / teapot
- Not mine (from https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Kieitrio/Mustang%20&%20Sally%20V2.txt)
- Made some changes to it
- works like the harold (but much weaker)
- looks _much_ cooler because of the new skin

# Misc
- Changed the pimpernel skin
- Added regen snipers (from https://github.com/BLCM/BLCMods/blob/master/Pre%20Sequel%20Mods/Aaron0000/Weapon-Item%20Parts%20and%20Accessories/RegenSnipers.txt)


## unencumbered.py
- was an attempt to make a gunless zero
- there are too few user controlled events without guns
