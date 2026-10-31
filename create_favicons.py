import os
from PIL import Image, ImageDraw, ImageFont

output_dir = r"C:\Users\dasan\.gemini\antigravity\scratch\grihakon-interiors-kolkata\assets\images"
os.makedirs(output_dir, exist_ok=True)

# 1. logo.svg
logo_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 100" width="520" height="100">
  <defs>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F3E7C4" />
      <stop offset="50%" stop-color="#D4AF37" />
      <stop offset="100%" stop-color="#AA8214" />
    </linearGradient>
    <linearGradient id="emeraldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#143D30" />
      <stop offset="100%" stop-color="#081E17" />
    </linearGradient>
  </defs>
  <!-- Architectural Emblem: stylized roofline & geometric spatial corner -->
  <rect x="10" y="10" width="80" height="80" rx="16" fill="url(#emeraldGrad)" stroke="url(#goldGrad)" stroke-width="2.5" />
  <path d="M 50 24 L 74 44 L 66 44 L 66 72 L 54 72 L 54 56 L 46 56 L 46 72 L 34 72 L 34 44 L 26 44 Z" fill="none" stroke="url(#goldGrad)" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" />
  <circle cx="50" cy="46" r="3" fill="#D4AF37" />

  <!-- Typography -->
  <text x="108" y="52" font-family="'Cinzel', 'Playfair Display', Georgia, serif" font-size="34" font-weight="700" letter-spacing="2" fill="#FFFFFF">GRIHAKON</text>
  <text x="110" y="78" font-family="'Montserrat', 'Helvetica Neue', sans-serif" font-size="12" font-weight="500" letter-spacing="4" fill="#D4AF37">INTERIOR DESIGN &amp; RENOVATION</text>
</svg>'''

with open(os.path.join(output_dir, "logo.svg"), "w", encoding="utf-8") as f:
    f.write(logo_svg)

# 2. favicon.svg
favicon_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <linearGradient id="favGold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F3E7C4" />
      <stop offset="50%" stop-color="#D4AF37" />
      <stop offset="100%" stop-color="#AA8214" />
    </linearGradient>
    <linearGradient id="favBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#143D30" />
      <stop offset="100%" stop-color="#081E17" />
    </linearGradient>
  </defs>
  <rect x="0" y="0" width="100" height="100" rx="20" fill="url(#favBg)" />
  <rect x="2" y="2" width="96" height="96" rx="18" fill="none" stroke="url(#favGold)" stroke-width="3" />
  <path d="M 50 18 L 78 42 L 70 42 L 70 76 L 56 76 L 56 58 L 44 58 L 44 76 L 30 76 L 30 42 L 22 42 Z" fill="none" stroke="url(#favGold)" stroke-width="4.5" stroke-linejoin="round" stroke-linecap="round" />
  <circle cx="50" cy="46" r="4" fill="#D4AF37" />
</svg>'''

with open(os.path.join(output_dir, "favicon.svg"), "w", encoding="utf-8") as f:
    f.write(favicon_svg)

# 3. Render PNGs using Pillow (512x512, 180x180, 32x32, favicon.ico)
size = 512
img = Image.new("RGBA", (size, size), (14, 46, 34, 255))
draw = ImageDraw.Draw(img)

# Outer metallic gold border
draw.rounded_rectangle([16, 16, size-16, size-16], radius=70, outline=(212, 175, 55, 255), width=12)

# House & architectural crest points
# (50% x, 18% y) -> (256, 100)
# (78% x, 42% y) -> (399, 215)
points = [
    (256, 110),
    (390, 225),
    (355, 225),
    (355, 380),
    (285, 380),
    (285, 290),
    (227, 290),
    (227, 380),
    (157, 380),
    (157, 225),
    (122, 225)
]
draw.polygon(points, outline=(212, 175, 55, 255), fill=(20, 61, 48, 255))
# Re-draw outline thicker
draw.line(points + [points[0]], fill=(212, 175, 55, 255), width=16, joint="curve")

# Center gold gem
draw.ellipse([240, 225, 272, 257], fill=(243, 231, 196, 255), outline=(212, 175, 55, 255), width=4)

# Letter 'G' monogram accent
try:
    font = ImageFont.truetype("arial.ttf", 60)
    draw.text((256, 430), "GRIHAKON", fill=(255, 255, 255, 255), font=font, anchor="mm")
except Exception:
    draw.text((220, 420), "GRIHAKON", fill=(255, 255, 255, 255))

# Save 512
img.save(os.path.join(output_dir, "logo-512.png"))

# Apple touch icon 180x180
img_180 = img.resize((180, 180), Image.Resampling.LANCZOS)
img_180.save(os.path.join(output_dir, "apple-touch-icon.png"))

# Favicon 32x32
img_32 = img.resize((32, 32), Image.Resampling.LANCZOS)
img_32.save(os.path.join(output_dir, "favicon-32x32.png"))

# Favicon .ico
img.save(os.path.join(output_dir, "favicon.ico"), format="ICO", sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])

print("Favicon suite and logos generated successfully!")
