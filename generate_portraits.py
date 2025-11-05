#!/usr/bin/env python3
"""Generate character portraits for KalsiumHeroes units"""

from PIL import Image, ImageDraw, ImageFont
import os

# Portrait dimensions to match Duelist.png
WIDTH, HEIGHT = 568, 600
BACKGROUND = (128, 128, 128)  # Gray background like Duelist

def create_speedrunner():
    """Athletic speedster with light armor and dynamic pose"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BACKGROUND)
    draw = ImageDraw.Draw(img)

    # Color scheme: Blues and cyans for speed/agility
    skin = (239, 213, 192)
    hair = (45, 85, 135)
    outfit_light = (95, 165, 220)
    outfit_dark = (35, 95, 160)
    accent = (220, 240, 255)

    # Head/neck
    draw.ellipse([220, 80, 348, 220], fill=skin, outline=(180, 150, 130), width=3)

    # Hair - spiky/windswept
    points = [(250, 90), (200, 70), (210, 100), (230, 80), (260, 60),
              (290, 75), (310, 65), (330, 80), (340, 100), (320, 90)]
    draw.polygon(points, fill=hair, outline=(20, 40, 80), width=2)

    # Eyes - alert and focused
    draw.ellipse([250, 135, 270, 155], fill=(255, 255, 255), outline=(0, 0, 0), width=2)
    draw.ellipse([298, 135, 318, 155], fill=(255, 255, 255), outline=(0, 0, 0), width=2)
    draw.ellipse([255, 140, 265, 150], fill=(35, 95, 160))
    draw.ellipse([303, 140, 313, 150], fill=(35, 95, 160))

    # Mouth - determined
    draw.arc([250, 165, 318, 185], 200, 340, fill=(120, 80, 70), width=2)

    # Torso - light athletic wear
    draw.rectangle([180, 240, 388, 550], fill=outfit_light, outline=outfit_dark, width=3)

    # Vest/armor accent
    draw.polygon([(220, 260), (284, 240), (348, 260), (348, 380), (220, 380)],
                 fill=outfit_dark, outline=(15, 55, 100), width=2)

    # Speed stripes accent
    for i in range(3):
        y = 290 + i * 30
        draw.line([230 + i*10, y, 270 + i*10, y], fill=accent, width=4)

    # Arms - dynamic pose
    draw.ellipse([140, 320, 200, 480], fill=outfit_light, outline=outfit_dark, width=3)
    draw.ellipse([368, 300, 428, 460], fill=outfit_light, outline=outfit_dark, width=3)

    # Hands
    draw.ellipse([145, 450, 185, 490], fill=skin, outline=(180, 150, 130), width=2)
    draw.ellipse([388, 430, 428, 470], fill=skin, outline=(180, 150, 130), width=2)

    return img

def create_lone_ranger():
    """Ranger/archer with hood and practical gear"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BACKGROUND)
    draw = ImageDraw.Draw(img)

    # Color scheme: Forest greens and browns
    skin = (239, 213, 192)
    hood = (85, 107, 47)
    outfit = (107, 142, 35)
    leather = (139, 90, 43)
    accent = (210, 180, 140)

    # Hood
    draw.polygon([(200, 60), (284, 40), (368, 60), (368, 200), (284, 220), (200, 200)],
                 fill=hood, outline=(50, 70, 30), width=3)

    # Face in shadow
    draw.ellipse([230, 100, 338, 210], fill=skin, outline=(180, 150, 130), width=3)

    # Eyes - sharp and calculating
    draw.ellipse([250, 135, 270, 150], fill=(255, 255, 255), outline=(0, 0, 0), width=2)
    draw.ellipse([298, 135, 318, 150], fill=(255, 255, 255), outline=(0, 0, 0), width=2)
    draw.ellipse([255, 138, 265, 147], fill=(70, 100, 30))
    draw.ellipse([303, 138, 313, 147], fill=(70, 100, 30))

    # Mouth - serious
    draw.line([260, 175, 308, 175], fill=(120, 80, 70), width=2)

    # Cloak/outfit
    draw.rectangle([170, 240, 398, 580], fill=outfit, outline=(60, 90, 25), width=3)

    # Leather chest piece
    draw.ellipse([210, 250, 358, 400], fill=leather, outline=(90, 60, 30), width=3)

    # Belt/strap
    draw.rectangle([200, 380, 368, 410], fill=leather, outline=(90, 60, 30), width=2)
    draw.rectangle([270, 260, 298, 380], fill=leather, outline=(90, 60, 30), width=2)

    # Buckle
    draw.rectangle([265, 385, 303, 405], fill=accent, outline=(150, 120, 80), width=2)

    # Arms
    draw.ellipse([130, 340, 190, 500], fill=outfit, outline=(60, 90, 25), width=3)
    draw.ellipse([378, 340, 438, 500], fill=outfit, outline=(60, 90, 25), width=3)

    # Hands with gloves
    draw.ellipse([135, 470, 175, 510], fill=leather, outline=(90, 60, 30), width=2)
    draw.ellipse([393, 470, 433, 510], fill=leather, outline=(90, 60, 30), width=2)

    return img

def create_golem():
    """Massive stone creature with rocky texture"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BACKGROUND)
    draw = ImageDraw.Draw(img)

    # Color scheme: Grays and earth tones
    stone_base = (120, 115, 110)
    stone_dark = (75, 70, 65)
    stone_light = (160, 155, 145)
    crystal = (100, 180, 255)

    # Large blocky head
    draw.rectangle([190, 70, 378, 240], fill=stone_base, outline=stone_dark, width=4)

    # Rock texture - random blocks
    import random
    random.seed(42)  # Consistent generation
    for _ in range(15):
        x = random.randint(195, 360)
        y = random.randint(75, 230)
        size = random.randint(8, 20)
        color = random.choice([stone_dark, stone_light, stone_base])
        draw.rectangle([x, y, x+size, y+size], fill=color, outline=stone_dark, width=1)

    # Eyes - glowing crystals
    draw.ellipse([220, 130, 260, 170], fill=crystal, outline=(50, 100, 150), width=3)
    draw.ellipse([308, 130, 348, 170], fill=crystal, outline=(50, 100, 150), width=3)
    draw.ellipse([230, 140, 250, 160], fill=(200, 230, 255))
    draw.ellipse([318, 140, 338, 160], fill=(200, 230, 255))

    # Massive shoulders and torso
    draw.polygon([(150, 260), (418, 260), (450, 400), (380, 600), (188, 600), (118, 400)],
                 fill=stone_base, outline=stone_dark, width=4)

    # More rock texture on body
    for _ in range(25):
        x = random.randint(130, 430)
        y = random.randint(265, 590)
        size = random.randint(10, 30)
        color = random.choice([stone_dark, stone_light, stone_base])
        draw.rectangle([x, y, x+size, y+size], fill=color, outline=stone_dark, width=1)

    # Crystal core
    draw.polygon([(270, 340), (298, 340), (310, 370), (298, 400), (270, 400), (258, 370)],
                 fill=crystal, outline=(50, 100, 150), width=3)

    # Shoulder plates
    draw.polygon([(150, 260), (120, 300), (140, 350), (180, 320)],
                 fill=stone_light, outline=stone_dark, width=3)
    draw.polygon([(418, 260), (448, 300), (428, 350), (388, 320)],
                 fill=stone_light, outline=stone_dark, width=3)

    # Arms - massive
    draw.ellipse([80, 340, 170, 530], fill=stone_base, outline=stone_dark, width=4)
    draw.ellipse([398, 340, 488, 530], fill=stone_base, outline=stone_dark, width=4)

    # Hands - stone fists
    draw.ellipse([75, 500, 155, 580], fill=stone_dark, outline=stone_light, width=3)
    draw.ellipse([413, 500, 493, 580], fill=stone_dark, outline=stone_light, width=3)

    return img

def create_rogue_mage_hunter():
    """Anti-mage specialist with enchanted gear"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BACKGROUND)
    draw = ImageDraw.Draw(img)

    # Color scheme: Dark purples, blacks, silver
    skin = (239, 213, 192)
    outfit_dark = (45, 25, 60)
    outfit_mid = (85, 45, 110)
    armor = (180, 180, 190)
    magic_glow = (180, 100, 255)

    # Head
    draw.ellipse([220, 80, 348, 220], fill=skin, outline=(180, 150, 130), width=3)

    # Hair - swept back
    draw.ellipse([200, 70, 280, 140], fill=(30, 20, 40), outline=(10, 5, 15), width=2)
    draw.ellipse([288, 70, 368, 140], fill=(30, 20, 40), outline=(10, 5, 15), width=2)
    draw.rectangle([200, 90, 368, 120], fill=(30, 20, 40))

    # Eyes - intense
    draw.ellipse([245, 135, 265, 155], fill=(255, 255, 255), outline=(0, 0, 0), width=2)
    draw.ellipse([303, 135, 323, 155], fill=(255, 255, 255), outline=(0, 0, 0), width=2)
    draw.ellipse([250, 140, 260, 150], fill=magic_glow)
    draw.ellipse([308, 140, 318, 150], fill=magic_glow)

    # Face scar
    draw.line([270, 145, 240, 170], fill=(200, 150, 150), width=2)

    # Mouth - grim
    draw.arc([250, 170, 318, 190], 200, 340, fill=(120, 80, 70), width=2)

    # Armored coat
    draw.rectangle([180, 240, 388, 580], fill=outfit_dark, outline=(20, 10, 30), width=3)

    # Chest armor plate
    draw.polygon([(230, 260), (284, 245), (338, 260), (330, 400), (238, 400)],
                 fill=armor, outline=(120, 120, 130), width=3)

    # Magical runes on armor
    rune_positions = [(260, 285), (308, 285), (284, 320), (260, 355), (308, 355)]
    for x, y in rune_positions:
        draw.ellipse([x-6, y-6, x+6, y+6], outline=magic_glow, width=2)
        draw.line([x, y-8, x, y+8], fill=magic_glow, width=1)
        draw.line([x-8, y, x+8, y], fill=magic_glow, width=1)

    # Belt with pouches
    draw.rectangle([190, 430, 378, 460], fill=outfit_mid, outline=(40, 20, 50), width=2)
    draw.rectangle([210, 445, 240, 480], fill=outfit_mid, outline=(40, 20, 50), width=2)
    draw.rectangle([328, 445, 358, 480], fill=outfit_mid, outline=(40, 20, 50), width=2)

    # Arms
    draw.ellipse([140, 320, 200, 500], fill=outfit_dark, outline=(20, 10, 30), width=3)
    draw.ellipse([368, 320, 428, 500], fill=outfit_dark, outline=(20, 10, 30), width=3)

    # Armored gauntlets
    draw.rectangle([145, 460, 185, 510], fill=armor, outline=(120, 120, 130), width=2)
    draw.rectangle([383, 460, 423, 510], fill=armor, outline=(120, 120, 130), width=2)

    # Glowing hand - magic suppression
    draw.ellipse([375, 450, 431, 506], fill=magic_glow, outline=magic_glow, width=15)
    draw.rectangle([383, 460, 423, 510], fill=armor, outline=(120, 120, 130), width=2)

    return img

def main():
    output_dir = '/home/user/KalsiumHeroes/KalsiumHeroes/Assets/Graphics/Sprites/UI/Units/Sprite'

    print("Generating character portraits...")

    portraits = {
        'Speedrunner.png': create_speedrunner(),
        'LoneRanger.png': create_lone_ranger(),
        'Golem.png': create_golem(),
        'RogueMageHunter.png': create_rogue_mage_hunter(),
    }

    for filename, img in portraits.items():
        filepath = os.path.join(output_dir, filename)
        img.save(filepath, 'PNG')
        print(f"Created: {filepath}")

    print("All portraits generated successfully!")

if __name__ == '__main__':
    main()
