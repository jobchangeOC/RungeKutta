#実行にはnumpyとmatplotlibが必要
import numpy as np
import matplotlib.pyplot as plt

import math

#nの動きによるグラフの変化を可視化するために複数回の処理
for cnt in range(4):
    #出力するファイル名の指定
    title = "sin"

    #u(x)とv(x)の初期値を設定
    u = [1.000000]
    v = [0.000000]

    #微分の刻み幅の設定
    h = 0.001

    #微分する範囲の設定
    strt = 0.000
    end = 1.000

    #比例関数のパラメータ
    def prop(x):
        #(cnt+1)回目の処理時に用いるnの値を設定
        if cnt == 0:
            num = 1
        elif cnt == 1:
            num = 5
        elif cnt == 2:
            num = 10
        else :
            num = 100

        #ここで関数を指定する
        func = 1 + math.sin(num * math.pi * x)

        return func

    #u'(x)についての微分方程式を計算する関数
    def dudx(x, ux, vx):
        #Qs(x)とQs'(x)を指定
        Qs = 1
        dQs = 0

        k = prop(x)

        #ここでu'(x)の微分方程式を設定
        du = ((-k * (ux - vx)) - (dQs * ux)) / Qs        
        return du

    #v'(x)についての微分方程式を計算する関数
    def dvdx(x, ux, vx):
        #Qa(x)とQa'(x)を指定
        Qa = 1
        dQa = 0

        k = prop(x)

        #ここでv'(x)の微分方程式を設定
        dv = ((k * (ux - vx) - (dQa * vx))) / Qa
        return dv

    #4次3変数のルンゲクッタ法を用いて数値的な解を求めるアルゴリズム
    def RungeKutta(x, uxx, vxx, h):
        #関数であるu(x+h)とv(x+h)の数値的な解を求める
        k1 = dudx(x, uxx, vxx) * h
        l1 = dvdx(x, uxx, vxx) * h

        k2 = dudx(x + (h / 2), uxx + (k1 / 2), vxx + (l1 / 2)) * h
        l2 = dvdx(x + (h / 2), uxx + (k1 / 2), vxx + (l1 / 2)) * h

        k3 = dudx(x + (h / 2), uxx + (k2 / 2), vxx + (l2 / 2)) * h
        l3 = dvdx(x + (h / 2), uxx + (k2 / 2), vxx + (l2 / 2)) * h

        k4 = dudx(x + h, uxx + k3, vxx + l3) * h
        l4 = dvdx(x + h, uxx + k3, vxx + l3) * h

        ku = uxx + ((k1 + (2 * k2) + (2 * k3) + k4) / 6)
        lv = vxx + ((l1 + (2 * l2) + (2 * l3) + l4) / 6)
        return [ku, lv]

    #出力に用いる配列の初期化
    amnt = [0.000]
    shft = [0.000]

    #for分によってstrtからendまでの微分を刻み幅hで行う処理
    for x in np.arange(strt, end, h):
        #u(x)とv(x)の位置を更新
        utemp = u[-1]
        vtemp = v[-1]

        #位置xを更新
        shft.append(x + h)

        #k(x)[u(x)-v(x)]Δxを計算
        plus = (prop(x) * (u[-1] - v[-1]) * h)

        #u(x) > v(x) が前提であるため誤処理を防ぐ
        if plus < 0:
            print(x)
            plus = 0
        
        #積分配列を更新
        amnt.append(amnt[-1] + plus)

        #各微分方程式の解を計算
        solve = RungeKutta(x, utemp, vtemp, h)

        #次に用いる解を配列へ格納
        u.append(solve[0])
        v.append(solve[1])

    #計算結果を把握したい場合にはコメントアウトを外す
    #print("x = 1, u = %.16f, tu = %.16f" % (u[-1], (1 / 2 + ((1 / 2) * math.exp(- 2 * 1)))))
    #print("x = 1, v = %.16f, tv = %.16f" % (v[-1], (1 / 2 - ((1 / 2) * math.exp(- 2 * 1)))))

    #計算結果をcnt毎にプロット
    if cnt == 0:
        plt.plot(shft, amnt, "-", label = "n = %d" % (cnt))
        #コンソール上にx=endのamnt[-1]を表示
        print("n = %f, amnt[-1] = %f" % ((cnt), amnt[-1]))
    elif cnt == 1:
        plt.plot(shft, amnt, "--", label = "n = %d" % (cnt))
        print("n = %f, amnt[-1] = %f" % ((cnt), amnt[-1]))
    elif cnt == 2:
        plt.plot(shft, amnt, "-.", label = "n = %d" % (cnt))
        print("n = %f, amnt[-1] = %f" % ((cnt), amnt[-1]))
    else:
        plt.plot(shft, amnt, ":", label = "n = %d" % (cnt))
        print("n = %f, amnt[-1] = %f" % ((cnt), amnt[-1]))


#グラフの出力処理
plt.plot(shft, amnt)

plt.xlabel("x")
plt.ylabel("amount")

plt.title(title)
plt.legend()

plt.savefig(title + ".png", dpi = 300)

#グラフを表示
plt.show()

#プロットをクリア
plt.clf()