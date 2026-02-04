from PIL import Image
try:
    from progress_bar import progress, progressReset
    has_progress_bar = True
except:
    has_progress_bar = False
    
def encode(text: str, base_image: str = "image.jpg", encoded_image: str = "encoded.jpg"):
    print(f"Encoding '{text}'")
    bin_text = '{:032b}'.format(len(text)) + to_binary(text)
    im = Image.open(base_image).convert('RGB')
    out = Image.new('RGB', im.size)
    width, height = im.size
    assert(len(bin_text) <= width * height)
    for x in range(width):
        for y in range(height):
            r,g,b = im.getpixel((x,y))
            if len(bin_text) > 0:
                char = bin_text[0]
                bin_text = bin_text[1:]
                # Get the nearest even number
                new_r = r if r % 2 == 0 else r - 1
                # Make it even or odd for 0 or 1
                new_r = new_r if char == '0' else new_r + 1
                out.putpixel((x,y), (new_r, g, b))
            else:
                out.putpixel((x,y), (r, g, b))
        if has_progress_bar:
            progress(width, message="Encoding text")
    if has_progress_bar:
        progressReset()
        print()
    out.save(encoded_image, format="PNG")
    
def decode(encoded_image: str = "encoded.jpg") -> str:
    bin_text = ''
    im = Image.open(encoded_image).convert('RGB')
    width, height = im.size
    for x in range(width):
        for y in range(height):
            r,g,b = im.getpixel((x,y))
            bin_text += '0' if r % 2 == 0 else '1'
        if has_progress_bar:
            progress(width, message="Decoding image")
    if has_progress_bar:
        progressReset()
        print()
    length = int(bin_text[:32], 2)
    bin_text = bin_text[32:32 + length * 8]
    return from_binary(bin_text)

def to_binary(text: str) -> str:
    return ''.join('{:08b}'.format(ord(c)) for c in text)

def from_binary(text: str) -> str:
    return ''.join(chr(int(text[i:i+8], 2)) for i in range(0, len(text), 8))

if __name__ == "__main__":
    text = "This is a test message"
    encode(text=text, base_image="image.jpg", encoded_image="encoded.jpg")
    decoded = decode(encoded_image="encoded.jpg")
    print(f"Decoded: '{decoded}'")