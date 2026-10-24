# Dead Channel - Storyline

A story questline for **S.T.A.L.K.E.R. Anomaly / G.A.M.M.A.**: Rostok, the Truck Cemetery, the Dead City
and the Wild Territory. Six stages, three endings. For Loners, Duty, Ecologists and Clear Sky; Duty players
get their own lines with the Barman.

It tells a story and leaves the world alone: only the quest's own squads fight (per-NPC goodwill), no
faction relation, price or other G.A.M.M.A. system is changed.

## Stages

| # | Stage | What happens |
|---|---|---|
| 1 | The Signal | The Barman calls on the radio once you are in Rostok. Talk to him; he pays an advance. |
| 2 | Asking Around | Ask 2 of 3 people in Rostok about the courier (the Duty patrol, the guide, the Duty medic). |
| 3 | Scrap and Radiation | Bandits at the Truck Cemetery, the courier's PDA near them. Report to the Barman; he calls an hour later. |
| 4 | Guests in the Dead City | Talk to Grek (pay him off, or go as security) - or, if the mercenaries are hostile to you, find a dead courier's orders. |
| 5 | Exchange on the Tracks | Lis waits at a campfire in the Wild Territory. Buy the crate back, take it by force, or choose a side - then survive what comes. |
| 6 | Reckoning | Back to the Barman; the ending follows your choice (pay, items and marked caches when he gets his crate). |

## Requirements

G.A.M.M.A., or S.T.A.L.K.E.R. Anomaly 1.5.3 with the modded exes (DLTX and DXML). Play as a Loner, Duty,
an Ecologist or Clear Sky.

## Installation (Mod Organizer 2)

1. In MO2: *Install a new mod from an archive* and pick the release zip (`gamedata/` is at its root).
2. Enable the mod; its place in the load order doesn't matter.
3. No new game needed: the Barman calls the next time you enter Rostok.

## Files

```
Dead Channel - Storyline/gamedata/
  scripts/dch_main.script                    story engine (stages, spawns, choices, endings)
  scripts/modxml_dch.script                  DXML: dialogs on the Barman and three Rostok NPCs; gold map spot
  configs/mod_system_zzz_dch.ltx             DLTX: dialogs, profiles, the NPCs Grek and Lis
  configs/gameplay/character_desc_dch.xml    Grek and Lis
  configs/gameplay/npc_profile_dch.xml       their profiles
  configs/gameplay/dialogs_dch.xml           dialogs (generated)
  configs/misc/squad_descr/squad_descr_dch.ltx  squads
  configs/misc/task/tm_dch.ltx               tasks
  configs/items/items/items_dch.ltx          quest items (vanilla icons and models)
  configs/text/eng/st_dch.xml                all texts (<id>_dolg: the Duty version)
tools/dch_gen_dialogs.py                     dialog generator
```

`dialogs_dch.xml` is generated: edit `tools/dch_gen_dialogs.py` and the texts, then run
`python tools/dch_gen_dialogs.py "Dead Channel - Storyline/gamedata"`.

Releases: tag `dch-vX.Y.Z` (the release workflow builds `Dead_Channel_Storyline_vX.Y.Z.zip`).
