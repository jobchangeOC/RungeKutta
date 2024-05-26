# RungeKutta.py

## 動作確認環境
- Windows 11 23H2
- Visual Studio Code 1.89.1
- Python 3.10.11 64-bit (microsoft-store)

## 利用ライブラリ
- numpy 1.23.5
- matplotlib 3.6.2

## 動作方法
1. numpyとmatplotlibをインストール
2. RungeKutta.pyをコンパイルして実行

## 概要
学生時代に卒業研究のため作成したプログラムです。

3変数を用いた4次のルンゲクッタ法を利用して、  
2つの下記微分方程式における数値解を計算します。

$$u^{\prime}(x) = \frac{- k(x) \cdot [u(x) - v(x)] - Q_s^{\prime}(x) \cdot u(x)}{Q_s(x)}$$
