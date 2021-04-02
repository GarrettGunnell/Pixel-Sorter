RANDOM_INTERVAL = 1
MIN_RANGE = 10
MAX_RANGE = 15

VERTICAL_SORT = 1

#low to high or high to low
INVERSE_SORT = 0

MASK = 0

# Condition for swapping
# 0 for red
# 1 for green
# 2 for blue
# 3 for brightness
CONDITION = 0

def setup():
    global photo
    global mask
    photo = loadImage("Assets/Ocean.png")
    if MASK:
        mask = loadImage("Assets/OceanMask.png")
        mask.loadPixels()
    size(1049, 720)
    frameRate(60)
    photo.loadPixels()
    sortPhoto()
    photo.updatePixels()
    
def draw():
    image(photo, 0, 0)
        
def sortPhoto():
    if RANDOM_INTERVAL:
        if VERTICAL_SORT:
            for x in range(photo.width):
                y = 0
                while y < photo.height:
                    segment = floor(random(MIN_RANGE, MAX_RANGE))
                    start = x + y * photo.width
                    stop = x + (y + segment) * photo.width
                    bubblesort(start, stop)
                    y += segment
        else:
            for y in range(photo.height):
                x = 0
                while x < photo.width:
                    segment = floor(random(MIN_RANGE, MAX_RANGE))
                    loc = x + y * photo.width
                    bubblesort(loc, loc + segment)
                    x += segment
    else:
        for i in range(photo.width if VERTICAL_SORT else photo.height):
            for j in range(photo.height - 1 if VERTICAL_SORT else photo.width - 1):
                for k in range(photo.height - 1 if VERTICAL_SORT else photo.width - x - 1):
                    loc = k + j * photo.width
                    loc2 = k + (j + 1) * photo.width if VERTICAL_SORT else (k + 1) + j * photo.width
                    if (swap_condition(photo.pixels[loc]) > swap_condition(photo.pixels[loc2])):
                            photo.pixels[loc], photo.pixels[loc2] = photo.pixels[loc2], photo.pixels[loc]
                            
def bubblesort(start, stop):
    for i in range(start, stop, photo.width if VERTICAL_SORT else 1):
        for j in range(start, stop, photo.width if VERTICAL_SORT else 1):
            loc = j
            loc2 = j + photo.width if VERTICAL_SORT else j + 1
            
            if loc >= len(photo.pixels) or loc2 >= len(photo.pixels): break
            if MASK:
                if alpha(mask.pixels[loc]) or alpha(mask.pixels[loc2]): continue
            
            if INVERSE_SORT:
                if (swap_condition(photo.pixels[loc]) < swap_condition(photo.pixels[loc2])):
                    photo.pixels[loc], photo.pixels[loc2] = photo.pixels[loc2], photo.pixels[loc]
            else:
                if (swap_condition(photo.pixels[loc]) > swap_condition(photo.pixels[loc2])):
                    photo.pixels[loc], photo.pixels[loc2] = photo.pixels[loc2], photo.pixels[loc]
                        
def swap_condition(pixel):
    if   CONDITION == 0: return red(pixel)
    elif CONDITION == 1: return green(pixel)
    elif CONDITION == 2: return blue(pixel)
    elif CONDITION == 3: return brightness(pixel)
    else:
        print("Broooo you forgot the swap condition")
        exit()

def keyPressed():
    if key == ' ':
        name = 'Captures/' + str(floor(random(10000))) + '.png'
        save(name)

    
