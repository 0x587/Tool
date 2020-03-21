from PIL import Image, ImageFont

from handright import Template, handwrite

text = """
    You want to write.
"""

template = Template(
    background=Image.open(r'./background.jpg'),
    font_size=90,
    font=ImageFont.truetype(r"./hand.ttf"),
    line_spacing_sigma=2,
    word_spacing=4,
    left_margin=215,
    right_margin=200,
    top_margin=360,
    bottom_margin=260,
    line_spacing=135,
    perturb_x_sigma=4,
    perturb_y_sigma=4,
)
images = handwrite(text, template)
for i, im in enumerate(images):
    assert isinstance(im, Image.Image)
    im.show()
    im.save(r"./IMG{}.jpeg".format(i))
