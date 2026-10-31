import os
import urllib.request
from PIL import Image

output_dir = r"C:\Users\dasan\.gemini\antigravity\scratch\grihakon-interiors-kolkata\assets\images"
os.makedirs(output_dir, exist_ok=True)

images = [
    ("hero-fallback.jpg", "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=1600&q=80"),
    ("living-room-luxury.jpg", "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=80"),
    ("modular-kitchen-island.jpg", "https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&w=1200&q=80"),
    ("master-bedroom-suite.jpg", "https://images.unsplash.com/photo-1616594039964-ae9021a400a0?auto=format&fit=crop&w=1200&q=80"),
    ("dining-cove-lighting.jpg", "https://images.unsplash.com/photo-1617806118233-18e1de247200?auto=format&fit=crop&w=1200&q=80"),
    ("walkin-wardrobe-closet.jpg", "https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?auto=format&fit=crop&w=1200&q=80"),
    ("false-ceiling-lighting.jpg", "https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?auto=format&fit=crop&w=1200&q=80"),
    ("renovation-civil-work.jpg", "https://images.unsplash.com/photo-1581094794329-c8112a89af12?auto=format&fit=crop&w=1200&q=80"),
    ("commercial-office-interior.jpg", "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1200&q=80"),
    ("architectural-blueprint-3d.jpg", "https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=1200&q=80"),
]

for filename, url in images:
    filepath = os.path.join(output_dir, filename)
    print(f"Downloading {filename}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=20) as response, open(filepath, 'wb') as out_file:
            out_file.write(response.read())
        
        # Optimize with Pillow
        with Image.open(filepath) as img:
            img = img.convert('RGB')
            # Resize if exceptionally large
            if img.width > 1600:
                h = int(img.height * (1600 / img.width))
                img = img.resize((1600, h), Image.Resampling.LANCZOS)
            img.save(filepath, "JPEG", quality=85, optimize=True)
            print(f"Optimized {filename} ({img.width}x{img.height})")
    except Exception as e:
        print(f"Error processing {filename}: {e}")

print("Image download and optimization complete!")
