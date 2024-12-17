import os
from PIL import Image
import tkinter as tk

# ウィンドウサイズを取得するための関数
def get_window_size():
    root = tk.Tk()
    root.update_idletasks()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.destroy()
    # return width, height
    # return 1920, 1200
    return 1920, 1080

def main():

    p = float(input('下何%を取得する？\n'))
    if not 0<=p<=100: exit(print('入力エラー\n'))

    # 入力フォルダと出力ファイルの指定
    INPUT_FOLDER = "input_images"
    OUTPUT_PDF = "output.pdf"
    print(f"入力フォルダ: {INPUT_FOLDER}")
    print(f"出力PDFファイル名: {OUTPUT_PDF}")

    # 一時的に保存するトリミング後の画像フォルダ
    TRIMMED_FOLDER = "trimmed_images"
    os.makedirs(TRIMMED_FOLDER, exist_ok=True)
    print(f"一時フォルダを作成: {TRIMMED_FOLDER}")

    # 画面サイズを取得
    screen_width, screen_height = get_window_size()
    print(f"画面サイズ: 幅={screen_width}, 高さ={screen_height}")

    # フォルダ内のすべてのPNGファイルを処理
    cropped_images = []
    for filename in os.listdir(INPUT_FOLDER):
        if filename.lower().endswith(".png"):
            image_path = os.path.join(INPUT_FOLDER, filename)
            print(f"画像ファイルを処理中: {image_path}")
            with Image.open(image_path) as img:
                # トリミング処理（画面全体の下半分）
                CROP_BOX = (0, (100 - p) * screen_height // 100, screen_width, screen_height)
                print(f"トリミングサイズ: {CROP_BOX}")
                cropped_img = img.crop(CROP_BOX)
                cropped_images.append(cropped_img)
                print(f"画像をトリミングしました: {filename}")

    # トリミング後の画像をPDFに結合して1ページのPDFを作成
    if cropped_images:
        print(f"トリミングされた画像の数: {len(cropped_images)}")
        widths, heights = zip(*(img.size for img in cropped_images))
        max_width = max(widths)
        total_height = sum(heights)
        print(f"結合画像の幅: {max_width}, 高さ: {total_height}")

        combined_image = Image.new("RGB", (max_width, total_height))
        print("新しい空の画像を作成しました")

        y_offset = 0
        for img in cropped_images:
            combined_image.paste(img, (0, y_offset))
            print(f"画像を結合中: y_offset={y_offset}")
            y_offset += img.height

        # 出力ファイルのパスを現在のディレクトリに保存
        output_path = os.path.join(os.getcwd(), OUTPUT_PDF)
        combined_image.save(output_path, "PDF")
        print(f"PDFファイルが作成されました: {output_path}")
    else:
        print("処理する画像が見つかりませんでした")

main()