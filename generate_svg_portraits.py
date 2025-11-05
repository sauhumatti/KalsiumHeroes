#!/usr/bin/env python3
"""Generate SVG character portraits for KalsiumHeroes units"""

import os

WIDTH, HEIGHT = 568, 600

def create_svg_header():
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{WIDTH}" height="{HEIGHT}" xmlns="http://www.w3.org/2000/svg">
<rect width="{WIDTH}" height="{HEIGHT}" fill="#808080"/>
'''

def create_svg_footer():
    return '</svg>'

def create_speedrunner_svg():
    """Athletic speedster with light armor and dynamic pose"""
    svg = create_svg_header()

    # Color definitions
    svg += '''
<!-- Speedrunner - Fast and agile -->
<defs>
    <linearGradient id="speedGrad" x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" style="stop-color:#5fa5dc;stop-opacity:1" />
        <stop offset="100%" style="stop-color:#235fa0;stop-opacity:1" />
    </linearGradient>
</defs>

<!-- Head -->
<ellipse cx="284" cy="150" rx="64" ry="70" fill="#efd5c0" stroke="#b49682" stroke-width="3"/>

<!-- Hair - spiky/windswept -->
<path d="M 250 90 L 200 70 L 210 100 L 230 80 L 260 60 L 290 75 L 310 65 L 330 80 L 340 100 L 320 90 Z"
      fill="#2d5587" stroke="#142850" stroke-width="2"/>

<!-- Eyes -->
<ellipse cx="260" cy="145" rx="10" ry="10" fill="#ffffff" stroke="#000000" stroke-width="2"/>
<ellipse cx="308" cy="145" rx="10" ry="10" fill="#ffffff" stroke="#000000" stroke-width="2"/>
<circle cx="260" cy="145" r="5" fill="#235fa0"/>
<circle cx="308" cy="145" r="5" fill="#235fa0"/>

<!-- Mouth -->
<path d="M 260 175 Q 284 180 308 175" fill="none" stroke="#785046" stroke-width="2"/>

<!-- Torso -->
<rect x="180" y="240" width="208" height="310" fill="url(#speedGrad)" stroke="#235fa0" stroke-width="3"/>

<!-- Vest -->
<path d="M 220 260 L 284 240 L 348 260 L 348 380 L 220 380 Z"
      fill="#235fa0" stroke="#0f3764" stroke-width="2"/>

<!-- Speed stripes -->
<line x1="240" y1="290" x2="280" y2="290" stroke="#dcf0ff" stroke-width="4" stroke-linecap="round"/>
<line x1="250" y1="320" x2="290" y2="320" stroke="#dcf0ff" stroke-width="4" stroke-linecap="round"/>
<line x1="260" y1="350" x2="300" y2="350" stroke="#dcf0ff" stroke-width="4" stroke-linecap="round"/>

<!-- Arms -->
<ellipse cx="170" cy="400" rx="30" ry="80" fill="url(#speedGrad)" stroke="#235fa0" stroke-width="3"/>
<ellipse cx="398" cy="380" rx="30" ry="80" fill="url(#speedGrad)" stroke="#235fa0" stroke-width="3"/>

<!-- Hands -->
<ellipse cx="165" cy="470" rx="20" ry="20" fill="#efd5c0" stroke="#b49682" stroke-width="2"/>
<ellipse cx="408" cy="450" rx="20" ry="20" fill="#efd5c0" stroke="#b49682" stroke-width="2"/>

<!-- Text label -->
<text x="284" y="580" font-family="Arial, sans-serif" font-size="16" fill="#235fa0" text-anchor="middle" font-weight="bold">SPEEDRUNNER</text>
'''

    return svg + create_svg_footer()

def create_lone_ranger_svg():
    """Ranger with hood and practical gear"""
    svg = create_svg_header()

    svg += '''
<!-- Lone Ranger - Precision marksman -->
<defs>
    <linearGradient id="rangerGrad" x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" style="stop-color:#6b8e23;stop-opacity:1" />
        <stop offset="100%" style="stop-color:#556b2f;stop-opacity:1" />
    </linearGradient>
</defs>

<!-- Hood -->
<path d="M 200 60 L 284 40 L 368 60 L 368 200 L 284 220 L 200 200 Z"
      fill="#556b2f" stroke="#323c1e" stroke-width="3"/>

<!-- Face -->
<ellipse cx="284" cy="155" rx="54" ry="55" fill="#efd5c0" stroke="#b49682" stroke-width="3"/>

<!-- Eyes - sharp -->
<ellipse cx="260" cy="145" rx="10" ry="8" fill="#ffffff" stroke="#000000" stroke-width="2"/>
<ellipse cx="308" cy="145" rx="10" ry="8" fill="#ffffff" stroke="#000000" stroke-width="2"/>
<circle cx="260" cy="145" r="5" fill="#46641e"/>
<circle cx="308" cy="145" r="5" fill="#46641e"/>

<!-- Serious mouth -->
<line x1="260" y1="175" x2="308" y2="175" stroke="#785046" stroke-width="2"/>

<!-- Cloak -->
<rect x="170" y="240" width="228" height="340" fill="url(#rangerGrad)" stroke="#3c5a19" stroke-width="3"/>

<!-- Leather chest piece -->
<ellipse cx="284" cy="325" rx="74" ry="75" fill="#8b5a2b" stroke="#5a3c1e" stroke-width="3"/>

<!-- Belt/strap -->
<rect x="200" y="380" width="168" height="30" fill="#8b5a2b" stroke="#5a3c1e" stroke-width="2"/>
<rect x="270" y="260" width="28" height="120" fill="#8b5a2b" stroke="#5a3c1e" stroke-width="2"/>

<!-- Buckle -->
<rect x="265" y="385" width="38" height="20" fill="#d2b48c" stroke="#967850" stroke-width="2"/>

<!-- Arms -->
<ellipse cx="160" cy="420" rx="30" ry="80" fill="url(#rangerGrad)" stroke="#3c5a19" stroke-width="3"/>
<ellipse cx="408" cy="420" rx="30" ry="80" fill="url(#rangerGrad)" stroke="#3c5a19" stroke-width="3"/>

<!-- Gloved hands -->
<ellipse cx="155" cy="490" rx="20" ry="20" fill="#8b5a2b" stroke="#5a3c1e" stroke-width="2"/>
<ellipse cx="413" cy="490" rx="20" ry="20" fill="#8b5a2b" stroke="#5a3c1e" stroke-width="2"/>

<!-- Text label -->
<text x="284" y="570" font-family="Arial, sans-serif" font-size="16" fill="#556b2f" text-anchor="middle" font-weight="bold">LONE RANGER</text>
'''

    return svg + create_svg_footer()

def create_golem_svg():
    """Massive stone creature"""
    svg = create_svg_header()

    svg += '''
<!-- Golem - Stone tank -->
<defs>
    <linearGradient id="stoneGrad" x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" style="stop-color:#a09b91;stop-opacity:1" />
        <stop offset="100%" style="stop-color:#4b4641;stop-opacity:1" />
    </linearGradient>
    <radialGradient id="crystalGlow">
        <stop offset="0%" style="stop-color:#c8e6ff;stop-opacity:1" />
        <stop offset="50%" style="stop-color:#64b4ff;stop-opacity:1" />
        <stop offset="100%" style="stop-color:#3278b4;stop-opacity:1" />
    </radialGradient>
</defs>

<!-- Large blocky head -->
<rect x="190" y="70" width="188" height="170" fill="url(#stoneGrad)" stroke="#4b4641" stroke-width="4"/>

<!-- Rock texture on head -->
<rect x="210" y="90" width="15" height="15" fill="#4b4641" opacity="0.5"/>
<rect x="250" y="110" width="20" height="20" fill="#a09b91" opacity="0.3"/>
<rect x="300" y="95" width="12" height="12" fill="#4b4641" opacity="0.6"/>
<rect x="340" y="130" width="18" height="18" fill="#4b4641" opacity="0.4"/>
<rect x="220" y="180" width="25" height="25" fill="#a09b91" opacity="0.4"/>
<rect x="320" y="200" width="22" height="22" fill="#4b4641" opacity="0.5"/>

<!-- Glowing crystal eyes -->
<ellipse cx="240" cy="150" rx="20" ry="20" fill="url(#crystalGlow)" stroke="#326496" stroke-width="3"/>
<ellipse cx="328" cy="150" rx="20" ry="20" fill="url(#crystalGlow)" stroke="#326496" stroke-width="3"/>
<ellipse cx="240" cy="150" rx="10" ry="10" fill="#c8e6ff"/>
<ellipse cx="328" cy="150" rx="10" ry="10" fill="#c8e6ff"/>

<!-- Massive shoulders and torso -->
<path d="M 150 260 L 418 260 L 450 400 L 380 590 L 188 590 L 118 400 Z"
      fill="url(#stoneGrad)" stroke="#4b4641" stroke-width="4"/>

<!-- Rock texture on body -->
<rect x="180" y="300" width="25" height="25" fill="#4b4641" opacity="0.6"/>
<rect x="240" y="330" width="30" height="30" fill="#a09b91" opacity="0.4"/>
<rect x="320" y="310" width="20" height="20" fill="#4b4641" opacity="0.5"/>
<rect x="370" y="380" width="28" height="28" fill="#4b4641" opacity="0.6"/>
<rect x="200" y="450" width="22" height="22" fill="#a09b91" opacity="0.4"/>
<rect x="300" y="480" width="35" height="35" fill="#4b4641" opacity="0.5"/>
<rect x="350" y="520" width="25" height="25" fill="#4b4641" opacity="0.6"/>

<!-- Crystal core -->
<path d="M 270 340 L 298 340 L 310 370 L 298 400 L 270 400 L 258 370 Z"
      fill="url(#crystalGlow)" stroke="#326496" stroke-width="3"/>
<ellipse cx="284" cy="370" rx="15" ry="20" fill="#c8e6ff" opacity="0.7"/>

<!-- Shoulder plates -->
<path d="M 150 260 L 120 300 L 140 350 L 180 320 Z" fill="#a09b91" stroke="#4b4641" stroke-width="3"/>
<path d="M 418 260 L 448 300 L 428 350 L 388 320 Z" fill="#a09b91" stroke="#4b4641" stroke-width="3"/>

<!-- Massive arms -->
<ellipse cx="125" cy="435" rx="45" ry="95" fill="url(#stoneGrad)" stroke="#4b4641" stroke-width="4"/>
<ellipse cx="443" cy="435" rx="45" ry="95" fill="url(#stoneGrad)" stroke="#4b4641" stroke-width="4"/>

<!-- Stone fists -->
<ellipse cx="115" cy="540" rx="40" ry="40" fill="#4b4641" stroke="#a09b91" stroke-width="3"/>
<ellipse cx="453" cy="540" rx="40" ry="40" fill="#4b4641" stroke="#a09b91" stroke-width="3"/>

<!-- Text label -->
<text x="284" y="580" font-family="Arial, sans-serif" font-size="20" fill="#64b4ff" text-anchor="middle" font-weight="bold">GOLEM</text>
'''

    return svg + create_svg_footer()

def create_rogue_mage_hunter_svg():
    """Anti-mage specialist"""
    svg = create_svg_header()

    svg += '''
<!-- Rogue Mage Hunter - Anti-magic specialist -->
<defs>
    <linearGradient id="hunterGrad" x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" style="stop-color:#552d6e;stop-opacity:1" />
        <stop offset="100%" style="stop-color:#2d193c;stop-opacity:1" />
    </linearGradient>
    <radialGradient id="magicGlow">
        <stop offset="0%" style="stop-color:#d896ff;stop-opacity:0.9" />
        <stop offset="50%" style="stop-color:#b464ff;stop-opacity:0.7" />
        <stop offset="100%" style="stop-color:#8c3cc8;stop-opacity:0.3" />
    </radialGradient>
</defs>

<!-- Head -->
<ellipse cx="284" cy="150" rx="64" ry="70" fill="#efd5c0" stroke="#b49682" stroke-width="3"/>

<!-- Dark hair -->
<ellipse cx="240" cy="105" rx="40" ry="35" fill="#1e1428" stroke="#0a050f" stroke-width="2"/>
<ellipse cx="328" cy="105" rx="40" ry="35" fill="#1e1428" stroke="#0a050f" stroke-width="2"/>
<rect x="200" y="90" width="168" height="30" fill="#1e1428"/>

<!-- Intense eyes with magic glow -->
<ellipse cx="255" cy="145" rx="10" ry="10" fill="#ffffff" stroke="#000000" stroke-width="2"/>
<ellipse cx="313" cy="145" rx="10" ry="10" fill="#ffffff" stroke="#000000" stroke-width="2"/>
<circle cx="255" cy="145" r="5" fill="#b464ff"/>
<circle cx="313" cy="145" r="5" fill="#b464ff"/>
<ellipse cx="255" cy="145" rx="15" ry="15" fill="url(#magicGlow)" opacity="0.3"/>
<ellipse cx="313" cy="145" rx="15" ry="15" fill="url(#magicGlow)" opacity="0.3"/>

<!-- Face scar -->
<line x1="270" y1="145" x2="240" y2="170" stroke="#c89696" stroke-width="2"/>

<!-- Grim mouth -->
<path d="M 260 180 Q 284 175 308 180" fill="none" stroke="#785046" stroke-width="2"/>

<!-- Armored coat -->
<rect x="180" y="240" width="208" height="340" fill="url(#hunterGrad)" stroke="#140a1e" stroke-width="3"/>

<!-- Chest armor plate -->
<path d="M 230 260 L 284 245 L 338 260 L 330 400 L 238 400 Z"
      fill="#b4b4be" stroke="#787882" stroke-width="3"/>

<!-- Magical runes on armor -->
<g opacity="0.8">
    <circle cx="260" cy="285" r="8" fill="none" stroke="#b464ff" stroke-width="2"/>
    <line x1="260" y1="277" x2="260" y2="293" stroke="#b464ff" stroke-width="1"/>
    <line x1="252" y1="285" x2="268" y2="285" stroke="#b464ff" stroke-width="1"/>

    <circle cx="308" cy="285" r="8" fill="none" stroke="#b464ff" stroke-width="2"/>
    <line x1="308" y1="277" x2="308" y2="293" stroke="#b464ff" stroke-width="1"/>
    <line x1="300" y1="285" x2="316" y2="285" stroke="#b464ff" stroke-width="1"/>

    <circle cx="284" cy="320" r="8" fill="none" stroke="#b464ff" stroke-width="2"/>
    <line x1="284" y1="312" x2="284" y2="328" stroke="#b464ff" stroke-width="1"/>
    <line x1="276" y1="320" x2="292" y2="320" stroke="#b464ff" stroke-width="1"/>

    <circle cx="260" cy="355" r="8" fill="none" stroke="#b464ff" stroke-width="2"/>
    <line x1="260" y1="347" x2="260" y2="363" stroke="#b464ff" stroke-width="1"/>
    <line x1="252" y1="355" x2="268" y2="355" stroke="#b464ff" stroke-width="1"/>

    <circle cx="308" cy="355" r="8" fill="none" stroke="#b464ff" stroke-width="2"/>
    <line x1="308" y1="347" x2="308" y2="363" stroke="#b464ff" stroke-width="1"/>
    <line x1="300" y1="355" x2="316" y2="355" stroke="#b464ff" stroke-width="1"/>
</g>

<!-- Belt with pouches -->
<rect x="190" y="430" width="188" height="30" fill="#552d6e" stroke="#281432" stroke-width="2"/>
<rect x="210" y="445" width="30" height="35" fill="#552d6e" stroke="#281432" stroke-width="2"/>
<rect x="328" y="445" width="30" height="35" fill="#552d6e" stroke="#281432" stroke-width="2"/>

<!-- Arms -->
<ellipse cx="170" cy="410" rx="30" ry="90" fill="url(#hunterGrad)" stroke="#140a1e" stroke-width="3"/>
<ellipse cx="398" cy="410" rx="30" ry="90" fill="url(#hunterGrad)" stroke="#140a1e" stroke-width="3"/>

<!-- Armored gauntlets -->
<rect x="145" y="460" width="40" height="50" fill="#b4b4be" stroke="#787882" stroke-width="2"/>
<rect x="383" y="460" width="40" height="50" fill="#b4b4be" stroke="#787882" stroke-width="2"/>

<!-- Glowing magic suppression on right hand -->
<ellipse cx="403" cy="478" rx="28" ry="28" fill="url(#magicGlow)" opacity="0.6"/>
<rect x="383" y="460" width="40" height="50" fill="#b4b4be" stroke="#787882" stroke-width="2"/>

<!-- Text label -->
<text x="284" y="565" font-family="Arial, sans-serif" font-size="14" fill="#b464ff" text-anchor="middle" font-weight="bold">ROGUE MAGE HUNTER</text>
'''

    return svg + create_svg_footer()

def main():
    output_dir = '/home/user/KalsiumHeroes/KalsiumHeroes/Assets/Graphics/Sprites/UI/Units/Sprite'

    print("Generating SVG character portraits...")

    portraits = {
        'Speedrunner.svg': create_speedrunner_svg(),
        'LoneRanger.svg': create_lone_ranger_svg(),
        'Golem.svg': create_golem_svg(),
        'RogueMageHunter.svg': create_rogue_mage_hunter_svg(),
    }

    for filename, svg_content in portraits.items():
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'w') as f:
            f.write(svg_content)
        print(f"Created: {filepath}")

    print("\nAll SVG portraits generated successfully!")
    print("\nNote: Unity can import SVG files. You may also want to convert these to PNG")
    print("using a tool like Inkscape or ImageMagick for better compatibility.")

if __name__ == '__main__':
    main()
