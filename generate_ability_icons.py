#!/usr/bin/env python3
"""Generate ability icons for KalsiumHeroes units"""

import os

# Standard icon size
SIZE = 128

def create_svg_icon(content, bg_color="#1a1a1a", border_color="#3a3a3a"):
    """Create an SVG icon with standard structure"""
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{SIZE}" height="{SIZE}" xmlns="http://www.w3.org/2000/svg">
<defs>
    <radialGradient id="bgGrad">
        <stop offset="0%" style="stop-color:{bg_color};stop-opacity:1" />
        <stop offset="100%" style="stop-color:#000000;stop-opacity:1" />
    </radialGradient>
</defs>
<rect width="{SIZE}" height="{SIZE}" fill="url(#bgGrad)" stroke="{border_color}" stroke-width="3"/>
{content}
</svg>'''

def duelist_cordial_invitation():
    """Spell that taunts/invites enemy - invitation card with magical aura"""
    content = '''
<!-- Invitation card/letter -->
<rect x="30" y="35" width="68" height="85" fill="#f5f5dc" stroke="#d4af37" stroke-width="3" rx="5"/>
<line x1="40" y1="55" x2="88" y2="55" stroke="#d4af37" stroke-width="2"/>
<line x1="40" y1="70" x2="88" y2="70" stroke="#d4af37" stroke-width="2"/>
<line x1="40" y1="85" x2="88" y2="85" stroke="#d4af37" stroke-width="2"/>

<!-- Wax seal -->
<circle cx="64" cy="100" r="15" fill="#8b0000" stroke="#5a0000" stroke-width="2"/>
<text x="64" y="108" font-family="serif" font-size="20" fill="#5a0000" text-anchor="middle" font-weight="bold">D</text>

<!-- Magical sparkles -->
<circle cx="25" cy="30" r="3" fill="#ffd700" opacity="0.8"/>
<circle cx="103" cy="45" r="2" fill="#ffd700" opacity="0.8"/>
<circle cx="20" cy="100" r="2.5" fill="#ffd700" opacity="0.8"/>
<circle cx="108" cy="115" r="3" fill="#ffd700" opacity="0.8"/>
'''
    return create_svg_icon(content, "#2d1a3d", "#d4af37")

def duelist_parry_stance():
    """Defensive stance - crossed swords/defensive posture"""
    content = '''
<!-- Shield in center -->
<path d="M 64 25 L 85 35 L 85 80 Q 64 100 64 100 Q 64 100 43 80 L 43 35 Z"
      fill="#c0c0c0" stroke="#808080" stroke-width="3"/>

<!-- Shield boss -->
<circle cx="64" cy="55" r="12" fill="#d4af37" stroke="#b8930b" stroke-width="2"/>

<!-- Sword crossing -->
<line x1="35" y1="40" x2="93" y2="88" stroke="#e0e0e0" stroke-width="5"/>
<line x1="93" y1="40" x2="35" y2="88" stroke="#e0e0e0" stroke-width="5"/>
<line x1="35" y1="40" x2="93" y2="88" stroke="#a0a0a0" stroke-width="3"/>
<line x1="93" y1="40" x2="35" y2="88" stroke="#a0a0a0" stroke-width="3"/>

<!-- Defensive aura -->
<circle cx="64" cy="64" r="55" fill="none" stroke="#4169e1" stroke-width="2" opacity="0.5"/>
'''
    return create_svg_icon(content, "#1a2d3d", "#4169e1")

def duelist_target_weak_spot():
    """Precision attack - target reticle with highlighted weak point"""
    content = '''
<!-- Target circles -->
<circle cx="64" cy="64" r="50" fill="none" stroke="#ff6b6b" stroke-width="3"/>
<circle cx="64" cy="64" r="35" fill="none" stroke="#ff6b6b" stroke-width="2"/>
<circle cx="64" cy="64" r="20" fill="none" stroke="#ff6b6b" stroke-width="2"/>

<!-- Crosshair -->
<line x1="14" y1="64" x2="50" y2="64" stroke="#ff4444" stroke-width="3"/>
<line x1="78" y1="64" x2="114" y2="64" stroke="#ff4444" stroke-width="3"/>
<line x1="64" y1="14" x2="64" y2="50" stroke="#ff4444" stroke-width="3"/>
<line x1="64" y1="78" x2="64" y2="114" stroke="#ff4444" stroke-width="3"/>

<!-- Weak spot indicator (X) -->
<circle cx="64" cy="64" r="8" fill="#ff0000" opacity="0.7"/>
<line x1="56" y1="56" x2="72" y2="72" stroke="#ffffff" stroke-width="3"/>
<line x1="72" y1="56" x2="56" y2="72" stroke="#ffffff" stroke-width="3"/>

<!-- Scanning lines -->
<line x1="20" y1="30" x2="45" y2="45" stroke="#ff6b6b" stroke-width="1" opacity="0.6"/>
<line x1="108" y1="30" x2="83" y2="45" stroke="#ff6b6b" stroke-width="1" opacity="0.6"/>
'''
    return create_svg_icon(content, "#2d1a1a", "#ff4444")

def duelist_opportunist():
    """Passive - eye watching for opportunities"""
    content = '''
<!-- Eye shape -->
<ellipse cx="64" cy="64" rx="45" ry="30" fill="#ffffff" stroke="#2a2a2a" stroke-width="3"/>

<!-- Iris -->
<circle cx="64" cy="64" r="18" fill="#d4af37" stroke="#b8930b" stroke-width="2"/>

<!-- Pupil -->
<circle cx="64" cy="64" r="10" fill="#1a1a1a"/>

<!-- Highlight -->
<circle cx="58" cy="58" r="4" fill="#ffffff" opacity="0.8"/>

<!-- Observant marks around eye -->
<path d="M 25 50 Q 20 64 25 78" fill="none" stroke="#d4af37" stroke-width="2"/>
<path d="M 103 50 Q 108 64 103 78" fill="none" stroke="#d4af37" stroke-width="2"/>
<line x1="40" y1="35" x2="50" y2="45" stroke="#d4af37" stroke-width="2"/>
<line x1="88" y1="35" x2="78" y2="45" stroke="#d4af37" stroke-width="2"/>
'''
    return create_svg_icon(content, "#2d2d1a", "#d4af37")

def speedrunner_move():
    """Movement ability - running figure with speed lines"""
    content = '''
<!-- Speed lines -->
<line x1="10" y1="40" x2="50" y2="40" stroke="#5fa5dc" stroke-width="4" stroke-linecap="round" opacity="0.7"/>
<line x1="15" y1="55" x2="60" y2="55" stroke="#5fa5dc" stroke-width="4" stroke-linecap="round" opacity="0.7"/>
<line x1="10" y1="70" x2="55" y2="70" stroke="#5fa5dc" stroke-width="4" stroke-linecap="round" opacity="0.7"/>
<line x1="15" y1="85" x2="50" y2="85" stroke="#5fa5dc" stroke-width="4" stroke-linecap="round" opacity="0.7"/>

<!-- Running figure (simplified) -->
<circle cx="85" cy="45" r="12" fill="#dcf0ff" stroke="#5fa5dc" stroke-width="2"/>
<line x1="85" y1="57" x2="85" y2="85" stroke="#dcf0ff" stroke-width="6" stroke-linecap="round"/>
<!-- Forward-leaning leg -->
<line x1="85" y1="85" x2="105" y2="105" stroke="#dcf0ff" stroke-width="5" stroke-linecap="round"/>
<!-- Back leg -->
<line x1="85" y1="85" x2="75" y2="100" stroke="#dcf0ff" stroke-width="5" stroke-linecap="round"/>
<!-- Arms -->
<line x1="85" y1="65" x2="105" y2="75" stroke="#dcf0ff" stroke-width="5" stroke-linecap="round"/>
<line x1="85" y1="65" x2="70" y2="55" stroke="#dcf0ff" stroke-width="5" stroke-linecap="round"/>
'''
    return create_svg_icon(content, "#1a2d3d", "#5fa5dc")

def speedrunner_speed_gain():
    """Speed boost - lightning bolt with upward arrow"""
    content = '''
<!-- Lightning bolt -->
<path d="M 64 15 L 50 55 L 68 55 L 54 105 L 85 60 L 65 60 Z"
      fill="#ffd700" stroke="#ff8c00" stroke-width="2"/>

<!-- Speed boost aura -->
<circle cx="64" cy="64" r="55" fill="none" stroke="#5fa5dc" stroke-width="2" opacity="0.4" stroke-dasharray="5,5"/>
<circle cx="64" cy="64" r="45" fill="none" stroke="#5fa5dc" stroke-width="2" opacity="0.4" stroke-dasharray="5,5"/>

<!-- Upward motion arrows -->
<path d="M 95 85 L 105 95 L 115 85" fill="none" stroke="#dcf0ff" stroke-width="3" stroke-linecap="round"/>
<path d="M 95 100 L 105 110 L 115 100" fill="none" stroke="#dcf0ff" stroke-width="3" stroke-linecap="round"/>
'''
    return create_svg_icon(content, "#1a1a2d", "#ffd700")

def speedrunner_side_kick():
    """Kick attack - boot/foot kicking with impact"""
    content = '''
<!-- Leg/Boot -->
<ellipse cx="45" cy="75" rx="8" ry="20" fill="#235fa0" stroke="#142850" stroke-width="2" transform="rotate(-30 45 75)"/>
<path d="M 52 85 L 70 90 L 75 95 L 70 102 L 58 98 Z"
      fill="#2d5587" stroke="#142850" stroke-width="2"/>

<!-- Impact burst -->
<circle cx="85" cy="95" r="3" fill="#ff6b6b"/>
<circle cx="95" cy="90" r="4" fill="#ff8c8c"/>
<circle cx="100" cy="100" r="3" fill="#ff6b6b"/>
<circle cx="90" cy="103" r="2.5" fill="#ff8c8c"/>

<!-- Motion arc -->
<path d="M 30 50 Q 60 60 85 90" fill="none" stroke="#dcf0ff" stroke-width="3" stroke-dasharray="5,3"/>

<!-- Impact lines -->
<line x1="85" y1="90" x2="105" y2="85" stroke="#ff6b6b" stroke-width="3" stroke-linecap="round"/>
<line x1="88" y1="95" x2="110" y2="100" stroke="#ff6b6b" stroke-width="3" stroke-linecap="round"/>
<line x1="85" y1="100" x2="105" y2="110" stroke="#ff6b6b" stroke-width="3" stroke-linecap="round"/>
'''
    return create_svg_icon(content, "#1a2d3d", "#235fa0")

def lone_ranger_pick_off():
    """Ranged attack - arrow hitting target"""
    content = '''
<!-- Arrow -->
<line x1="25" y1="35" x2="85" y2="85" stroke="#8b5a2b" stroke-width="5"/>
<path d="M 85 85 L 75 80 L 80 75 Z" fill="#696969" stroke="#505050" stroke-width="1"/>
<!-- Arrow fletching -->
<path d="M 25 35 L 20 30 L 28 32 Z" fill="#d2691e" stroke="#8b4513" stroke-width="1"/>
<path d="M 25 35 L 20 40 L 28 38 Z" fill="#d2691e" stroke="#8b4513" stroke-width="1"/>

<!-- Crosshair/Target at impact -->
<circle cx="95" cy="95" r="20" fill="none" stroke="#ff4444" stroke-width="2"/>
<circle cx="95" cy="95" r="10" fill="none" stroke="#ff4444" stroke-width="2"/>
<line x1="85" y1="95" x2="105" y2="95" stroke="#ff4444" stroke-width="2"/>
<line x1="95" y1="85" x2="95" y2="105" stroke="#ff4444" stroke-width="2"/>

<!-- Impact effect -->
<circle cx="95" cy="95" r="5" fill="#ff0000" opacity="0.7"/>

<!-- Trajectory line -->
<line x1="15" y1="25" x2="30" y2="40" stroke="#556b2f" stroke-width="2" stroke-dasharray="3,3" opacity="0.6"/>
'''
    return create_svg_icon(content, "#1a2d1a", "#d2691e")

def lone_ranger_shove():
    """Push/displacement - hand pushing with force lines"""
    content = '''
<!-- Hand pushing -->
<path d="M 40 64 L 55 50 L 60 52 L 63 48 L 68 50 L 70 46 L 75 48 L 75 75 L 40 75 Z"
      fill="#8b5a2b" stroke="#5a3c1e" stroke-width="2"/>

<!-- Force wave -->
<path d="M 80 50 Q 95 64 80 78" fill="none" stroke="#6b8e23" stroke-width="4" stroke-linecap="round"/>
<path d="M 90 45 Q 105 64 90 83" fill="none" stroke="#6b8e23" stroke-width="3" stroke-linecap="round" opacity="0.7"/>
<path d="M 100 40 Q 115 64 100 88" fill="none" stroke="#6b8e23" stroke-width="2" stroke-linecap="round" opacity="0.5"/>

<!-- Impact particles -->
<circle cx="85" cy="55" r="3" fill="#9acd32" opacity="0.8"/>
<circle cx="95" cy="64" r="4" fill="#9acd32" opacity="0.8"/>
<circle cx="88" cy="73" r="3" fill="#9acd32" opacity="0.8"/>

<!-- Direction arrow -->
<path d="M 105 64 L 115 54 L 115 74 Z" fill="#6b8e23" opacity="0.7"/>
'''
    return create_svg_icon(content, "#1a2d1a", "#6b8e23")

def lone_ranger_shrapnel():
    """AOE damage - explosion with flying fragments"""
    content = '''
<!-- Central explosion -->
<circle cx="64" cy="64" r="20" fill="#ff6b00" opacity="0.7"/>
<circle cx="64" cy="64" r="15" fill="#ff8c00" opacity="0.8"/>
<circle cx="64" cy="64" r="10" fill="#ffa500"/>

<!-- Shrapnel pieces -->
<path d="M 64 30 L 68 35 L 60 35 Z" fill="#696969" stroke="#404040" stroke-width="1"/>
<path d="M 95 50 L 98 55 L 92 57 Z" fill="#696969" stroke="#404040" stroke-width="1"/>
<path d="M 105 75 L 108 80 L 103 82 Z" fill="#696969" stroke="#404040" stroke-width="1"/>
<path d="M 90 95 L 93 100 L 87 100 Z" fill="#696969" stroke="#404040" stroke-width="1"/>
<path d="M 50 105 L 53 110 L 48 108 Z" fill="#696969" stroke="#404040" stroke-width="1"/>
<path d="M 25 85 L 28 90 L 23 88 Z" fill="#696969" stroke="#404040" stroke-width="1"/>
<path d="M 20 55 L 23 60 L 18 58 Z" fill="#696969" stroke="#404040" stroke-width="1"/>
<path d="M 35 35 L 38 40 L 33 38 Z" fill="#696969" stroke="#404040" stroke-width="1"/>

<!-- Trajectory lines -->
<line x1="64" y1="44" x2="64" y2="25" stroke="#ff6b00" stroke-width="2" opacity="0.5"/>
<line x1="84" y1="54" x2="100" y2="45" stroke="#ff6b00" stroke-width="2" opacity="0.5"/>
<line x1="90" y1="74" x2="110" y2="70" stroke="#ff6b00" stroke-width="2" opacity="0.5"/>
<line x1="74" y1="84" x2="95" y2="100" stroke="#ff6b00" stroke-width="2" opacity="0.5"/>
<line x1="54" y1="84" x2="45" y2="110" stroke="#ff6b00" stroke-width="2" opacity="0.5"/>
<line x1="44" y1="74" x2="20" y2="90" stroke="#ff6b00" stroke-width="2" opacity="0.5"/>
<line x1="44" y1="54" x2="15" y2="50" stroke="#ff6b00" stroke-width="2" opacity="0.5"/>
<line x1="54" y1="44" x2="30" y2="30" stroke="#ff6b00" stroke-width="2" opacity="0.5"/>

<!-- AOE circle indicator -->
<circle cx="64" cy="64" r="50" fill="none" stroke="#ff6b00" stroke-width="2" opacity="0.4" stroke-dasharray="5,3"/>
'''
    return create_svg_icon(content, "#2d1a1a", "#ff6b00")

def golem_armor_bash():
    """Heavy attack - fist smashing down"""
    content = '''
<!-- Stone fist -->
<ellipse cx="64" cy="75" rx="30" ry="25" fill="#787873" stroke="#4b4641" stroke-width="3"/>
<rect x="45" y="50" width="38" height="30" fill="#5a5751" stroke="#4b4641" stroke-width="3"/>
<!-- Knuckles/texture -->
<rect x="48" y="65" width="10" height="12" fill="#4b4641" opacity="0.5"/>
<rect x="59" y="68" width="10" height="12" fill="#4b4641" opacity="0.5"/>
<rect x="70" y="65" width="10" height="12" fill="#4b4641" opacity="0.5"/>

<!-- Impact effect -->
<line x1="30" y1="105" x2="50" y2="95" stroke="#ffd700" stroke-width="4" stroke-linecap="round"/>
<line x1="98" y1="105" x2="78" y2="95" stroke="#ffd700" stroke-width="4" stroke-linecap="round"/>
<line x1="50" y1="110" x2="64" y2="100" stroke="#ffd700" stroke-width="3" stroke-linecap="round"/>
<line x1="78" y1="110" x2="64" y2="100" stroke="#ffd700" stroke-width="3" stroke-linecap="round"/>

<!-- Ground impact waves -->
<path d="M 20 110 Q 64 105 108 110" fill="none" stroke="#8b7355" stroke-width="3"/>
<path d="M 15 118 Q 64 112 113 118" fill="none" stroke="#8b7355" stroke-width="2" opacity="0.7"/>

<!-- Motion lines -->
<line x1="45" y1="25" x2="50" y2="45" stroke="#a09b91" stroke-width="3" opacity="0.6" stroke-linecap="round"/>
<line x1="64" y1="20" x2="64" y2="45" stroke="#a09b91" stroke-width="3" opacity="0.6" stroke-linecap="round"/>
<line x1="83" y1="25" x2="78" y2="45" stroke="#a09b91" stroke-width="3" opacity="0.6" stroke-linecap="round"/>
'''
    return create_svg_icon(content, "#1a1a1a", "#787873")

def golem_rock_shield():
    """Defense buff - stone shield with crystals"""
    content = '''
<!-- Large stone shield -->
<path d="M 64 20 L 95 35 L 95 85 Q 64 110 64 110 Q 64 110 33 85 L 33 35 Z"
      fill="#787873" stroke="#4b4641" stroke-width="4"/>

<!-- Rock texture -->
<rect x="50" y="45" width="12" height="12" fill="#4b4641" opacity="0.5"/>
<rect x="70" y="55" width="15" height="15" fill="#4b4641" opacity="0.5"/>
<rect x="55" y="75" width="10" height="10" fill="#4b4641" opacity="0.5"/>

<!-- Crystal embedded in center -->
<path d="M 64 50 L 72 58 L 64 75 L 56 58 Z"
      fill="#64b4ff" stroke="#326496" stroke-width="2"/>
<path d="M 64 50 L 72 58 L 64 62 Z" fill="#c8e6ff" opacity="0.7"/>

<!-- Protective aura -->
<circle cx="64" cy="64" r="55" fill="none" stroke="#64b4ff" stroke-width="2" opacity="0.4"/>
<circle cx="64" cy="64" r="48" fill="none" stroke="#64b4ff" stroke-width="2" opacity="0.3"/>
'''
    return create_svg_icon(content, "#1a1a2d", "#64b4ff")

def golem_earthquake():
    """AOE ground attack - cracked earth with shockwaves"""
    content = '''
<!-- Ground cracks -->
<line x1="64" y1="64" x2="30" y2="30" stroke="#8b7355" stroke-width="4" stroke-linecap="round"/>
<line x1="64" y1="64" x2="98" y2="35" stroke="#8b7355" stroke-width="4" stroke-linecap="round"/>
<line x1="64" y1="64" x2="105" y2="75" stroke="#8b7355" stroke-width="4" stroke-linecap="round"/>
<line x1="64" y1="64" x2="90" y2="105" stroke="#8b7355" stroke-width="4" stroke-linecap="round"/>
<line x1="64" y1="64" x2="35" y2="100" stroke="#8b7355" stroke-width="4" stroke-linecap="round"/>
<line x1="64" y1="64" x2="23" y2="70" stroke="#8b7355" stroke-width="4" stroke-linecap="round"/>

<!-- Central impact point -->
<circle cx="64" cy="64" r="12" fill="#4b4641" stroke="#2a2a2a" stroke-width="2"/>
<circle cx="64" cy="64" r="6" fill="#2a2a2a"/>

<!-- Shockwave rings -->
<circle cx="64" cy="64" r="30" fill="none" stroke="#8b7355" stroke-width="3" opacity="0.7"/>
<circle cx="64" cy="64" r="45" fill="none" stroke="#8b7355" stroke-width="2" opacity="0.5"/>
<circle cx="64" cy="64" r="58" fill="none" stroke="#8b7355" stroke-width="2" opacity="0.3"/>

<!-- Dust particles -->
<circle cx="35" cy="40" r="3" fill="#a09b91" opacity="0.7"/>
<circle cx="90" cy="45" r="4" fill="#a09b91" opacity="0.7"/>
<circle cx="100" cy="80" r="3" fill="#a09b91" opacity="0.7"/>
<circle cx="85" cy="100" r="3.5" fill="#a09b91" opacity="0.7"/>
<circle cx="40" cy="95" r="4" fill="#a09b91" opacity="0.7"/>
<circle cx="28" cy="75" r="3" fill="#a09b91" opacity="0.7"/>
'''
    return create_svg_icon(content, "#1a1a1a", "#8b7355")

def golem_rock_solid():
    """Passive - solid rock formation"""
    content = '''
<!-- Main boulder/rock -->
<ellipse cx="64" cy="70" rx="40" ry="35" fill="#787873" stroke="#4b4641" stroke-width="4"/>
<ellipse cx="50" cy="55" rx="30" ry="25" fill="#5a5751" stroke="#4b4641" stroke-width="3"/>
<ellipse cx="80" cy="60" rx="25" ry="22" fill="#5a5751" stroke="#4b4641" stroke-width="3"/>

<!-- Rock texture -->
<rect x="45" y="60" width="15" height="15" fill="#4b4641" opacity="0.4"/>
<rect x="70" y="68" width="12" height="12" fill="#4b4641" opacity="0.5"/>
<rect x="55" y="80" width="18" height="18" fill="#4b4641" opacity="0.4"/>

<!-- Immovable indicator - ground roots/foundation -->
<rect x="30" y="100" width="68" height="8" fill="#3a3a3a" opacity="0.8"/>
<rect x="25" y="108" width="78" height="5" fill="#2a2a2a" opacity="0.6"/>

<!-- Stability lines -->
<line x1="35" y1="95" x2="35" y2="105" stroke="#4b4641" stroke-width="3"/>
<line x1="50" y1="95" x2="50" y2="105" stroke="#4b4641" stroke-width="3"/>
<line x="64" y1="95" x2="64" y2="105" stroke="#4b4641" stroke-width="3"/>
<line x1="78" y1="95" x2="78" y2="105" stroke="#4b4641" stroke-width="3"/>
<line x1="93" y1="95" x2="93" y2="105" stroke="#4b4641" stroke-width="3"/>
'''
    return create_svg_icon(content, "#1a1a1a", "#787873")

def mage_hunter_hunt_the_mark():
    """Tracking ability - marked target with tracking magic"""
    content = '''
<!-- Target silhouette -->
<ellipse cx="64" cy="45" rx="15" ry="18" fill="#3a2050" stroke="#b464ff" stroke-width="2" opacity="0.7"/>
<rect x="50" y="63" width="28" height="35" fill="#3a2050" stroke="#b464ff" stroke-width="2" opacity="0.7"/>
<ellipse cx="54" cy="98" rx="6" ry="15" fill="#3a2050" stroke="#b464ff" stroke-width="2" opacity="0.7"/>
<ellipse cx="74" cy="98" rx="6" ry="15" fill="#3a2050" stroke="#b464ff" stroke-width="2" opacity="0.7"/>

<!-- Magical tracking marks -->
<circle cx="64" cy="45" r="8" fill="none" stroke="#b464ff" stroke-width="2"/>
<line x1="64" y1="37" x2="64" y2="25" stroke="#b464ff" stroke-width="2"/>
<line x1="64" y1="53" x2="64" y2="65" stroke="#b464ff" stroke-width="2"/>
<line x1="56" y1="45" x2="44" y2="45" stroke="#b464ff" stroke-width="2"/>
<line x1="72" y1="45" x2="84" y2="45" stroke="#b464ff" stroke-width="2"/>

<!-- Tracking particles -->
<circle cx="35" cy="30" r="3" fill="#b464ff" opacity="0.8"/>
<circle cx="93" cy="35" r="2.5" fill="#b464ff" opacity="0.8"/>
<circle cx="30" cy="70" r="3" fill="#b464ff" opacity="0.8"/>
<circle cx="98" cy="75" r="2.5" fill="#b464ff" opacity="0.8"/>
<circle cx="40" cy="105" r="3" fill="#b464ff" opacity="0.8"/>
<circle cx="88" cy="108" r="3" fill="#b464ff" opacity="0.8"/>

<!-- Tracking lines converging on target -->
<line x1="35" y1="30" x2="54" y2="40" stroke="#b464ff" stroke-width="1" opacity="0.5"/>
<line x1="93" y1="35" x2="74" y2="42" stroke="#b464ff" stroke-width="1" opacity="0.5"/>
<line x1="30" y1="70" x2="50" y2="60" stroke="#b464ff" stroke-width="1" opacity="0.5"/>
<line x1="98" y1="75" x2="78" y2="65" stroke="#b464ff" stroke-width="1" opacity="0.5"/>
'''
    return create_svg_icon(content, "#1a0a2d", "#b464ff")

def mage_hunter_swift_strike():
    """Quick attack - blade with speed effect"""
    content = '''
<!-- Blade -->
<path d="M 95 25 L 100 30 L 45 85 L 40 80 Z"
      fill="#c0c0c0" stroke="#808080" stroke-width="2"/>
<path d="M 100 30 L 105 35 L 50 90 L 45 85 Z"
      fill="#e0e0e0" stroke="#a0a0a0" stroke-width="1"/>

<!-- Blade tip -->
<path d="M 95 25 L 100 20 L 105 25 L 100 30 Z"
      fill="#a0a0a0" stroke="#707070" stroke-width="1"/>

<!-- Hilt -->
<rect x="35" y="85" width="15" height="8" fill="#552d6e" stroke="#2d193c" stroke-width="1" transform="rotate(-45 42.5 89)"/>
<circle cx="42" cy="89" r="4" fill="#b464ff" stroke="#8c3cc8" stroke-width="1"/>

<!-- Speed effect - multiple afterimages -->
<path d="M 90 30 L 95 35 L 40 90 L 35 85 Z"
      fill="#b464ff" opacity="0.3" stroke="none"/>
<path d="M 85 35 L 90 40 L 35 95 L 30 90 Z"
      fill="#b464ff" opacity="0.2" stroke="none"/>

<!-- Motion lines -->
<line x1="75" y1="20" x2="85" y2="30" stroke="#b464ff" stroke-width="2" opacity="0.6" stroke-linecap="round"/>
<line x1="70" y1="30" x2="80" y2="40" stroke="#b464ff" stroke-width="2" opacity="0.6" stroke-linecap="round"/>
<line x1="65" y1="40" x2="75" y2="50" stroke="#b464ff" stroke-width="2" opacity="0.6" stroke-linecap="round"/>

<!-- Impact spark -->
<circle cx="72" cy="56" r="4" fill="#ffffff" opacity="0.8"/>
<line x1="66" y1="50" x2="60" y2="44" stroke="#ffffff" stroke-width="2" opacity="0.6" stroke-linecap="round"/>
<line x1="78" y1="50" x2="84" y2="44" stroke="#ffffff" stroke-width="2" opacity="0.6" stroke-linecap="round"/>
<line x1="72" y1="62" x2="72" y2="70" stroke="#ffffff" stroke-width="2" opacity="0.6" stroke-linecap="round"/>
'''
    return create_svg_icon(content, "#1a0a2d", "#c0c0c0")

def mage_hunter_castigation():
    """Anti-magic - shattered spell with suppression symbol"""
    content = '''
<!-- Broken magic circle -->
<path d="M 64 20 A 40 40 0 0 1 95 45" fill="none" stroke="#b464ff" stroke-width="3" opacity="0.6" stroke-dasharray="5,3"/>
<path d="M 100 55 A 40 40 0 0 1 90 85" fill="none" stroke="#b464ff" stroke-width="3" opacity="0.6" stroke-dasharray="5,3"/>
<path d="M 82 92 A 40 40 0 0 1 45 95" fill="none" stroke="#b464ff" stroke-width="3" opacity="0.6" stroke-dasharray="5,3"/>
<path d="M 35 90 A 40 40 0 0 1 25 55" fill="none" stroke="#b464ff" stroke-width="3" opacity="0.6" stroke-dasharray="5,3"/>
<path d="M 27 45 A 40 40 0 0 1 50 22" fill="none" stroke="#b464ff" stroke-width="3" opacity="0.6" stroke-dasharray="5,3"/>

<!-- Suppression X -->
<line x1="35" y1="35" x2="93" y2="93" stroke="#ff4444" stroke-width="6"/>
<line x1="93" y1="35" x2="35" y2="93" stroke="#ff4444" stroke-width="6"/>

<!-- Shattered magic particles -->
<circle cx="30" cy="25" r="3" fill="#b464ff" opacity="0.5"/>
<circle cx="98" cy="30" r="2.5" fill="#b464ff" opacity="0.5"/>
<circle cx="105" cy="70" r="3" fill="#b464ff" opacity="0.5"/>
<circle cx="95" cy="105" r="2.5" fill="#b464ff" opacity="0.5"/>
<circle cx="50" cy="110" r="3" fill="#b464ff" opacity="0.5"/>
<circle cx="20" cy="90" r="2.5" fill="#b464ff" opacity="0.5"/>
<circle cx="18" cy="50" r="3" fill="#b464ff" opacity="0.5"/>

<!-- Anti-magic rune in center -->
<circle cx="64" cy="64" r="15" fill="none" stroke="#ff4444" stroke-width="2"/>
<path d="M 64 52 L 64 76" stroke="#ff4444" stroke-width="2"/>
<path d="M 52 64 L 76 64" stroke="#ff4444" stroke-width="2"/>
<circle cx="64" cy="64" r="5" fill="#ff4444"/>
'''
    return create_svg_icon(content, "#1a0a2d", "#ff4444")

def mage_hunter_opportune_flight():
    """Mobility - figure leaping/evading with magic trail"""
    content = '''
<!-- Figure leaping -->
<circle cx="75" cy="40" r="10" fill="#d4b4e0" stroke="#b464ff" stroke-width="2"/>
<line x1="75" y1="50" x2="75" y2="70" stroke="#d4b4e0" stroke-width="5" stroke-linecap="round"/>
<!-- Legs in motion -->
<line x1="75" y1="70" x2="85" y2="55" stroke="#d4b4e0" stroke-width="4" stroke-linecap="round"/>
<line x1="75" y1="70" x2="65" y2="85" stroke="#d4b4e0" stroke-width="4" stroke-linecap="round"/>
<!-- Arms -->
<line x1="75" y1="55" x2="90" y2="50" stroke="#d4b4e0" stroke-width="4" stroke-linecap="round"/>
<line x1="75" y1="55" x2="65" y2="48" stroke="#d4b4e0" stroke-width="4" stroke-linecap="round"/>

<!-- Movement arc -->
<path d="M 30 85 Q 50 50 75 40" fill="none" stroke="#b464ff" stroke-width="3" stroke-dasharray="5,3" opacity="0.7"/>

<!-- Magic trail -->
<circle cx="32" cy="83" r="4" fill="#b464ff" opacity="0.7"/>
<circle cx="40" cy="72" r="3.5" fill="#b464ff" opacity="0.6"/>
<circle cx="47" cy="62" r="3" fill="#b464ff" opacity="0.5"/>
<circle cx="55" cy="53" r="2.5" fill="#b464ff" opacity="0.4"/>
<circle cx="63" cy="46" r="2" fill="#b464ff" opacity="0.3"/>

<!-- Speed effect -->
<line x1="25" y1="90" x2="35" y2="82" stroke="#552d6e" stroke-width="3" opacity="0.5" stroke-linecap="round"/>
<line x1="30" y1="95" x2="38" y2="88" stroke="#552d6e" stroke-width="2" opacity="0.4" stroke-linecap="round"/>

<!-- Evasion indicator -->
<path d="M 95 75 Q 100 64 95 53" fill="none" stroke="#b464ff" stroke-width="2" stroke-dasharray="3,2" opacity="0.6"/>
<path d="M 100 73 Q 105 64 100 55" fill="none" stroke="#b464ff" stroke-width="2" stroke-dasharray="3,2" opacity="0.4"/>
'''
    return create_svg_icon(content, "#1a0a2d", "#b464ff")

def mage_hunter_marked_hunter():
    """Passive - hunter's mark with magic sensing"""
    content = '''
<!-- Hunter's mark - stylized eye with crosshair -->
<ellipse cx="64" cy="64" rx="40" ry="28" fill="none" stroke="#b464ff" stroke-width="3"/>

<!-- Inner targeting reticle -->
<circle cx="64" cy="64" r="20" fill="none" stroke="#b464ff" stroke-width="2"/>
<circle cx="64" cy="64" r="12" fill="none" stroke="#b464ff" stroke-width="2"/>

<!-- Crosshair -->
<line x1="64" y1="44" x2="64" y2="30" stroke="#b464ff" stroke-width="2"/>
<line x1="64" y1="84" x2="64" y2="98" stroke="#b464ff" stroke-width="2"/>
<line x1="44" y1="64" x2="30" y2="64" stroke="#b464ff" stroke-width="2"/>
<line x1="84" y1="64" x2="98" y2="64" stroke="#b464ff" stroke-width="2"/>

<!-- Central mark -->
<circle cx="64" cy="64" r="6" fill="#b464ff" opacity="0.8"/>
<circle cx="64" cy="64" r="3" fill="#ffffff"/>

<!-- Magic sensing particles orbiting -->
<circle cx="64" cy="36" r="3" fill="#d896ff" opacity="0.8"/>
<circle cx="90" cy="50" r="2.5" fill="#d896ff" opacity="0.8"/>
<circle cx="90" cy="78" r="3" fill="#d896ff" opacity="0.8"/>
<circle cx="64" cy="92" r="2.5" fill="#d896ff" opacity="0.8"/>
<circle cx="38" cy="78" r="3" fill="#d896ff" opacity="0.8"/>
<circle cx="38" cy="50" r="2.5" fill="#d896ff" opacity="0.8"/>

<!-- Corner marks -->
<line x1="32" y1="46" x2="38" y2="52" stroke="#b464ff" stroke-width="2"/>
<line x1="32" y1="52" x2="38" y2="46" stroke="#b464ff" stroke-width="2"/>
<line x1="96" y1="46" x2="90" y2="52" stroke="#b464ff" stroke-width="2"/>
<line x1="96" y1="52" x2="90" y2="46" stroke="#b464ff" stroke-width="2"/>
<line x1="32" y1="76" x2="38" y2="82" stroke="#b464ff" stroke-width="2"/>
<line x1="32" y1="82" x2="38" y2="76" stroke="#b464ff" stroke-width="2"/>
<line x1="96" y1="76" x2="90" y2="82" stroke="#b464ff" stroke-width="2"/>
<line x1="96" y1="82" x2="90" y2="76" stroke="#b464ff" stroke-width="2"/>
'''
    return create_svg_icon(content, "#1a0a2d", "#b464ff")

def main():
    output_dir = '/home/user/KalsiumHeroes/KalsiumHeroes/Assets/Graphics/Sprites/UI/Abilities/Icons'

    abilities = {
        # Duelist
        'CordialInvitation.svg': duelist_cordial_invitation(),
        'ParryStance.svg': duelist_parry_stance(),
        'TargetWeakSpot.svg': duelist_target_weak_spot(),
        'Opportunist.svg': duelist_opportunist(),

        # Speedrunner
        'SpeedrunnerMove.svg': speedrunner_move(),
        'SpeedGain.svg': speedrunner_speed_gain(),
        'SideKick.svg': speedrunner_side_kick(),

        # Lone Ranger
        'PickOff.svg': lone_ranger_pick_off(),
        'Shove.svg': lone_ranger_shove(),
        'Shrapnel.svg': lone_ranger_shrapnel(),

        # Golem
        'ArmorBash.svg': golem_armor_bash(),
        'RockShield.svg': golem_rock_shield(),
        'Earthquake.svg': golem_earthquake(),
        'RockSolid.svg': golem_rock_solid(),

        # Rogue Mage Hunter
        'HuntTheMark.svg': mage_hunter_hunt_the_mark(),
        'SwiftStrike.svg': mage_hunter_swift_strike(),
        'CastigationOfCasting.svg': mage_hunter_castigation(),
        'OpportuneFlight.svg': mage_hunter_opportune_flight(),
        'MarkedHunter.svg': mage_hunter_marked_hunter(),
    }

    print(f"Generating {len(abilities)} ability icons...")

    for filename, svg_content in abilities.items():
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'w') as f:
            f.write(svg_content)
        print(f"Created: {filename}")

    print(f"\nAll {len(abilities)} ability icons generated successfully!")
    print(f"Location: {output_dir}")

if __name__ == '__main__':
    main()
