import sys
import time

SUCCESS_MESSAGE = "Yeyyy, selesaii"
SUCCESS = "Thank youuu and see youuu:3"
EMPTY_MESSAGE = "\n=== Tidak ada lirik lagu yang ditemukan==="
CREDIT_MESSAGE = "// Code by @aadnanmt //\n"

def run_lyriczzz():

    lyriczzz = [
        ("\n""Soul try to figure it out", 0.10),
        ("From where I've been escapin", 0.10),
        ("Running to end all the sin", 0.11),
        ("Get away from the pressure", 0.10),
        ("\n""Wondering to get a love that is so pure", 0.14),
        ("Gotta have to always make sure", 0.10),
        ("That I'm not just somebody's pleasure", 0.10)
    ]
    delays = [0.3, 4.6, 9.0, 13.4, 16.4, 25.5, 29.3]

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
