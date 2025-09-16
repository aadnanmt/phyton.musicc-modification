import sys
import time

SUCCESS_MESSAGE = "Yeyyy, selesaii"
SUCCESS = "Thank youuu and see youuu:3"
EMPTY_MESSAGE = "\n=== Tidak ada lirik lagu yang ditemukan==="
CREDIT_MESSAGE = "// Code by @aadnanmt //\n"

def run_lyriczzz():

    lyriczzz = [
        ("Cause you could be the one that I love", 0.05),
        ("AAAA~ AAA~\n", 0.1),
        ("I could be the one that you dream", 0.05),
        ("AAAA~ AAA~", 0.09),
        ("\nA message in bottle is all i can do", 0.10),
        ("Standin' here hopin' it gets to you\n", 0.08),
        ("Cause you could be the one that I keep", 0.05),
        ("AAAA~ AAA~", 0.1),
        ("\nAnd I could be the reason you can't sleep", 0.04),
        ("AAAA~ AAA~", 0.1),
        ("\nA message in a bottle is all I can do\n", 0.10),
        ("Hopin' it gets TO YOUUUU", 0.08),
    ]
    delay = [0.4, 1.3, 0.3, 1.1, 0.7, 0.9, 0.5, 0.6, 0.6, 0.6, 0.6, 0.6]

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