import sys
import time

SUCCESS_MESSAGE = "Yeyyy, selesaii"
SUCCESS = "Thank youuu and see youuu:3"
EMPTY_MESSAGE = "\n=== Tidak ada lirik lagu yang ditemukan==="
CREDIT_MESSAGE = "// Code by @aadnanmt //\n"

def run_lyriczzz():

    lyriczzz = [
        ("Do you think I have forgotten?", 0.1),
        ("Do you think I have forgotten?", 0.1),
        ("Do you think I have forgotten", 0.1),
        ("about you?", 0.2),
        ("There was something bout you that now I cant remember", 0.08),
        ("Its the same damn thing that made my heart surrender", 0.1),
        ("And I miss you on a train, I miss you in the morning", 0.1),
        ("I never know what to think about", 0.1),
        ("I think about youuuuuu", 0.1)
    ]
    delays = [0.3, 5.0, 10.0, 15.0, 20.3, 25.0, 27.0, 30.2, 33.3]

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
