# The Noise - Main Storyline

A story questline for **S.T.A.L.K.E.R. Anomaly / G.A.M.M.A.** It replaces Fanatic's "Training Day" tutorial
with a 16-stage main story that starts in the Cordon village and ends with a three-way choice.

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
| 7-10 | Renegades, the missing scout, the bloodsucker, the strike team | Spore | money, medkits, ammo |
| 11 | Cold | Spore / Cold | goodwill |
| 12 | The Wreck - the flight recorder | Cold | money, Basic Tools, medkits, ammo |
| 13-14 | The Cipher, a favour for Sid in the Garbage | Cold / Sidorovich | money, medkits, ammo |
| 15 | The Dead Convoy - Agroprom | Sidorovich | money |
| 16 | Kamerton - give it to Cold, sell it to Sid, or destroy it with Wolf | - | CS-2a armor / SKS + money / Soul |

An epilogue message arrives a day after the choice. Reward cap by design: no armor above light,
no weapon above an SKS.

## Features

- All tasks are main-story tasks (gold markers); the next quest giver gets a gold map marker too.
- Turning in a stage leads straight into the next offer in the same conversation (or "later").
- Targets, corpses and squads are spawned for each stage, away from anomalies and from locations used
  by the previous stages. Map markers follow the corpse that carries the quest item until it is picked up.
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
3. Start a new game as a loner in Cordon. Sid's radio call comes about 20 seconds after you load in.

## Notes

- The story starts only on a fresh game as a loner starting in Cordon. It disables Fanatic's "Training Day".
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
