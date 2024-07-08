import pygame
import os
class SpiritAnimation:
    def __init__(self, spirit, animation_folder_path):
        self.spirit = spirit
        self.animation_folder_path = animation_folder_path
        self.animations = {}
        self.load_animations()

    def load_animations(self):
        """加载所有动画帧"""
        # 假设动画文件夹中包含每个动作的子文件夹，如 'walk', 'run', 'jump' 等
        for action in os.listdir(self.animation_folder_path):
            action_path = os.path.join(self.animation_folder_path, action)
            if os.path.isdir(action_path):
                print(action_path)
                frame_files = [f"{i}.bmp" for i in range(1, 36)]
                frames = [pygame.image.load(os.path.join(action_path, file)).convert_alpha() for file in frame_files]
                self.animations[action] = frames

    def play_animation(self, action_id, screen, position, frame_rate=24):
        """播放指定的动作动画"""
        if action_id not in self.animations:
            print(f"Animation {action_id} not found for spirit {self.spirit}.")
            return

        frames = self.animations[action_id]
        total_frames = len(frames)
        frame_duration_ms = 1000 // frame_rate

        current_frame = 0
        start_time = pygame.time.get_ticks()

        while True:
            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - start_time

            # 计算应该显示哪一帧
            current_frame = (elapsed_time // frame_duration_ms) % total_frames

            # 绘制当前帧
            frame = frames[current_frame]
            screen.blit(frame, position)

            # 检查是否需要退出循环
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            pygame.display.flip()
            pygame.time.delay(frame_duration_ms)

# 使用示例
if __name__ == "__main__":
    pygame.init()

    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Spirit Animation")

    # 假设动画文件夹路径存储在变量中
    animation_folder_path = '123'
    
    # 创建Spirit动画实例
    spirit = 1
    spirit_animation = SpiritAnimation(spirit, animation_folder_path)

    # 播放Spirit的'walk'动作
    spirit_animation.play_animation('walk', screen, (100, 100))

    pygame.quit()
