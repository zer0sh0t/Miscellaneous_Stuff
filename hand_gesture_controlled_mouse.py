'''
index finger - mouse pointer
hit index finger against the thumb - left click
hit middle finger against the thumb - right click
be careful with the program, it can get out of control pretty easily
in such a case, don't panic, press 'a' to abort the program
'''

import cv2
import keyboard
import pyautogui
import numpy as np
import mediapipe as mp

class HandDetector():
    def __init__(self, mode=False, max_hands=2, detection_con=0.5, track_con=0.5):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(mode, max_hands, detection_con, track_con)
        self.mp_draw = mp.solutions.drawing_utils

    def find_hands(self, img, draw=True):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)
        if self.results.multi_hand_landmarks and draw:
            for hand_lms in self.results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(img, hand_lms, self.mp_hands.HAND_CONNECTIONS)
        return img

    def find_position(self, img, hand_num=0, key_point_idx=8, win_coords=False):
        kplm = None
        wkplm = None
        if self.results.multi_hand_landmarks:
            hand = self.results.multi_hand_landmarks[hand_num]
            for i, lm in enumerate(hand.landmark):
                h, w, c = img.shape
                display_x, display_y = int(lm.x * w), int(lm.y * h)
                win_x, win_y = int(lm.x * 1920), int(lm.y * 1080) 

                if key_point_idx:
                    if i == key_point_idx:
                        if win_coords:
                            wkplm = (win_x, win_y)

                        kplm = np.array([display_x, display_y])
                        cv2.circle(img, (display_x, display_y), 10, (255, 0, 0), cv2.FILLED)
        if win_coords:
            return kplm, wkplm
        else:
            return kplm

def main(debug_mode=False):
    cap = cv2.VideoCapture(0)
    detector = HandDetector()
    while True:
        _, img = cap.read()
        img = cv2.flip(img, 1)
        img = detector.find_hands(img, draw=debug_mode)
        kplm0 = detector.find_position(img, key_point_idx=4)
        kplm1, wkplm1 = detector.find_position(img, key_point_idx=8, win_coords=True)
        kplm2 = detector.find_position(img, key_point_idx=12)

        try:
            left_click_val = np.round(np.linalg.norm(kplm1 - kplm0), 4)
            right_click_val = np.round(np.linalg.norm(kplm2 - kplm0), 4)
            pyautogui.moveTo(wkplm1[0], wkplm1[1], 0.001, pyautogui.easeInOutQuad)
            if left_click_val < 30:
                pyautogui.click(button='left')
            if right_click_val < 50:
                pyautogui.click(button='right')

            if debug_mode:
                print(left_click_val < 30, wkplm1, right_click_val < 50)
        except:
            pass

        if keyboard.is_pressed('a'):
            print('aborting...')
            break

        if debug_mode:
            cv2.imshow('window', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()