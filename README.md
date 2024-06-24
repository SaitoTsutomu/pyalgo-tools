# pyalgo-tools

pyalgo-tools is a collection of various algorithms.

## Example ドント方式で議席数を計算

```python
print(dhondt(100, [45, 12, 34]))
```

```
[50 13 37]
```

## Example 指定した合計となる部分集合の列挙

```python
ary = [2, 1, 4, 3, 2]
for subset in enum_sub(ary, 4):
    print(f"sum({subset}) = {sum(subset)}")
```

```
sum([2, 2]) = 4
sum([1, 3]) = 4
sum([4]) = 4
```

## Example 2つの円の重なる面積

```python
print(round(circle_overlap_area(0, 2, 1, 0, 1, 2), 4))
```

```
3.1416
```

