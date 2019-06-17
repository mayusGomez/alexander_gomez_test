"""
XLine Class
Allow build Line X-axis object (x1, x2)
"""

from exception import WrongValuesException

class XLine:
    def __init__(self, x1, x2):
        """
        Init Class with first and second point
        """
        self.x1 = x1
        self.x2 = x2

    def detect_overlap(self, xlin):
        """
        detect_overlap
        :parameter xlin: XLine instanciate object
        :return boolean: True whether they overlap, and False otherwise
        :raise WrongValuesException: For non numeric values, decimal values or not line(point)  
        """
        line_minor = None
        line_major = None

        if self.x1 <= xlin.x1:
            line_minor = self
            line_major = xlin
        else:
            line_minor = xlin
            line_major = self
        
        if line_major.x1 >= line_minor.x1 and line_major.x1 < line_minor.x2:
            return True
        else:
            return False
