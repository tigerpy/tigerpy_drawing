# tigerpy_drawing.py
import sys
from abc import ABC, abstractmethod
import copy

if __name__ == "__main___":
    print("This module is not meant to be executed directly.")
    sys.exit(1) 

class Pen:
    def __init__(self, strokeSize = 1, strokeColor = (0, 0, 0), fillColor = None):
        self.mStrokeSize = strokeSize
        self.mStrokeColor = strokeColor
        self.mFillColor = fillColor

    def SetStrokeSize(self, strokeSize):
        self.mStrokeSize = strokeSize

    def SetStrokeColor(self, strokeColor):
        self.mStrokeColor = strokeColor

    def SetFillColor(self, fillColor):
        self.mFillColor = fillColor

    def GetStrokeSize(self):
        return self.mStrokeSize
    
    def GetStrokeColor(self):
        return self.mStrokeColor
    
    def GetFillColor(self):
        return self.mFillColor

class DrawingVisitor(ABC):
    @abstractmethod
    def DrawLine(self, pen, x1, y1, x2, y2):
        pass

    @abstractmethod
    def DrawRectangle(self, pen, x, y, width, height):
        pass

class Drawing:
    @abstractmethod
    def Accept(self, visitor):
        pass

class LineDrawing(Drawing):
    def __init__(self, pen, x1, y1, x2, y2):
        self.mPen = copy.copy(pen)
        self.mX1 = x1
        self.mY1 = y1
        self.mX2 = x2
        self.mY2 = y2

    def Accept(self, visitor):
        visitor.DrawLine(self.mPen, self.mX1, self.mY1, self.mX2, self.mY2)

class RectangleDrawing(Drawing):
    def __init__(self, pen, x, y, width, height):
        self.mPen = copy.copy(pen)
        self.mX = x 
        self.mY = y
        self.mWidth = width
        self.mHeight = height

    def Accept(self, visitor):
        visitor.DrawRectangle(self.mPen, self.mX, self.mY, self.mWidth, self.mHeight)        

# Helper methods for SVG tags
def BeginTag(tag):
    return '<' + tag + ' '

def NumberAttribute(attrName, attrValue):
    return attrName + '="' + str(attrValue) + '"' + ' '

def StringAttribute(attrName, attrValue):
    return attrName + '="' + attrValue + '"' + ' '

def ColorAttribute(attrName, color):
    return attrName + '="rgb(' + str(color[0]) + ',' + str(color[1]) + ',' + str(color[2]) + ')" '

def EndTag():
    return '/>'

class SVGDrawingVisitor(DrawingVisitor):
    def __init__(self, fileName, width, height):
        try:
            self.mFile = open(fileName, 'w')
            self.mFile.write('<svg width="' + str(width) + '" height="' + str(height) + '">\n')
        except Exception as e:
            print(f"An exception occurred: {e}")

    def DrawLine(self, pen, x1, y1, x2, y2):
        line = BeginTag("line") + \
               NumberAttribute("x1", x1) + \
               NumberAttribute("y1", y1) + \
               NumberAttribute("x2", x2) + \
               NumberAttribute("y2", y2) + \
               NumberAttribute("stroke-width", pen.GetStrokeSize()) + \
               ColorAttribute("stroke", pen.GetStrokeColor()) + \
               EndTag() + '\n'
        self.mFile.write(line)

    def DrawRectangle(self, pen, x, y, width, height):
        line = BeginTag("rect") + \
               NumberAttribute("x", x) + \
               NumberAttribute("y", y) + \
               NumberAttribute("width", width) + \
               NumberAttribute("height", height) + \
               NumberAttribute("stroke-width", pen.GetStrokeSize()) + \
               ColorAttribute("stroke", pen.GetStrokeColor())
        
        if (pen.GetFillColor() == None):
               line += StringAttribute("fill", "none")
        else:
               line += ColorAttribute("fill", pen.GetFillColor())

        line += EndTag() + '\n'
        self.mFile.write(line)

    def __del__(self):
        self.mFile.write('</svg>')
        self.mFile.close()

class DrawingCanvas:
    def __init__(self, width, height):
        self.mWidth = width
        self.mHeight = height
        self.mPen = Pen() 
        self.mDrawings = []

    def SetPen(self, pen):
        self.mPen = copy.copy(pen)

    def DrawLine(self, x1, y1, x2, y2):
        self.mDrawings.append(LineDrawing(self.mPen, x1, y1, x2, y2))

    def DrawRectangle(self, x, y, width, height):
        self.mDrawings.append(RectangleDrawing(self.mPen, x, y, width, height))
                        
    def ExportSVG(self, fileName):
        svgDwgVisitor = SVGDrawingVisitor(fileName, self.mWidth, self.mHeight)
        for dwg in self.mDrawings:
            dwg.Accept(svgDwgVisitor)