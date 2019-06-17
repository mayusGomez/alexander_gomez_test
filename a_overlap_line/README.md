## Execution

The class lines.line.XLine allow create a x-axis line. This Class have the method 'detect_overlap' for compare with another instance and identify whether they overlap:

```python
from lines.line import XLine
from lines.exception import WrongValuesException

line_one = XLine(1,6)
line_two = XLine(6,8)
resp = line_one.detect_overlap(line_two)

```
 In this example, resp == False, beacuse both lines are not overlap

 ```python
from lines.line import XLine
from lines.exception import WrongValuesException

line_one = XLine(1,6)
line_two = XLine(5,8)
resp = line_one.detect_overlap(line_two)

```

In this example, resp == False, because both lines are overlap

## Environment

- python 3.6 installed
- clone repository: $git clone ...
- Locate to the folder: cd a_overlap_line
- Create virtual environment: $virtualenv --python python3 venv
- Install requirements: $pip install -r requirements.txt
- For test, run $pytest

