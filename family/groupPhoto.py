from PIL import Image, ImageDraw, ImageFont
import pandas as pd
from pypinyin import lazy_pinyin


def capture():
    source_data = "../data/comments-test.csv"
    source_picture = "../data/black_magic_girl2.jpeg"
    source_font = "../data/alipuhui.ttf"
    target_picture = "../result/black_magic_girl2_result_v20.jpeg"
    channel = "RGB"
    sample_char = "哈"
    fill_color = "lightgray"
    child_w = 20
    child_h = 20

    all_fans = pd.read_csv(source_data, sep="\t")
    lottery_pool = set()
    for index, row in all_fans.iterrows():
        lottery_pool.add(row['name'])
    list_character = list(lottery_pool)
    list_character.sort(key=lambda char: lazy_pinyin(char)[0][0])
    character = "\t".join(list_character)
    font = ImageFont.truetype(source_font, child_h)
    girl = Image.open(source_picture)
    w, h = girl.size
    image_child = Image.new(channel, (child_w, child_h))
    image_target = Image.new(channel, (child_w * w, child_h * h))
    text_w, text_h = font.getsize(sample_char)
    offset_x = (child_w - text_w) >> 1
    offset_y = (child_h - text_h) >> 1
    char_index = 0
    draw = ImageDraw.Draw(image_child)
    for y in range(h):
        for x in range(w):
            print("进度：", str(y+x/w/1.0), "/", h)
            draw.rectangle((0, 0, child_w, child_h), fill=fill_color)
            draw.text((offset_x, offset_y), character[char_index], font=font, fill=girl.getpixel((x, y)))
            image_target.paste(image_child, (x*child_w, y*child_h))
            char_index = (char_index + 1) % len(character)
    image_target.save(target_picture)


if __name__ == '__main__':
    capture()
