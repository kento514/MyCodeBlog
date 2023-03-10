# 入力の基本
- 整数の入力  
`ni = lambda: int(input())`  
- リスト型の入力  
`nl = lambda: list(map(int, input().split()))`  
- 二つ以上の変数の入力  
`na = lambda: map(int,input().split())`  
- 文字列の入力  
`ns = lambda: input()`  
- 文字列を一文字ずつリストにして入力  
`nsl = lambda: list(input())`


# PracticeA - Welcome to AtCoder
ポイント：出力`print(sep='', end='')`で簡単に書ける．

# ABC086A - Product
ポイント：if分を一行で書くこと  
`'Even' if (a*b)%2 ==0 else 'Odd'`

# ABC081A - Placing Marbles
ポイント　文字列やリストの中身の数え方  
パターン１：`s.count('1')`  
パターン２:
>`import collections`  
>`l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']`  
>`c = collections.Counter(l)`  
>`print(c)`  
>`# Counter({'a': 4, 'c': 2, 'b': 1})`

# ABC081B - Shift only
ポイント：ビット演算と強制終了  
`1<<3 =8`と`exit(print('test'))`

# ABC087B - Coins
ポイント：for分の使い方．３重ループの回避
`for i in range(N)`と`//`整数のあまり

# ABC083B - Some Sums
ポイント：各桁の和を求める方法
`sum(list(map(int, str(i))))`

# ABC088B - Card Game for Two
ポイント：ソート
`x = sorted(x, reverse=True)`降順

# ABC085B - Kagami Mochi
ポイント：重複なしのリスト
`set(list)`と集合の大きさ`len(set(list))`

# ABC085C - Otoshidama
ポイント：最大ループ数・・・$10^6$

# ABC049C - 白昼夢
ポイント：リストに高速に出し入れするシステム
> `from collections import deque`
> `dlist = deque()`
> `dlist.append([1,2])`
> `dlist.pop()`
## 参考文献
[参考文献](https://qiita.com/ryosuke0825/items/bbc5c0673e6c6c958d66)

# ABC086C - Traveling
ポイント：時間を以下に減らせるか
毎回すべての時間を考慮せず，二つだけに注目する．