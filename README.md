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

$$v^{\prime}(x) = \frac{k(x) \cdot [u(x) - v(x)] - Q_a^{\prime}(x) \cdot v(x)}{Q_a(x)}$$


数値解を計算する都合で、微分の刻み幅 $h$ ごとに計算するため、  
実際に計算するのは下記のような方程式となります。


$$u(x+h) = \frac{- k(x) \cdot [u(x) - v(x)] - Q_s(x+h) \cdot u(x)}{Q_s(x)}$$

$$v(x+h) = \frac{k(x) \cdot [u(x) - v(x)] - Q_a(x+h) \cdot v(x)}{Q_a(x)}$$


$u(x)$ , $v(x)$ , $k(x)$ , $Q_s(x)$ , $Q_a(x)$ は任意の関数をプログラム内で設定します。

計算結果を用いて下記の積分を数値的に求めたグラフをファイルへ出力します。

$$\int_{strt}^{end} k(x) \cdot [u(x) - v(x)] dx$$

$strt$ と $end$ をそれぞれ指定して任意の範囲に対する積分を行います。

## 注意事項
研究では $k(x)$ , $Q_s(x)$ , $Q_a(x)$ のうち1つを任意の関数として設定して、  
その他は定数である場合における、関数のパラメータの変化によるグラフの違いを調べました。

そのため、初期設定では簡単のために $Q_s(x)$ , $Q_a(x)$ は $1$ と設定しており、  
$u(strt)=1$ , $v(strt) = 0$ と設定しています。

また、$k(x) = 1 + \sin n \pi x$ である場合に、  
$n = 1，5，10，100$ として $0 \le x \le 1$ の範囲を計算した結果をそれぞれグラフへプロットします。
