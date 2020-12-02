from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

code = '''
def fibonacci(n):
a = 0
b = 1
for i in range(0, n):
    temp = a
    a = b
    b = temp + b
return a

# Display the first 15 Fibonacci numbers.
for c in range(0, 15):
    print(fibonacci(c))
'''
print(highlight(code, PythonLexer(), HtmlFormatter()))
print("--- END OUTPUT / START CSS ---")
#print(HtmlFormatter().get_style_defs('.highlight'))
