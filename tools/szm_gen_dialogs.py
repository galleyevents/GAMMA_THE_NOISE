# Generates configs/gameplay/dialogs_szm.xml from the stage layout and the texts in st_szm.xml.
import os, re, sys
gd = sys.argv[1]
st = open(os.path.join(gd, "configs", "text", "eng", "st_szm.xml"), encoding="cp1251").read()
ids = set(re.findall(r'string id="([^"]+)"', st))

OFFERED_BY = {2: "sid", 3: "sid", 4: "sid", 5: "sid", 6: "sid",
              7: "spore", 8: "spore", 9: "spore", 10: "spore", 11: "spore",
              12: "cold", 13: "cold", 14: "sid", 15: "sid",
              # Act V: 17/19/21 after the giver's radio call, the rest straight from the report dialogs;
              # 23 by whoever was chosen in Act IV ("act5": the dialog is on all three, the script picks)
              17: "cold", 18: "cold", 19: "sid", 20: "sid", 21: "wolf", 22: "wolf", 23: "act5"}
# the stage offered right after a report, when it isn't n + 1
NEXT_OFFER = {18: 23, 20: 23, 22: 23}
TURNED_IN_TO = {1: "sid", 2: "sid", 3: "wolf", 4: "sid", 5: "sid",
                6: "spore", 7: "spore", 8: "spore", 9: "spore", 10: "spore",
                11: "cold", 12: "cold", 13: "sid", 14: "sid",
                # Act V: report dialogs only, the stages come over the radio (23-24 complete themselves)
                17: "cold", 18: "cold", 19: "sid", 20: "sid", 21: "wolf", 22: "wolf",
                25: "cold", 26: "sid", 27: "wolf"}

def ph(i, text, nexts=(), action=None, precond=()):
    s = '<phrase id="%d">' % i
    for p in precond:
        s += "<precondition>%s</precondition>" % p
    s += "<text>%s</text>" % text
    if action:
        s += "<action>%s</action>" % action
    for n in nexts:
        s += "<next>%d</next>" % n
    return s + "</phrase>"

# Phrases are built as (id, text, nexts, action, preconditions) and rendered at the end
def offer_phrases(m, who, base):
    """accept/decline block of stage m's offer, starting at phrase id base (actor's opener)"""
    b = base
    return [
        (b,     "szm_%d_offer_0" % m, [b + 1], None, ()),
        (b + 1, "szm_%d_offer_1" % m, [b + 2, b + 3], None, ()),
        (b + 2, "szm_%d_offer_2" % m, [b + 4], None, ()),
        (b + 3, "szm_offer_decline",  [b + 5], None, ()),
        (b + 4, "szm_%d_offer_4" % m, [], "szm_main.give_%d" % m, ()),
        (b + 5, "szm_declined_%s" % who, [], None, ()),
    ]

# Clear Sky actor: a phrase whose text has a <text>_csky variant gets a twin with that text (id + CSKY_OFFSET,
# same nexts and action); the preconditions pick one of the two
CSKY_OFFSET = 500

def csky_variants(phrases):
    twins = {q[0]: q[0] + CSKY_OFFSET for q in phrases if q[1] + "_csky" in ids}
    out = []
    for i, text, nexts, action, pre in phrases:
        nexts = [x for n in nexts for x in ([n, twins[n]] if n in twins else [n])]
        if i in twins:
            out.append((i, text, nexts, action, tuple(pre) + ("szm_main.actor_not_csky",)))
            out.append((twins[i], text + "_csky", nexts, action, tuple(pre) + ("szm_main.actor_csky",)))
        else:
            out.append((i, text, nexts, action, pre))
    return out

# Scaled rewards: when a gear reward is given as money (swap) or as a better but worn gun (worn), the NPC
# says szm_<kind>_<who>_<category> first, the actor answers szm_<kind>_ok and the reward line follows
# (a copy of it: the original is for "nothing to explain")
NOTES = (("swap", "weapon"), ("swap", "outfit"), ("swap", "backpack"), ("worn", "weapon"))
NOTE_BASE, OK_BASE, NOTE_REWARD = 200, 250, 300

def swap_branch(phrases, before, reward, who):
    """phrases: list of (id, text, nexts, action, precond); adds the note lines between phrase `before`
    (actor) and `reward` (NPC) if `who` has any"""
    notes = [(k, c) for k, c in NOTES if "szm_%s_%s_%s" % (k, who, c) in ids]
    if not notes:
        return
    kinds = sorted({k for k, c in notes})
    ok_id = {k: OK_BASE + j for j, k in enumerate(kinds)}
    p = {q[0]: q for q in phrases}
    i, text, nexts, action, pre = p[reward]
    phrases[phrases.index(p[reward])] = (i, text, nexts, action, tuple(pre) + ("szm_main.reward_not_swapped",))
    note_ids = [NOTE_BASE + j for j in range(len(notes))]
    b = p[before]
    phrases[phrases.index(b)] = (b[0], b[1], note_ids + [reward], b[3], b[4])
    for nid, (k, c) in zip(note_ids, notes):
        phrases.append((nid, "szm_%s_%s_%s" % (k, who, c), [ok_id[k]], None, ("szm_main.reward_%s_%s" % (k, c),)))
    for k in kinds:
        phrases.append((ok_id[k], "szm_%s_ok" % k, [NOTE_REWARD], None, ()))
    phrases.append((NOTE_REWARD, text, nexts, action, ()))

def render(phrases):
    return [ph(i, text, nexts, action, precond) for i, text, nexts, action, precond in csky_variants(phrases)]

def dialog(did, precond, phrases):
    out = ['\t<dialog id="%s">' % did, "\t\t<precondition>%s</precondition>" % precond, "\t\t<phrase_list>"]
    out += ["\t\t\t" + p for p in phrases]
    out += ["\t\t</phrase_list>", "\t</dialog>"]
    return "\n".join(out)

blocks = []
for n in range(1, 28):
    if n in OFFERED_BY:
        blocks.append(dialog("szm_%d_offer" % n, "szm_main.can_offer_%d" % n, render(offer_phrases(n, OFFERED_BY[n], 0))))
    if n in TURNED_IN_TO:
        lines = sorted((int(k) for k in re.findall(r'string id="szm_%d_done_(\d+)"' % n, st)))
        assert lines == list(range(len(lines))) and len(lines) % 2 == 0, (n, lines)
        k = len(lines) - 1          # the NPC's last line: rewards
        who = TURNED_IN_TO[n]
        phr = [(i, "szm_%d_done_%d" % (n, i), [i + 1], None, ()) for i in range(k)]
        m = NEXT_OFFER.get(n, n + 1)
        chain = OFFERED_BY.get(m) in (who, "act5")
        if chain:
            # straight into the next offer, or "later" (the offer dialog stays available)
            phr.append((k, "szm_%d_done_%d" % (n, k), [k + 1, k + 2], "szm_main.turn_in_%d" % n, ()))
            phr.append((k + 1, "szm_%d_offer_0" % m, [k + 3], None, ()))
            phr.append((k + 2, "szm_later", [k + 4], None, ()))
            phr.append((k + 3, "szm_%d_offer_1" % m, [k + 5, k + 6], None, ()))
            phr.append((k + 4, "szm_later_%s" % who, [], None, ()))
            phr.append((k + 5, "szm_%d_offer_2" % m, [k + 7], None, ()))
            phr.append((k + 6, "szm_offer_decline", [k + 8], None, ()))
            phr.append((k + 7, "szm_%d_offer_4" % m, [], "szm_main.give_%d" % m, ()))
            phr.append((k + 8, "szm_declined_%s" % who, [], None, ()))
        else:
            phr.append((k, "szm_%d_done_%d" % (n, k), [], "szm_main.turn_in_%d" % n, ()))
        swap_branch(phr, k - 1, k, who)
        blocks.append(dialog("szm_%d_done" % n, "szm_main.can_turn_in_%d" % n, render(phr)))

for who in ("cold", "sid", "wolf"):
    phr = [
        (0, "szm_16_%s_0" % who, [1], None, ()),
        (1, "szm_16_%s_1" % who, [2, 3], None, ()),
        (2, "szm_16_%s_2" % who, [4], None, ()),
        (3, "szm_16_think", [5], None, ()),
        (4, "szm_16_%s_4" % who, [], "szm_main.turn_in_16_%s" % who, ()),
        (5, "szm_16_%s_5" % who, [], None, ()),
    ]
    swap_branch(phr, 2, 4, who)
    # Sid's precondition also keeps a Clear Sky actor from selling the Kamerton
    precond = "szm_main.can_turn_in_16_sid" if who == "sid" else "szm_main.can_turn_in_16"
    blocks.append(dialog("szm_16_%s" % who, precond, render(phr)))

xml = '''<?xml version="1.0" encoding="windows-1251"?>
<!--
	The Noise - main storyline. Generated by szm_gen_dialogs.py - edit the generator, not this file.
	szm_n_offer: 0 actor ask, 1 npc briefing, 2 accept, 3 decline, 4 npc gives the task, 5 npc after decline
	szm_n_done : report and rewards, then (same NPC) the next offer right away or "later"
	szm_16_<who>: the Act IV choice (Cold / Sid / Wolf). Who says what is set in modxml_szm.script.
	500+: the Clear Sky actor's version of a phrase (text id + _csky)
	200+ / 250+ / 300: gear reward given as money or as a worn gun - the NPC's line, the actor's answer, the reward line
-->
<game_dialogs>

''' + "\n\n".join(blocks) + "\n\n</game_dialogs>\n"

used = re.findall(r"<text>([^<]+)</text>", xml)
missing = sorted({t for t in used if t not in ids})
assert not missing, missing
open(os.path.join(gd, "configs", "gameplay", "dialogs_szm.xml"), "w", encoding="cp1251", newline="").write(xml)
print("dialogs:", xml.count("<dialog id="))
