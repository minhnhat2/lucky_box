import pygame
import random

# Khởi tạo pygame
pygame.init()

# Đặt kích thước màn hình
size = (800, 600)
screen = pygame.display.set_mode(size)

# Đặt tiêu đề của cửa sổ
pygame.display.set_caption("Box Game")

# Tải hình ảnh hộp
closed_box_image = pygame.image.load("box_1.png").convert()
opened_box_image = pygame.image.load("box_2.png").convert()

# Tải hình nền
background_image = pygame.image.load("background_1.png").convert()

# Tải hiệu ứng âm thanh
box_open_sound = pygame.mixer.Sound("music.ogg")

# Tạo một danh sách các từ
words = ["Chúc bạn may mắn lần sau", "Chúc bạn may mắn lần sau", "50k", "100k", "20k", "Chúc bạn may mắn lần sau"]

# Tạo danh sách hộp 2D
boxes = [[(0, 0) for _ in range(2)] for _ in range(3)]

# Điền vào các hộp với các từ ngẫu nhiên
for row in range(3):
    for col in range(2):
        boxes[row][col] = (random.choice(words), False)

# Đặt phông chữ và cỡ chữ
font = pygame.font.Font(None, 36)

# Vòng lặp trò chơi chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Kiểm tra xem người chơi có nhấp vào nút chuột không
    if pygame.mouse.get_pressed()[0]:
        # Nhận vị trí chuột
        mouse_pos = pygame.mouse.get_pos()

        # Tính hàng và cột của hộp đã được nhấp
        row = mouse_pos[1] // 200
        col = mouse_pos[0] // 400

        # Kiểm tra xem hộp có được mở không
        if not boxes[row][col][1]:
            # Set the box as opened
            boxes[row][col] = (boxes[row][col][0], True)
            box_open_sound.play()

    # Vẽ nền trên màn hình
    screen.blit(background_image, (0, 0))
    # Vẽ các hộp trên màn hình
    for row in range(3):
        for col in range(2):
            if boxes[row][col][1]:
                screen.blit(opened_box_image, (col * 400, row * 200))
                text = font.render(boxes[row][col][0], True, (255, 255, 255))
                text_rect = text.get_rect(center=(col*400+200,row*200+100))
                screen.blit(text, text_rect)
            else:
                screen.blit(closed_box_image, (col * 400, row * 200))

    pygame.display.flip()

# Thoát game
pygame.quit()
