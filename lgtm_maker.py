import os
from PIL import Image,ImageFont,ImageDraw

def main():
  # 画像のパスを input() にて取得し、ファイル名のみを取得
  image_path = input('Enter the absolute path or drag a file into the terminal:')
  image_path = image_path.replace("'", "").strip()
  image_file = os.path.basename(image_path)

  # path から画像を読み取る
  image = Image.open(image_file)

  # 画像のリサイズを行い、リサイズ後の width, height を表示
  resize_image = image.resize((512, int(512 * image.size[1] / image.size[0])))
  print("アスペクト比固定　width: {}, height: {}".format(resize_image.size[0], resize_image.size[1]))

  # フォントについてのパラメータを記載
  font_path    = '/System/Library/Fonts/SF-Pro-Display-Heavy.otf';
  font_size    = 120
  text         = 'LGTM'
  color        = 'white'
  stroke_color = 'black'
  stroke_width = 4

  # font を指定
  font = ImageFont.truetype(font_path, font_size)

  # text の width, height を取得
  text_bbox = font.getbbox(text)

  # テキストを配置する箇所を指定
  w, h = (resize_image.size[0] - text_bbox[2])/2, (resize_image.size[1] - text_bbox[3])/2

  # 文字を表示
  draw = ImageDraw.Draw(resize_image)
  draw.text(
    (w, h),
    text,
    font=font,
    fill=color,
    stroke_width=stroke_width,
    stroke_fill=stroke_color
  )

  # 結果を保存
  resize_image.save('result_' + image_file)

if __name__ == '__main__':
  main()


  main()