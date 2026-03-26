import logging

'''
### **Handler**

A *handler* decides **where** log messages are sent (file, console, etc.).
Loggers generate messages, and handlers deliver them to different outputs.
Multiple handlers can be attached to the same logger.

### **FileHandler**

`FileHandler` writes log messages to a **file**.
Useful for saving logs permanently for debugging or audit purposes.
You specify a filename like `FileHandler("app.log")`.

### **StreamHandler**

`StreamHandler` sends log messages to an **output stream**, usually the console (`stdout`).
Used when you want logs to appear on-screen while the program runs.
It prints every log message to the terminal by default.

The log messages will be shown on the terminal by default where u will be running your python program.

'''

# The default value of filemode in logging.basicConfig() is 'a'.

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers= [
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmeticApp")

def add(a,b):
    result = a+b
    logger.debug(f"Adding {a} and {b} = {result}")
    return result

def sub(a,b):
    result = a-b
    logger.debug(f"Sbtracting {b} from {a} = {result}")
    return result

def mul(a,b):
    result = a*b
    logger.debug(f"Multiplying {a} and {b} = {result}")
    return result

def div(a,b):
    try:
        result = a/b
        logger.debug(f"Dividing {a} by {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
    
add(10,15)
sub(15,10)
mul(10,20)
div(20,0)