import logging
import colorgram

logging.basicConfig(level = logging.DEBUG)



def main():
    """
    gets the top 13 colors from an image
    :return: list of tuple of rgb colors
    """
    colors = colorgram.extract('hirst-image.jpeg', 5)

    color_list =[]

    print('colors = \\\n[')
    for color in colors:
        print(f"    {{\n        'red':' {color.rgb.r}")
        print(f"        'green': {color.rgb.g}")
        print(f"        'blue': {color.rgb.b}")
        print(f"        'tuple': ({color.rgb.r}, {color.rgb.g}, {color.rgb.b})")
        print(f"        'proportion': {color.proportion * 100:0.2f}%\n    }}")

        color_list += (color.rgb.r, color.rgb.g, color.rgb.b),

    print(f"]\ntuple_list = {color_list}")

if __name__ == '__main__':
    main()

# logging.debug(stuff)
