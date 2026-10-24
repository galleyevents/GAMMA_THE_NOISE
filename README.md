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
  Armor is compared by class first (light < medium < scientific/heavy), then by price.
- Story targets are always hostile: squads the player has to kill get a personal goodwill of -10000
  towards the player, set again during the stage, so no faction relation (G.A.M.M.A.'s dynamic ones
  included) makes them neutral.
- Squads that come for the player hunt them instead of holding their spot: the army patrol (stage 10),
  the looters at the wreck (12), the Clear Sky squad (20) and the mercenaries in the tunnels (23).
- Spawn spots without other squads are preferred, then ones the last stages didn't use.
- The transmitter under Agroprom (stage 24) is a field radio station (generator, radio, two antenna
  devices) crackling with electric anomaly effects and playing the Noise. Once its guards are dead,
  stand next to it and press the use key to pull out the resonator; it goes silent and dark.
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

1. In MO2: *Install a new mod from an archive* and pick the release zip. The installer asks for the
   reward mode (below). Updating: remove the old version first.
   (Copying the `The Noise - Main Storyline` folder into `mods` by hand works too, with full rewards.)
2. Enable the mod. Load order doesn't matter much: it adds its own files and uses
   DXML/DLTX instead of overwriting shared configs.
3. Start a new game, or load an existing save, as a Loner, Duty, Freedom, Ecologist or Clear Sky character. Sid's radio call comes about
   a minute after you are in Cordon (an existing save elsewhere gets it after arriving in Cordon).

## Reward modes

| Mode | Money | Ammo, medicine | Gear (backpack, armor, weapons, tools, stage 4 jacket and gas mask, Sid's TOZ advance) | Story artifacts |
|---|---|---|---|---|
| Full (default) | yes | yes | yes | yes |
| No gear | yes | yes | no | yes |
| Money only | yes | no | no | yes |

Picked in the installer (it adds `configs/mod_system_szm_mode.ltx`) and changeable at any time in MCM
(*The Noise* > *Rewards*), which overrides the installer's choice. Quest items and what a task needs (the
cooking kit) are always given. In the hardcore modes Cold pays 5 000 RU for the Kamerton instead of the armor. Reward lines that would promise removed items have `<id>_nogear` /
`<id>_money` versions in `st_szm.xml`.

## Notes

- The story starts for a Loner, Duty, Freedom, Ecologist or Clear Sky character (new game or existing save)
  once they are in Cordon (`ALLOWED_COMMUNITIES` in `szm_main.script`). It disables Fanatic's "Training Day".
  Every squad the story sends against the player is hostile to any faction. A Clear Sky player can't sell
  the Kamerton to Sid (only Cold or Wolf), and Sid, Spore and Cold talk to them as one of Clear Sky
  (`<id>_csky` texts in `st_szm.xml`; the dialog generator picks them up on its own).
- Internal ids use the `szm_` prefix (from the working title "Szum"). Don't rename them: saves depend on them.
- Uninstalling mid-story leaves the quest items and task entries orphaned in your save.
- `dialogs_szm.xml` is generated: edit `tools/szm_gen_dialogs.py` (stage givers, chaining) and the texts,
  then run `python tools/szm_gen_dialogs.py "The Noise - Main Storyline/gamedata"`.

## Files

```
The Noise - Main Storyline/gamedata/
  scripts/szm_main.script                    story engine (stages, spawns, markers, rewards)
  scripts/modxml_szm.script                  DXML: dialogs on Sid, Wolf, Spore, Cold; gold map spot
  scripts/szm_mcm.script                     MCM: reward mode
  configs/mod_system_szm.ltx                 DLTX: registers the dialog file
  configs/gameplay/dialogs_szm.xml           dialogs (generated)
  configs/misc/task/tm_szm.ltx               tasks, money and goodwill rewards
  configs/misc/squad_descr/squad_descr_szm.ltx  spawned squads
  configs/items/items/items_szm.ltx          quest items
  configs/text/eng/st_szm.xml                all texts
  textures/ui/ui_szm_icons.dds               quest item icons
tools/szm_gen_dialogs.py                     dialog generator
installer/fomod/                             MO2 installer (FOMOD), packed into the release zip
installer/options/<mode>/                    what each reward mode adds (mod_system_szm_mode.ltx)
```
