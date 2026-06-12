import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add global typography rules to the base CSS (after body {})
base_text_css = """
        /* --- Typography: Body Text --- */
        p, li {
            font-size: clamp(0.95rem, 2vw, 1.05rem);
            line-height: 1.9;
            letter-spacing: 0.03em;
            color: var(--navy);
            opacity: 0.85;
            margin-bottom: 25px;
        }
        p:last-child {
            margin-bottom: 0;
        }
        p strong, li strong {
            font-weight: 900;
            color: var(--primary);
            opacity: 1;
        }
        blockquote {
            border-left: 4px solid var(--primary);
            padding: 15px 0 15px 25px;
            margin: 40px 0;
            font-size: clamp(1.1rem, 2vw, 1.25rem);
            font-weight: 700;
            line-height: 1.8;
            letter-spacing: 0.05em;
            color: var(--navy);
            background: rgba(0, 178, 178, 0.05);
            border-radius: 0 4px 4px 0;
        }
        .text-light p, .text-light li {
            color: var(--white);
            opacity: 0.9;
        }
        .text-light p strong, .text-light li strong {
            color: var(--primary);
        }
"""
# Inject right after body { ... }
content = re.sub(r'(body\s*\{[^}]+\})', r'\1\n' + base_text_css, content)

# Remove conflicting inline styles or redundant CSS classes
# .story-right p
content = re.sub(r'\.story-right p\s*\{[^}]+\}', '', content)
content = re.sub(r'\.story-right p strong\s*\{[^}]+\}', '', content)
content = re.sub(r'\.story-right blockquote\s*\{[^}]+\}', '', content)

# .approach-card p
content = re.sub(r'\.approach-card p\s*\{[^}]+\}', '', content)

# MANIFESTO text wrapper: change inline line-height: 2.2; font-size: 1.05rem; color: rgba(255,255,255,0.85); to use class text-light
content = re.sub(r'<section class="section-manifesto"([^>]+)>', r'<section class="section-manifesto text-light"\1>', content)
content = re.sub(r'style="max-width: 800px; margin: 0 auto; line-height: 2\.2; font-size: 1\.05rem; color: rgba\(255,255,255,0\.85\);"', 'style="max-width: 800px; margin: 0 auto;"', content)
content = re.sub(r'<p style="margin-bottom: 30px;">', '<p>', content)
content = re.sub(r'<p style="margin-bottom: 50px;">', '<p style="margin-bottom: 50px;">', content) # keep the last one if it has special margin, actually let's just strip inline margins for p in manifesto
content = re.sub(r'<p style="margin-bottom: 30px;">', '<p>', content)

# Rules text
content = re.sub(r'<p style="color: var\(--navy\); opacity: 0\.8;">', '<p>', content)
content = re.sub(r'<p style="color: var\(--navy\); opacity: 0\.8; max-width: 700px; margin-left: auto; margin-right: auto;">', '<p style="max-width: 700px; margin-left: auto; margin-right: auto;">', content)

# Impact text
content = re.sub(r'<section class="section-impact"([^>]+)>', r'<section class="section-impact"\1>', content)

# Media query cleanups
content = re.sub(r'\.story-right p\s*\{\s*font-size:[^}]+\}', '', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Typography updated for body text.")
