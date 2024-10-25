import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
screen_width = 1200
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Visual Novel Sederhana")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TRANSPARENT_BLACK = (0, 0, 0, 180)

# Font
font = pygame.font.Font(None, 50)
name_font = pygame.font.Font(None, 40)
time_font = pygame.font.Font(None, 30)

# Memuat gambar
background = pygame.image.load("background2.jpg")
character_happy = pygame.image.load("happy.png")
character_sad = pygame.image.load("happy.png")

# Menyesuaikan ukuran karakter
character_size = (500, 750)
character_happy = pygame.transform.scale(character_happy, character_size)
character_sad = pygame.transform.scale(character_sad, character_size)

# Memuat dan memutar soundtrack
pygame.mixer.music.load("abc.ogg")
pygame.mixer.music.play(-1)

# Fungsi untuk menampilkan teks dengan pembagian baris
def draw_text_multiline(text, x, y, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + word + ' '
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + ' '

    lines.append(current_line)

    for i, line in enumerate(lines):
        text_surface = font.render(line, True, WHITE)
        screen.blit(text_surface, (x, y + i * font.get_height()))

# Fungsi untuk menggambar dialog box
def draw_dialog_box():
    dialog_box = pygame.Rect(50, 600, screen_width - 100, 200)
    pygame.draw.rect(screen, TRANSPARENT_BLACK, dialog_box)
    pygame.draw.rect(screen, WHITE, dialog_box, 3)

# Fungsi untuk menggambar nama karakter dengan border
def draw_character_name(name):
    name_surface = name_font.render(name, True, WHITE)
    name_rect = name_surface.get_rect(center=(screen_width // 9, 570))
    border_rect = name_rect.inflate(110, 10)
    pygame.draw.rect(screen, TRANSPARENT_BLACK, border_rect)
    pygame.draw.rect(screen, WHITE, border_rect, 3)
    screen.blit(name_surface, name_rect)

# Fungsi untuk menggambar jam
def draw_time():
    current_time = "12:35"
    time_surface = time_font.render(current_time, True, WHITE)
    screen.blit(time_surface, (screen_width - 100, 100))

# Fungsi untuk menggambar pilihan
def draw_choices(choices):
    y_positions = [700, 740]
    for i, choice in enumerate(choices):
        draw_text_multiline(f"{i + 1}. {choice}", 500, y_positions[i], font, screen_width - 550)

# Fungsi untuk menampilkan menu keluar
def exit_menu():
    while True:
        screen.fill(BLACK)
        draw_text_multiline("Apakah Anda yakin ingin keluar?", screen_width // 4, screen_height // 3, font, screen_width // 2)
        draw_text_multiline("Tekan Y untuk Ya, T untuk Tidak", screen_width // 4, screen_height // 2, font, screen_width // 2)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_t:
                    return

# Fungsi utama
def main():
    clock = pygame.time.Clock()
    running = True
    dialog_index = 0
    choices = []
    waiting_for_choice = False

    # Dialog tentang menyatakan cinta
    dialogs = [
        ("Hai, Kenalin aku ''Rin''. Aku ini ciptaan ''radjaaaxp'' >~<!", character_happy, "Rin", ["Apa ini sudah rilis?"]),
        ("Ohh iya lupa untuk rincian game ini masih ditahap pengembangan yaa.", character_happy, "Rin", []),
        ("Aku janji kalo project ini SELESAI aku kasih tau yaa.", character_happy, "Rin", ["Baik kalo gitu aku tunggu!", "Kok lama banget rilisnya!."]),
        
        # Dialog jika memilih "Aku juga mencintaimu!"
        ("Oke ditunggu aja yaa buat pengembangannya. Stay tune!.", character_happy, "Rin", []),
        ("Nanti kalo udah selesai aku janji bakal kasih kamu nyoba ini game.", character_happy, "Rin", []),
        
    ]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_menu()
                continue

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit_menu()
                if event.key == pygame.K_SPACE and not waiting_for_choice:
                    if choices:
                        waiting_for_choice = True
                    else:
                        dialog_index += 1

                if event.key in [pygame.K_1, pygame.K_2] and choices:
                    choice_index = int(event.unicode) - 1
                    if 0 <= choice_index < len(choices):
                        if choice_index == 0:  # Jika memilih "Aku juga mencintaimu!"
                            dialog_index += 1  # Lanjut ke dialog bahagia
                        else:  # Jika memilih "Aku masih butuh waktu."
                            dialog_index = 5  # Lanjut ke dialog pemahaman
                        waiting_for_choice = False

        screen.blit(background, (0, 0))

        draw_dialog_box()

        if dialog_index < len(dialogs):
            character_name = dialogs[dialog_index][2]
            screen.blit(dialogs[dialog_index][1], (50, 150))
            draw_text_multiline(dialogs[dialog_index][0], 500, 630, font, screen_width - 550)
            draw_character_name(character_name)
            
            choices = dialogs[dialog_index][3]
            if choices:
                draw_choices(choices)
        else:
            draw_text_multiline("Terima kasih telah mencobanya, Di tunggu yaa sampe rilis. Kalo gitu aku izin pamit yaa >~<!", 70, 630, font, screen_width - 140)

        draw_time()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
