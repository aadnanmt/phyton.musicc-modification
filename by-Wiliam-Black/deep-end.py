import sys
import time

SUCCESS_MESSAGE = "\n=== Yeyyy, Lirik Lagu Selesai ==="
EMPTY_MESSAGE = "\n=== Tidak ada lirik lagu yang ditemukan==="
CREDIT_MESSAGE = "Code by @aadnanmt | Inspired by @micolarighi\n"

def run_lyriczzz():

    lyriczzz = [
        ("I've been lost in my head", 0.08),
        ("Over something I said", 0.08),
        ("All these feelings got me down", 0.07),
        ("In the deep end", 0.09),
        ("Trying not to pretend", 0.08),
        ("I'm not losing it again", 0.07),
        ("When nothing's even wrong", 0.07),
        ("There's no reason", 0.06),
    ]
    delay = [0.4, 0.5, 0.4, 0.9, 0.4, 0.5, 0.4, 1.2]

    print(CREDIT_MESSAGE)
    print("=== Deep End - Wiliam Black ===") 
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
            print(SUCCESS_MESSAGE)
        else:
            print(EMPTY_MESSAGE)
        
    except KeyboardInterrupt:
        print(f"\n== Program dihentikan oleh pengguna ==")
        return
    except Exception as e:
        print(f"\n== Terjadi kesalahan: {e} ==")
        return

run_lyriczzz()
