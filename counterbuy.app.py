import streamlit as st
from collections import defaultdict

# 1. CHARACTER DATABASE
HERO_COUNTERS = {
    "Abrams": ["Healbane", "Inhibitor", "Crippling Headshot", "Indomitable", "Unstoppable"],
    "Apollo": ["Slowing Hex", "Counterspell", "Spellbreaker"],
    "Bebop": ["Dispel Magic", "Counterspell", "Indomitable", "Knockdown"],
    "Billy": ["Toxic Bullets", "Siphon Bullets", "Rebuttal"],
    "Calico": ["Slowing Hex", "Spirit Shielding", "Counterspell", "Warpstone"],
    "Celeste": ["Spirit Res", "Spellbreaker", "Silence Wave"],
    "Doorman": ["Spirit Shielding", "Counterspell", "Dispel Magic", "Unstoppable", "Indomitable"],
    "Dynamo": ["Slowing Hex", "Healbane", "Inhibitor", "Spirit Shielding", "Knockdown", "Unstoppable", "Ethereal Shift"],
    "Graves": ["Spirit Shielding", "Reactive Barrier", "Indomitable", "Spirit Resilience", "Monster Rounds"],
    "Gray Talon": ["Spellbreaker", "Counterspell"],
    "Haze": ["Rusted Barrel", "Disarming Hex", "Metal Skin", "Plated Armor"],
    "Holliday": ["Spell Breaker", "Indomitable", "Rescue Beam", "Slowing Hex", "Counterspell"],
    "Infernus": ["Dispel Magic", "Counterspell", "Ethereal Shift", "Rusted Barrel", "Disarming Hex"],
    "Kelvin": ["Healbane", "Silence Wave", "Spirit Resilience", "Unstoppable"],
    "Lady Geist": ["Silence Wave"],
    "Lash": ["Counterspell", "Unstoppable", "Spellbreaker", "Warpstone"],
    "McGinnis": ["Monster Rounds", "Warpstone", "Spirit Resilience"],
    "Mina": ["Spirit Resilience", "Knockdown", "Slowing Hex"],
    "Mirage": ["Dispel Magic", "Spellbreaker"],
    "Mo & Krill": ["Indomitable", "Siphon Bullets", "Spirit Resilience"],
    "Paige": ["Reactive Barrier", "Indomitable", "Counterspell", "Disarming Hex"],
    "Paradox": ["Silence Wave", "Warpstone"],
    "Pocket": ["Silence Wave", "Divine Barrier"],
    "Rem": ["Counterspell", "Slowing Hex", "Healbane", "Inhibitor", "Monster Rounds"],
    "Seven": ["Knockdown", "Dispel Magic", "Counterspell", "Indomitable", "Warpstone"],
    "Shiv": ["Dispel Magic", "Spirit Shielding", "Spellbreaker", "Counterspell", "Metal Skin"],
    "Silver": ["Metal Skin", "Plated Armor", "Slowing Hex", "Rusted Barrel", "Disarming Hex"],
    "Sinclair": ["Slowing Hex", "Counterspell", "Reactive Barrier", "Spellbreaker"],
    "Venator": ["Bullet Resilience", "Reactive Barrier", "Indomitable", "Metal Skin"],
    "Victor": ["Crippling Headshot," "Healbane," "Inhibitor," "Reactive Barrier", "Indomitable", "Warpstone"],
    "Vindicta": ["Phantom Strike", "Knockdown", "Dispel Magic", "Metal Skin", "Plated Armor", "Rusted Barrel", "Disarming Hex"],
    "Viscous": ["Rebuttal", "Healbane", "Inhibitor", "Silence Wave", "Reactive Barrier", "Indomitable"],
    "Vyper": ["Rusted Barrel", "Disarming Hex", "Slowing Hex", "Plated Armor", "Metal Skin", "Reactive Barrier", "Indomitable", "Dispel Magic"],
    "Warden": ["Crippling Headshot", "Dispel Magic", "Metal Skin"],
    "Wraith": ["Slowing Hex", "Silence Wave," "Reactive Barrier", "Indomitable", "Rusted Barrel", "Disarming Hex", "Metal Skin", "Plated Armor"],
    "Yamato": ["Dispel Magic", "Spellbreaker", "Spellbreaker", "Counterspell", "Slowing Hex"],
}

# 2. STREAMLIT UI LAYOUT
st.set_page_config(page_title="Deadlock Counterbuy Tool", layout="wide")

st.title("pastry counterbuy bot 🤖")
st.write("stop the momentum of problematic characters before they torment your team")

# Multi-select dropdown
selected_team = st.multiselect(
    "select enemy heroes(max 6):",
    options=sorted(list(HERO_COUNTERS.keys())),
    max_selections=6
)

# 3. REAL-TIME CALCULATION & DISPLAY
if selected_team:
    item_overlap = defaultdict(list)
    for hero in selected_team:
        for item in HERO_COUNTERS[hero]:
            item_overlap[item].append(hero)

    # Sort by overlap count
    sorted_items = sorted(item_overlap.items(), key=lambda x: len(x[1]), reverse=True)

    # Format into table data
    table_data = [
        {
            "counter": item,
            "relevant to": len(targets),
            "counters": ", ".join(targets)
        }
        for item, targets in sorted_items
    ]

    st.subheader("counterbuys")
    st.dataframe(
        table_data, 
        use_container_width=True,
        hide_index=True
    )
else:
    st.info("type or select up to 6 characters for relevant counterbuys 🍰")