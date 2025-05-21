BitwiseTwo
// For this challenge you will perform a bitwise operation on two binary numbers. 
// have the function BitwiseTwo(strArr) take the array of strings stored in strArr, which will only contain two strings of equal length that represent binary numbers, 
   and return a final binary string that performed the bitwise AND operation on both strings. A bitwise AND operation places a 1 in the new string where there is a 1 in both
   locations in the binary strings, otherwise it places a 0 in that spot. For example: if strArr is ["10111", "01101"] then your program should return the string "00101"

Common Bitwise Operators
Here are the primary bitwise operators used in many programming languages:

AND (&): Returns 1 only if both corresponding bits are 1.

OR (|): Returns 1 if at least one of the corresponding bits is 1.

XOR (^): Returns 1 if the corresponding bits are different.

NOT (~): Inverts all the bits.

Left Shift (<<): Shifts bits to the left, filling with 0s on the right.

Right Shift (>>): Shifts bits to the right, filling with 0s on the left for unsigned numbers.


# In[ ]:


To convert binary strings to integers in Python, you can use the built-in int() function, specifying 2 as the base. 
Here's how you can do it:

✅ Method 1: Using int() with Base 2
binary_string = "1101"
decimal_value = int(binary_string, 2)
print(decimal_value)  # Output: 13

To convert an integer to a binary string in Python, you can utilize several built-in methods, each offering different formatting options. Here's a breakdown of the most common approaches:

### 1. Using `bin()` Function

The `bin()` function returns the binary representation of an integer prefixed with `'0b'`:([GeeksforGeeks][1])
number = 42
binary_string = bin(number)
print(binary_string)  # Output: '0b101010'
```
If you prefer the binary string without the `'0b'` prefix, you can slice it:

binary_string = bin(number)[2:]
print(binary_string)  # Output: '101010'
```
### 2. Using `format()` Function

The `format()` function provides a way to format numbers into binary strings without the `'0b'` prefix:

binary_string = format(number, 'b')
print(binary_string)  # Output: '101010'
```
For zero-padded binary strings, specify the width:([Stack Overflow][2])

padded_binary = format(number, '08b')
print(padded_binary)  # Output: '00101010'
```



---

### 3. Using f-Strings (Python 3.6+)

Python 3.6 introduced f-strings, allowing for concise formatting:

```python
binary_string = f'{number:b}'
print(binary_string)  # Output: '101010'
```



For zero-padded binary strings:

```python
padded_binary = f'{number:08b}'
print(padded_binary)  # Output: '00101010'
```



---

### 4. Manual Conversion (Bitwise Operations)

For educational purposes or custom formatting, you can manually convert an integer to a binary string using bitwise operations:

```python
def int_to_binary(num):
    if num == 0:
        return '0'
    binary = ''
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2
    return binary

binary_string = int_to_binary(number)
print(binary_string)  # Output: '101010'
```



---

### 5. Handling Negative Integers

For negative integers, the methods above will represent the number in two's complement form. If you need a custom representation (e.g., sign-magnitude), you'll need to implement additional logic.

---

**Note:** For most use cases, the `bin()` function or `format()` function are recommended due to their simplicity and efficiency.

If you have specific requirements or need further assistance, feel free to ask!

[1]: https://www.geeksforgeeks.org/integer-to-binary-string-in-python/?utm_source=chatgpt.com "Integer to Binary String in Python | GeeksforGeeks"
[2]: https://stackoverflow.com/questions/699866/convert-int-to-binary-string-in-python?utm_source=chatgpt.com "Convert int to binary string in Python - Stack Overflow"


# In[1]:


def BitwiseTwo(strArr):
    for i in strArr:
        decimal = int(strArr[0], 2) & int(strArr[1],2)
    return bin(decimal)[2:]
    
BitwiseTwo(["10111", "01101"])


# In[2]:


def BitwiseTwo(strArr):
    for i in strArr:
        decimal = int(strArr[0], 2) & int(strArr[1],2)
    return f'{decimal:05b}'
    
BitwiseTwo(["10111", "01101"])


# In[ ]:




