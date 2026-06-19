import os
import random
import time
from PIL import Image
from tkinter import Tk, filedialog

# UI Colors
C = '\033[96m' # Cyan
M = '\033[95m' # Magenta
Y = '\033[93m' # Yellow
G = '\033[92m' # Green
W = '\033[0m'  # Reset
BOLD = '\033[1m'

# --- THE MASTERPIECE ASCII ---
MONA_LISA = r"""
                     ._,ad88888888bba,_
                  ,ad8888I8888888888888bba,
                ,8888888I888888888888888888a,
              ,d8888888Izzzzzzzzz,;,;ZZZY8888888b,
             d88888PP''  ''YY888888888888888888b,
           ,d88''__,-----------,,,,;;ZZZY8888888888b,
           ,8III''              ;;1"ZZZIII888888888,
          ,I881;'               ;1ZZZZZ88bIII888888,
         ,II88Z1;,              ;llZZZZZ888888I8888,
        ,II888Z1;,             ,;;;;;1llZZZ88888I888b
       ,II8888Z;;             `;;;;;''11ZZ888888I8888,
       II88888Z;'              ;IZZZZZ88888I888b
       II88888IZZZZZZZZZ,  .aaaaa,__,1;1llZZZ888888I888
       II88888IZZ'<(@>|Z] |ZZZ<'<@>ZZZZ;;1llZZ88888I88I
      ,II88888;''''... ;| |ZZ;''''...  ;;1lZ888888I888
      II8888881        `; ;;           .;1lZZ888888I888,
     ,II888888Z;         ;;            .;llZZZ8888888I88I
     III888888Z1;    _.,  ;;          ,;;1llZZZ888888I888
     II8888888Z;;;---(  _  )        ,;;;llZZZZ888888I888,
     II88888888Z1;;;;;`---'Z;.     ,;;;;llZZZZZ888888I888b
    ]I888888888Z;;;;'    ";111111,;;;;;ll11ZZZZ888888I8I88,
    II88888888Z1..;"Y88bd888P";;;,;;1llZZZZZZ888888I888I
    II888888888Z1;,  `"PPP";;;,;;;ll11ZZZZZW8888888I8888
    II8888888888Z1;;.  `;;;1;;;;;1llZZZZZZZW8888888I8888
   `II888888888888Z1;.    ,;;;11lZZZZZZWMZ8888888I88888
    II88888888888888Zbaa11lZZZZZZZZWMWZZZ8888888I88888,
    `II88888888888888b"WMZZZZWMWMZZZZI88888888I88888b
     `II88888888888888;ZZMMMMZZZZZZZ11I88888888I88888,
       `II8888888888888;`1ZZZZZZZZZ1111llI88888888888,
        II8888888888888, `;111ZZZ111111;;.Y8888888I888b
"""

TITLE = r"""
██████╗ ██╗██╗  ██╗██╗███████╗    ████████╗██████╗ ██╗██╗  ██╗██╗███████╗
██╔══██╗██║╚██╗██╔╝██║██╔════╝    ╚══██╔══╝██╔══██╗██║╚██╗██╔╝██║██╔════╝
██████╔╝██║ ╚███╔╝ ██║█████╗         ██║   ██████╔╝██║ ╚███╔╝ ██║█████╗  
██╔═══╝ ██║ d█╔██╗ ██║██╔══╝         ██║   ██╔══██╗██║ d█╔██╗ ██║██╔══╝  
██║     ██║██╔╝ ██╗██║███████╗       ██║   ██║  ██║██║██╔╝ ██╗██║███████╗
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝       ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝╚══════╝
"""

def center_print(text_block, color=W):
    try:
        width = os.get_terminal_size().columns
    except:
        width = 100
    lines = text_block.split('\n')
    for line in lines:
        pad = (width - len(line)) // 2
        print(f"{' ' * max(0, pad)}{color}{line}{W}")

def show_display():
    os.system('cls' if os.name == 'nt' else 'clear')
    center_print(MONA_LISA, C)
    center_print(TITLE, M)
    
    try:
        width = os.get_terminal_size().columns
    except:
        width = 100
        
    sep = "=" * 60
    print(f"{Y}{sep.center(width)}{W}")
    cred = "v1.0 | Developed by Mohammed Shezil"
    print(f"{G}{BOLD}{cred.center(width)}{W}")
    print(f"{Y}{sep.center(width)}{W}\n")

def get_image_path():
    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    file_path = filedialog.askopenfilename(
        title="🧚 Select Image Matrix File",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
    )
    root.destroy()
    return file_path

def pixel_scramble(img_path, key, mode='encrypt'):
    try:
        img = Image.open(img_path).convert("RGB")
        pixels = img.load()
        width, height = img.size
        
        coords = [(x, y) for x in range(width) for y in range(height)]
        
        random.seed(key)
        shuffled_coords = coords.copy()
        random.shuffle(shuffled_coords)
        
        new_img = Image.new("RGB", (width, height))
        new_pixels = new_img.load()
        
        xor_mask = key % 255
        
        print(f"\n[*] Executing structural alterations... Please wait.")
        
        if mode == 'encrypt':
            for idx, (orig_x, orig_y) in enumerate(coords):
                r, g, b = pixels[orig_x, orig_y]
                new_x, new_y = shuffled_coords[idx]
                new_pixels[new_x, new_y] = (r ^ xor_mask, g ^ xor_mask, b ^ xor_mask)
        else:
            for idx, (orig_x, orig_y) in enumerate(coords):
                scrambled_x, scrambled_y = shuffled_coords[idx]
                r, g, b = pixels[scrambled_x, scrambled_y]
                new_pixels[orig_x, orig_y] = (r ^ xor_mask, g ^ xor_mask, b ^ xor_mask)
                
        dirname, filename = os.path.split(img_path)
        base_name, ext = os.path.splitext(filename)
        out_name = f"{mode}ed_{base_name}.png" 
        out_path = os.path.join(dirname, out_name)
        
        new_img.save(out_path, "PNG")
        print(f"\n{G}[✔] Success! Output stored beautifully as: {out_name}{W}")
        
    except Exception as e:
        print(f"\n{os.sys.argv[0]}: [!] Execution failed: {e}")

def main():
    os.system('') 
    
    while True:
        show_display()
        print(" [1] Secure Cipher-Lock Image (Encrypt)")
        print(" [2] Reverse Matrix Scramble (Decrypt)")
        print(" [3] Break Out Vector (Exit)")
        
        choice = input("\nSelect vector path (1-3): ").strip()
        
        if choice in ['1', '2']:
            print("\n[*] Triggering system explorer file-dialog window...")
            img_path = get_image_path()
            
            if not img_path:
                print(f"{Y}[!] Process aborted: No target image selected.{W}")
                time.sleep(2)
                continue
                
            try:
                key = int(input("Provide private symmetric numerical key: "))
                mode = 'encrypt' if choice == '1' else 'decrypt'
                pixel_scramble(img_path, key, mode)
            except ValueError:
                print(f"\n{W}[!] Operational error: Private key must be a numerical integer.{W}")
                
        elif choice == '3':
            print(f"\n{M}Shutting down systems safely. Task 02 Complete.{W}")
            break
        else:
            print(f"\n{Y}[!] Input out of bounds. Select 1, 2, or 3.{W}")
            
        input(f"\n{C}Press Enter to loop back context panel...{W}")

if __name__ == "__main__":
    main()
