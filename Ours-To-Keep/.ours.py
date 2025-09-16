import sys
import time
 
SUCCESS_MESSAGE = "Yeyyy, selesaiii"
SUCCESS = "Thank youuu and see youuu:3"
EMPTY_MESSAGE = "\n=== Tidak ada lirik lagu yang ditemukan==="
CREDIT_MESSAGE = "// Code by aadnanmt //\n"

def run_lyriczzz():

    lyriczzz = [
        ("Do you ever feel the need", 0.12),
        ("to get away from me?", 0.10),
        ("Do I bore you?", 0.13),
        ("OR", 0.03), 
        ("do you want to", 0.05),
        ("Take me", 0.16),
        ("from this crowded place to", 0.13),
        ("Somewhere we can find some peace?", 0.08),
        ("And the world", 0.05),
        ("is", 0.05),
        ("OURS", 0.02),
        ("TO", 0.05),
        ("KEEP~", 0.09),
    ]
    delay = [0.6, 0.3, 0.6, 0.5, 0.3, 0.3, 0.5, 0.6, 0.7, 0.2, 0.3, 0.2, 0.4]

    print(CREDIT_MESSAGE)
    print("=== Ours to keep - Kendis Adis ===") 
    print()
    try:
        for i, (baris_lagu, delay_karakter) in enumerate(lyriczzz):
            for karakter in baris_lagu:
                print(karakter, end='')
                sys.stdout.flush()
                time.sleep(delay_karakter)
            time.sleep(delay[i])
            print('')
            
        if len(lyriczzz) > 0:
            print('')
            print('')
            print('')
            print(SUCCESS_MESSAGE)
            print(SUCCESS)
        else:
            print(EMPTY_MESSAGE)
        
    except KeyboardInterrupt:
        print(f"\n== Program dihentikan oleh pengguna ==")
        return
    except Exception as e:
        print(f"\n== Terjadi kesalahan: {e} ==")
        return

run_lyriczzz()
