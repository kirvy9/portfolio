import cv2
import numpy as np
from PIL import Image
import io

class OpenCVGameAutomation:
    def __init__(self, driver):
        self.driver = driver
        # 버튼 템플릿 이미지 로드
        self.templates = {
            'start_button': cv2.imread('templates/start_button.png'),
            'confirm_button': cv2.imread('templates/confirm_button.png'),
            'mission_button': cv2.imread('templates/mission_button.png')
        }
    
    def get_screenshot(self):
        """스크린샷을 OpenCV 형식으로 변환"""
        screenshot = self.driver.get_screenshot_as_png()
        img = Image.open(io.BytesIO(screenshot))
        return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    
    def find_template(self, template_name, threshold=0.8):
        """화면에서 템플릿 이미지 찾기"""
        screenshot = self.get_screenshot()
        template = self.templates[template_name]
        
        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        
        if max_val >= threshold:
            # 템플릿 크기
            h, w = template.shape[:2]
            # 클릭할 중앙 좌표 계산
            center_x = max_loc[0] + w // 2
            center_y = max_loc[1] + h // 2
            return (center_x, center_y)
        
        return None
    
    def click_button(self, template_name):
        """템플릿 이미지와 일치하는 버튼 찾아 클릭"""
        coords = self.find_template(template_name)
        if coords:
            self.driver.tap([coords])
            print(f"{template_name} 버튼 찾아서 클릭: {coords}")
            return True
        
        print(f"{template_name} 버튼을 찾을 수 없음")
        return False