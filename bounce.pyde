xCoordinate = 50
yCoordinate = 20
speed = 10
ySpeed = 20
ellipseSize = 30

def setup():
    size(400, 400)
    
def draw():
    background(0)
    global xCoordinate, speed, ySpeed, ellipseSize, yCoordinate
    leftTopBoundary = ellipseSize / 2
    rightBottomBoundary = 400 - ellipseSize / 2    
    if xCoordinate >= rightBottomBoundary or xCoordinate <= leftTopBoundary:
        speed = -speed
    if yCoordinate >= rightBottomBoundary or yCoordinate <= leftTopBoundary:
        ySpeed = -ySpeed
    yCoordinate += ySpeed
    xCoordinate += speed
    fill(255, 25, 100)
    ellipse( xCoordinate, yCoordinate, ellipseSize, ellipseSize)
    
