from gtts import gTTS
import os
import time
import subprocess

def voice(teks):
    """
    Fungsi untuk mengubah teks menjadi suara dan memutarnya.
    
    Parameters:
    teks (str): Teks yang akan diubah menjadi suara.
    """
    print("Memproses Text-to-Speech dengan gTTS.")

    audio_file = "output.mp3"

    # Periksa jika pengguna ingin keluar
    if teks.lower() == "exit":
        print("Keluar dari program.")
        return

    # Hapus file audio sebelumnya jika ada
    if os.path.exists(audio_file):
        try:
            os.remove(audio_file)
        except Exception as e:
            print(f"Error menghapus file: {e}")

    # Proses teks menjadi suara
    try:
        tts = gTTS(text=teks, lang='id', slow=False)  # Ubah 'id' ke 'en' untuk bahasa Inggris, atau sesuai kebutuhan
        tts.save(audio_file)
    except Exception as e:
        print(f"Error saat memproses TTS: {e}")
        return

    # Putar audio menggunakan subprocess untuk menghindari MCI error
    try:
        subprocess.run(["ffplay", "-nodisp", "-autoexit", audio_file], check=True)
    except Exception as e:
        print(f"Error saat memutar audio: {e}")

    # Tunggu sebentar sebelum melanjutkan
    time.sleep(1)