import colorgram

extracted_colors = colorgram.extract("hirst_painting\image.jpg", 25)

colors = []

i = 0
for color in extracted_colors:
    new_color = extracted_colors[i].rgb
    new_color_string = str(f"({new_color.r}, {new_color.g}, {new_color.b})")
    colors.append(new_color_string)
    i += 1
