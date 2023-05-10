from PIL import Image
im = Image.open("wallstreet-580.webp").convert("RGB")
im.save("wallstreet.png", "png")
