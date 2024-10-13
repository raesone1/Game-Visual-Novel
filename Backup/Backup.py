import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Visual Novel Sederhana")

#command Fullscreen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Fullscreen mode

# Font
font = pygame.font.Font("path/to/your/Mf Love Song.ttf", 36)  # Ganti dengan font Doki Doki yang sesuai

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
font = pygame.font.Font(None, 36)

# Memuat gambar latar belakang dan karakter
background = pygame.image.load("latar belakang.jpg")  # Ganti dengan nama file gambar latar belakangmu
character_eva = pygame.image.load("nahida.png")  # Ganti dengan nama file gambar karakter Eva
character_liam = pygame.image.load("nahida.png")  # Ganti dengan nama file gambar karakter Liam

# Memuat dan memutar soundtrack
pygame.mixer.music.load("background_music.mp3")  # Ganti dengan nama file musikmu
pygame.mixer.music.play(-1)  # Memutar musik secara loop (-1 berarti loop terus menerus)

# Fungsi untuk menampilkan teks
def draw_text(text, x, y):
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, (x, y))

# Fungsi utama
def main():
    clock = pygame.time.Clock()
    running = True
    scene = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Gambar latar belakang
        screen.blit(background, (0, 0))

        if scene == 0:
            # Menampilkan karakter di posisi yang ditentukan
            screen.blit(character_liam, (50, 300))  # Posisi karakter Liam di kiri
            screen.blit(character_eva, (500, 300))  # Posisi karakter Eva di kanan
            draw_text("Eva: Halo, Liam! Apa kabar hari ini?", 50, 100)
            draw_text("1. Aku baik-baik saja!", 50, 200)
            draw_text("2. Biasa saja.", 50, 250)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_1]:
                scene = 1
            elif keys[pygame.K_2]:
                scene = 2

        elif scene == 1:
            # Menampilkan karakter di posisi yang ditentukan
            screen.blit(character_liam, (50, 300))  # Posisi karakter Liam di kiri
            screen.blit(character_eva, (500, 300))  # Posisi karakter Eva di kanan
            draw_text("Liam: Aku senang mendengarnya!", 50, 100)
            draw_text("Tekan R untuk kembali.", 50, 200)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                scene = 0

        elif scene == 2:
            # Menampilkan karakter di posisi yang ditentukan
            screen.blit(character_liam, (50, 300))  # Posisi karakter Liam di kiri
            screen.blit(character_eva, (500, 300))  # Posisi karakter Eva di kanan
            draw_text("Liam: Oh, semoga harimu segera membaik.", 50, 100)
            draw_text("Tekan R untuk kembali.", 50, 200)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                scene = 0

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()