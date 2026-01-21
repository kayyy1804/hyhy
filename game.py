import random

def main():
    print("=" * 50)
    print("🎮 SELAMAT DATANG DI GAME TEBAK ANGKA 🎮")
    print("=" * 50)
    print()
    
    # Mengatur kesulitan game
    while True:
        print("Pilih level kesulitan:")
        print("1. Mudah (1-50)")
        print("2. Sedang (1-100)")
        print("3. Sulit (1-500)")
        
        level = input("\nMasukkan pilihan (1-3): ").strip()
        
        if level == "1":
            max_num = 50
            max_attempts = 10
            print("✅ Anda memilih level MUDAH")
            break
        elif level == "2":
            max_num = 100
            max_attempts = 7
            print("✅ Anda memilih level SEDANG")
            break
        elif level == "3":
            max_num = 500
            max_attempts = 5
            print("✅ Anda memilih level SULIT")
            break
        else:
            print("❌ Pilihan tidak valid! Silakan coba lagi.\n")
            continue
    
    print(f"📍 Saya sudah menebak angka antara 1 dan {max_num}")
    print(f"⏰ Anda punya {max_attempts} kesempatan untuk menebak\n")
    
    # Generate angka random
    secret_number = random.randint(1, max_num)
    attempts = 0
    guessed = False
    
    # Loop game
    while attempts < max_attempts and not guessed:
        try:
            guess = int(input(f"Tebakan ke-{attempts + 1}: "))
            
            # Validasi input
            if guess < 1 or guess > max_num:
                print(f"⚠️  Silakan masukkan angka antara 1 dan {max_num}!\n")
                continue
            
            attempts += 1
            remaining = max_attempts - attempts
            
            if guess == secret_number:
                print()
                print("🎉" * 25)
                print(f"🎉 SELAMAT! Anda berhasil menebak angka: {secret_number}")
                print(f"🎉 Anda membutuhkan {attempts} percobaan")
                print("🎉" * 25)
                guessed = True
            elif guess < secret_number:
                print(f"📈 Angka terlalu KECIL! Sisa kesempatan: {remaining}\n")
            else:
                print(f"📉 Angka terlalu BESAR! Sisa kesempatan: {remaining}\n")
        
        except ValueError:
            print("❌ Input tidak valid! Silakan masukkan angka.\n")
            continue
    
    # Jika tidak berhasil menebak
    if not guessed:
        print()
        print("=" * 50)
        print(f"😢 GAME OVER! Angka yang benar adalah: {secret_number}")
        print(f"💔 Anda tidak berhasil dalam {max_attempts} kesempatan")
        print("=" * 50)
    
    # Tanya ulang
    print()
    while True:
        play_again = input("Apakah Anda ingin bermain lagi? (y/n): ").strip().lower()
        if play_again == "y":
            print("\n" * 2)
            main()
            break
        elif play_again == "n":
            print("\n👋 Terima kasih telah bermain! Sampai jumpa lagi!")
            break
        else:
            print("❌ Masukkan 'y' atau 'n'!\n")

if __name__ == "__main__":
    main()
