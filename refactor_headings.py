import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add CSS classes
css_addition = """
        .event-heading-en {
            font-family: 'Oswald', sans-serif;
            font-size: clamp(3.5rem, 8vw, 6.5rem) !important;
            font-weight: 900;
            text-transform: uppercase;
            letter-spacing: 2px;
            line-height: 1.1;
            color: var(--navy);
            margin-bottom: 20px;
        }
        .event-heading-jp {
            font-family: 'Noto Sans JP', sans-serif;
            font-size: clamp(1.8rem, 4vw, 2.5rem) !important;
            font-weight: 900;
            line-height: 1.4;
            letter-spacing: 1px;
            color: var(--navy);
            margin-bottom: 20px;
        }
"""
content = content.replace(".story-title {", css_addition + "        .story-title {")

# Also update story-subtitle
content = re.sub(r'\.story-subtitle\s*\{[^}]+\}', """.story-subtitle {
            font-family: 'Oswald', sans-serif;
            font-size: clamp(0.85rem, 2vw, 1.1rem) !important;
            font-weight: 900;
            color: var(--primary);
            letter-spacing: 4px;
            text-transform: uppercase;
            display: inline-block;
            margin-bottom: 15px;
        }""", content)

# Replace Japanese H2s
content = re.sub(r'<h2 class="story-title">誰もが主人公になれる、<br>最高の瞬間をデザインする。</h2>', '<h2 class="event-heading-jp">誰もが主人公になれる、<br>最高の瞬間をデザインする。</h2>', content)
content = re.sub(r'<h2 class="approach-title">熱狂を生み出し、人を惹きつける3つの仕掛け。</h2>', '<h2 class="event-heading-jp">熱狂を生み出し、人を惹きつける3つの仕掛け。</h2>', content)
content = re.sub(r'<h2 class="approach-title">その一瞬にある、熱狂と感動。</h2>', '<h2 class="event-heading-jp" style="text-align: center;">その一瞬にある、熱狂と感動。</h2>', content)
content = re.sub(r'<h2 class="approach-title">OSLを体験する4つのステップ。</h2>', '<h2 class="event-heading-jp" style="text-align: center;">OSLを体験する4つのステップ。</h2>', content)
content = re.sub(r'<h2 class="approach-title">よくあるご質問。</h2>', '<h2 class="event-heading-jp" style="text-align: center;">よくあるご質問。</h2>', content)

# Replace English H2s
content = re.sub(r'<h2 style="[^"]*">The Impact</h2>', '<h2 class="event-heading-en" style="text-align: center; margin-bottom: 60px;">The Impact</h2>', content)
content = re.sub(r'<h2 style="[^"]*">The OSL Ecosystem</h2>', '<h2 class="event-heading-en" style="text-align: center; margin-bottom: 60px;">The OSL Ecosystem</h2>', content)
content = re.sub(r'<h2 class="approach-title" style="[^"]*">Extreme Formats</h2>', '<h2 class="event-heading-en" style="text-align: center;">Extreme Formats</h2>', content)
content = re.sub(r'<h2 class="story-title" style="[^"]*">The Producer\'s<br>Desk</h2>', '<h2 class="event-heading-en">The Producer\'s<br>Desk</h2>', content)
content = re.sub(r'<h2 style="[^"]*">Bring Your Passion\.</h2>', '<h2 class="event-heading-en" style="text-align: center; margin-bottom: 50px; color: white;">Bring Your Passion.</h2>', content)
content = re.sub(r'<h2 style="[^"]*">Official Partners</h2>', '<h2 class="event-heading-en" style="text-align: center; margin-bottom: 50px;">Official Partners</h2>', content)

# Remove media queries that conflict with clamp
content = re.sub(r'\.story-title, \.approach-header h2, \.flow-header h2, \.faq-header h2, \.gallery-header h2\s*\{\s*font-size: clamp\([^}]+\}\s*', '', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Done")
