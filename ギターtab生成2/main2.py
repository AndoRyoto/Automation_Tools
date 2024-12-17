import os
from PIL import Image
import cv2  # OpenCV for template matching
import numpy as np
import tkinter as tk

MARZIN = 100

def get_window_size():
    return 1920, 1080

def crop_size(image_path, screen_width, screen_height):
    TRIMMED_FOLDER = "base_images"
    # 入力画像を読み込む
    input_img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if input_img is None:
        print(f"画像を読み込めませんでした: {image_path}")
        return 0, 0, screen_width, screen_height
    
    best_match = None
    for template_name in os.listdir(TRIMMED_FOLDER):
        template_path = os.path.join(TRIMMED_FOLDER, template_name)
        template_img = cv2.imread(template_path, cv2.IMREAD_COLOR)
        
        # テンプレート画像のロードに失敗した場合はスキップ
        if template_img is None:
            print(f"テンプレート画像を読み込めませんでした: {template_path}")
            continue

        # テンプレートマッチングを実行
        result = cv2.matchTemplate(input_img, template_img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # 最も一致した位置とスコアを記録
        if best_match is None or max_val > best_match['score']:
            best_match = {
                'top_left': max_loc,
                'width': template_img.shape[1],
                'height': template_img.shape[0],
                'score': max_val
            }

    # 最適な一致が見つかった場合、その領域の座標を返す
    if best_match:
        top_left = best_match['top_left']
        width = best_match['width']
        height = best_match['height']
        # return top_left[0], top_left[1], top_left[0] + width, top_left[1] + height
        return 0, top_left[1] - MARZIN, screen_width, top_left[1] + height + MARZIN
    else:
        # 一致する部分が見つからない場合、全体をクロップする
        return 0, 0, screen_width, screen_height

def process_image(image_path, CROP_BOX):
    with Image.open(image_path) as img:
        cropped_img = img.crop(CROP_BOX)
        print(f"画像をトリミングしました: {os.path.basename(image_path)}")
        return cropped_img

def combine_images_to_pdf(cropped_images, output_pdf):
    if cropped_images:
        widths, heights = zip(*(img.size for img in cropped_images))
        max_width = max(widths)
        total_height = sum(heights)
        
        combined_image = Image.new("RGB", (max_width, total_height))
        print("新しい空の画像を作成しました")
        
        y_offset = 0
        for img in cropped_images:
            combined_image.paste(img, (0, y_offset))
            print(f"画像を結合中: y_offset={y_offset}")
            y_offset += img.height
        
        output_path = os.path.join(os.getcwd(), output_pdf)
        combined_image.save(output_path, "PDF")
        print(f"PDFファイルが作成されました: {output_path}")
    else:
        print("処理する画像が見つかりませんでした")

def main():
    INPUT_FOLDER = "input_images"
    OUTPUT_PDF = "output.pdf"

    screen_width, screen_height = get_window_size()

    cropped_images = []
    for filename in os.listdir(INPUT_FOLDER):
        if filename.lower().endswith(".png"):
            image_path = os.path.join(INPUT_FOLDER, filename)

            CROP_BOX = crop_size(image_path, screen_width, screen_height)
            print(f"crop_Box : {CROP_BOX}")
            cropped_img = process_image(image_path, CROP_BOX)
            cropped_images.append(cropped_img)

    combine_images_to_pdf(cropped_images, OUTPUT_PDF)

main()
