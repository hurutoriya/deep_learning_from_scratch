# ゼロから作るディープラーニング

- 2020/06/13 start
- 2020/12/10 re-start

## 1 Python の基礎

スキップ

## 2 パーセプトロン

y = {0 (if w1x1 + w2x2 <= theta),1 if w1x1 + w2x2 > theta

しきい値を超えれば、yが発火する

### 単純な論理回路

- And をパーセプトロンで表現
  - (w1,w2,theta), (1,1,1) でOK.(a,a,a) でANDになる
  - b is bias, 全体的な発火のｙしやすさ
  - バイアスを組み込んで、しきい値に利用できる
- NAND 完全(NANDにより、他の回路を再現可能)

### 2.4 パーセプトロンの限界

- XOR のような境界を作りたい場合、不可能。一層のパーセプトロンでは線形の境界しか貼れない
- 2層のパーセプトロンで非線形なシグモイド関数を使えば任意の関数が表現可能である

### まとめ

- 多層のパーセプトロンは非線形領域の表現ができる

## 3. ニューラルネットワーク

