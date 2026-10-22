# The Noise - Storyline Tutorial

A story questline for **S.T.A.L.K.E.R. Anomaly / G.A.M.M.A.** It replaces Fanatic's "Training Day" tutorial
with a main story of 21 stages per playthrough (27 in all, across three Act V branches) that starts in the Cordon village and ends with a three-way choice.

Sidorovich calls the new stalker on the radio: he's looking for workers. Odd jobs around the village
turn into the search for his missing courier - and the first time you hear the Noise, a pulsing hiss
on the radio that leads from Cordon to the Great Swamps, Garbage and Agroprom, and to the military
prototype behind it.

## Story outline

| # | Stage | Giver | Reward |
|---|---|---|---|
| 1 | A Job Offer - Sid's radio call | Sidorovich | - |
| 2 | The Hunt - boars, two legs | Sidorovich | money |
| 3 | By the Campfire - cook boar meat for Wolf | Sidorovich / Wolf | money |
| 4 | The Missing Courier - the bandit, the cylinder, **the first Noise** | Sidorovich | Leather Jacket, PBF gas mask (TOZ-34 as an advance) |
| 5 | Jellyfish - the Noise again | Sidorovich | backpack, medicine |
| 6 | The Road to the Swamps | Sidorovich / Spore | goodwill |
| 7-10 | Renegades, the missing scout, the bloodsucker, the strike team (with two Clear Sky fighters) | Spore | money, medkits, ammo |
| 11 | Cold | Spore / Cold | goodwill |
| 12 | The Wreck - the flight recorder | Cold | money, Basic Tools, medkits, ammo |
| 13-14 | The Cipher, a favour for Sid in the Garbage | Cold / Sidorovich | money, medkits, ammo |
| 15 | The Dead Convoy - Agroprom | Sidorovich | money |
| 16 | Kamerton - give it to Cold, sell it to Sid, or destroy it with Wolf | - | Clear Sky armor / a rifle + money / Soul |

### Act V - the Noise returns

A day after the choice - and the "storyline complete" banner - the Noise is back: the side you chose calls
you on the radio and asks you to come over. From there the story flows as before: each report leads straight
into the next job, and in the tunnels under Agroprom the last stages follow over the radio.

| # | Stage | Side | Reward |
|---|---|---|---|
| 17 | Reprisal - an army patrol in the Swamps | Cold | money, medkits, ammo |
| 18 | Frequency Logs - an army signal team in Agroprom | Cold | money, medkits, ammo |
| 19 | The Buyer - his men in the Garbage, his PDA | Sid | money, ammo |
| 20 | Clear Sky's Debt - a Clear Sky hit squad in Cordon | Sid | money, medkits, ammo |
| 21 | Echo - an artifact where the Kamerton vanished | Wolf | money, medkits |
| 22 | Strangers in Cordon - mercenary scouts and their orders | Wolf | money, medkits, ammo |
| 23 | Under Agroprom - the missing scientists, their journal, mercenaries | all | money |
| 24 | The Transmitter - its guards and the resonator | all | money |
| 25-27 | Silence - the resonator to Cold / Sid / Wolf | the chosen side | money + medkits, ammo / money / Night Star |

Rewards scale with the player's gear (see below).

Timing is set at the top of `szm_main.script`: `ACT5_FIRST_DELAY_H` (24 in-game hours from the choice to the
radio call) and `ACT5_TEST_DELAY` (real seconds, overrides it for testing; **set it to `nil` before a release**).

## Features

- Scaled rewards: the mod remembers the most valuable weapon, armor and backpack the player has had
  equipped. Gear rewards (Sid's backpack, Cold's armor, Sid's rifle) are the first item of a tier list
  (`GEAR_TIERS` in `szm_main.script`) clearly better than that; if the player has outgrown the whole
  list, the giver says so in the report dialog and pays money instead - except for weapons: then the
  player gets a clearly better gun from `GEAR_OVERFLOW`, worn (only the barrel pristine, the other parts
  40-80%), and money only when even that list is outgrown. The same gear level scales the
  money of every stage and the medkit type. The leather jacket and gas mask of stage 4 stay fixed (tutorial).
- All tasks are main-story tasks (gold markers); the next quest giver gets a gold map marker too.
- Turning in a stage leads straight into the next offer in the same conversation (or "later").
- Targets, corpses and squads are spawned for each stage, away from anomalies and from locations used
  by the previous stages. Map markers follow the corpse that carries the quest item until it is picked up.
- In the strike team stage Spore sends two Clear Sky fighters (at least Experienced) along as companions;
  they help find the bodies and fight the army patrol, then go back to the base.
- Radio messages from the characters, including all three parties interested in the Kamerton.
- Custom inventory icons for the quest items, in G.A.M.M.A.'s icon style.

## Requirements

- G.A.M.M.A. (or Anomaly 1.5.2 with the modded exes and DXML / DLTX support).
- English language.

## Installation (Mod Organizer 2)

1. Copy the `The Noise - Main Storyline` folder into your MO2 `mods` folder
   (for G.A.M.M.A.: `<GAMMA>\mods\`).
2. Refresh MO2 (F5) and enable the mod. Load order doesn't matter much: it adds its own files and uses
   DXML/DLTX instead of overwriting shared configs.
3. Start a new game as a loner in Cordon, or load an existing loner save. Sid's radio call comes about
   a minute after you are in Cordon (an existing save elsewhere gets it after arriving in Cordon).

## Notes

- The story starts for a loner (new game or existing save) once they are in Cordon. It disables Fanatic's "Training Day".
- Internal ids use the `szm_` prefix (from the working title "Szum"). Don't rename them: saves depend on them.
- Uninstalling mid-story leaves the quest items and task entries orphaned in your save.
- `dialogs_szm.xml` is generated: edit `tools/szm_gen_dialogs.py` (stage givers, chaining) and the texts,
  then run `python tools/szm_gen_dialogs.py "The Noise - Main Storyline/gamedata"`.

## Files

```
The Noise - Main Storyline/gamedata/
  scripts/szm_main.script                    story engine (stages, spawns, markers, rewards)
  scripts/modxml_szm.script                  DXML: dialogs on Sid, Wolf, Spore, Cold; gold map spot
  configs/mod_system_szm.ltx                 DLTX: registers the dialog file
  configs/gameplay/dialogs_szm.xml           dialogs (generated)
  configs/misc/task/tm_szm.ltx               tasks, money and goodwill rewards
  configs/misc/squad_descr/squad_descr_szm.ltx  spawned squads
  configs/items/items/items_szm.ltx          quest items
  configs/text/eng/st_szm.xml                all texts
  textures/ui/ui_szm_icons.dds               quest item icons
tools/szm_gen_dialogs.py                     dialog generator
```
