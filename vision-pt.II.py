import sys
import time

SUCCESS_MESSAGE = "\n=== Yeyyy, Lirik Lagu Selesai ==="
EMPTY_MESSAGE = "\n=== Tidak ada lirik lagu yang ditemukan ==="
CREDIT_MESSAGE = "// Code by @aadnanmt //\n"

def run_lyriczzz():
    lyriczzz = [
        ("Silver, once golden", 0.10),
        ("There's only so much holding on", 0.07),
        ("You can't take when your mind's at stake", 0.08), 
        ("But I'll wait", 0.1),
        ("Do what you gotta do, what you gotta do to be you again", 0.09),
        ("Do what you gotta do, what you gotta do to put your heart to rest", 0.08),
        ("I'll keep waiting as long as it takes", 0.10),
        ("Do what you gotta do, what you gotta do to be you, you, you again", 0.10),
    ]
    
    delay = [0.5, 0.6, 0.6, 1.1, 0.5, 0.6, 1.5, 1.8]

    print(CREDIT_MESSAGE)
    print("=== Deep End - William Black ===")
    print()
    try:
        if len(lyriczzz) != len(delay):
            print("\n== Peringatan: Jumlah baris lirik dan nilai delay tidak sama! ==")
            return

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