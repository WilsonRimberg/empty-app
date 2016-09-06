from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset
# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, .30)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(1, black)
# A graphics asset that represents a rectangle
rectangle = RectangleAsset(50, 20, thinline, blue)
Sprite(rectangle)
Sprite(rectangle, (20,10))
# Now display a rectangle
ellipse = EllipseAsset(30, 20, thinline, blue)
Sprite(ellipse, (50,50))
polygon = PolygonAsset([(0,0),(150,0),(160,140), (60,180),(0,0)], thinline, red)
Sprite(polygon)
myapp = App()
myapp.run()
