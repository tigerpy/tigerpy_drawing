# tigerpy_drawing
Python Drawing Library

This is a Python library, which will enable clients to perform 2D drawing and then export it to SVG.

## Client Usage
```python
# client.py
from tigerpy_drawing import DrawingCanvas, Pen

redThinPen = Pen(1, (255, 0, 0))
blueThickPen = Pen(3, (0, 0, 255))

canvas = DrawingCanvas(300, 300)

canvas.SetPen(redThinPen)
canvas.DrawLine(0, 0, 100, 100)

canvas.SetPen(blueThickPen)
canvas.DrawLine(100, 0, 0, 100)

rectPen = Pen(2, (128, 255, 128), (255, 255, 0))
canvas.SetPen(rectPen)
canvas.DrawRectangle(30, 30, 40, 40)

canvas.SetPen(redThinPen)
canvas.DrawCircle(50, 50, 30)

canvas.SetPen(redThinPen)
canvas.DrawEllipse(60, 70, 20, 10)

canvas.DrawPolyline([[0, 0], [5, 10], [10, 20], [20, 5], [30, 40]])

purpleStrokeGreenFillPen = Pen(1, (163, 73, 164), (34, 177, 76))
canvas.SetPen(purpleStrokeGreenFillPen)
canvas.DrawPolygon([[220, 10], [300, 210], [170, 250], [123, 234]])

canvas.SetPen(redThinPen)
canvas.DrawText(50, 200, "Hello World!")

canvas.ExportSVG("temp.svg")
```

Run:
```
> python client.py
```

Output (screenshot of SVG file opened in Inkscape):
![temp](temp.png)

## TODOs
* Change font
* Transforms (translation, rotation, scaling)
* Bezier curves
* Export to other image formats: BMP, PNG, JPEG etc
* Draw arrows
* Draw N-gons (like hexagon, octagon etc)



