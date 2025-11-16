import sys
import time

SUCCESS_MESSAGE = "Yeyyy, selesaii"
SUCCESS = "Thank youuu and see youuu:3"
EMPTY_MESSAGE = "\n=== Tidak ada lirik lagu yang ditemukan==="
CREDIT_MESSAGE = "// Code by @aadnanmt //\n"

def run_lyriczzz():

    lyriczzz = [
        ("\nDi mo ba ako lilisanin?", 0.13),
        ("Hindi pa ba sapat pagpapahirap sa 'kin?", 0.10),
        ("Hindi na ba ma-mamamayapa?", 0.12),
        ("Hindi na ba ma-mamamayapa?", 0.12),
        ("\nHindi na makalaya...", 0.13)
    ]
    delays = [0.3, 4.8, 9.5, 14.0, 17.3]

    print(CREDIT_MESSAGE)
    print("=== Message in The Bottle - Taylor Swift ===") 
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
