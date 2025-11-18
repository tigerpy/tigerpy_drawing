# client.py
from tigerpy_drawing import DrawingCanvas, Pen

redThinPen = Pen(1, (255, 0, 0))
blueThickPen = Pen(3, (0, 0, 255))

canvas = DrawingCanvas(100, 100)

canvas.SetPen(redThinPen)
canvas.DrawLine(0, 0, 100, 100)

canvas.SetPen(blueThickPen)
canvas.DrawLine(100, 0, 0, 100)

rectPen = Pen(2, (128, 255, 128), (255, 255, 0))
canvas.SetPen(rectPen)
canvas.DrawRectangle(30, 30, 40, 40)

canvas.ExportSVG("temp.svg")


