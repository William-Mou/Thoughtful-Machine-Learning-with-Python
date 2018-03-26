# Thoughtful-Machine-Learning-with-Python
Thoughtful-Machine-Learning-with-Python

  版本同步於：https://hackmd.io/32QsBboWRAyGFmH4ah1NHw?both

# AI學習筆記
> [常見名詞觀念釐清](https://www.zhihu.com/question/57770020)
![](https://i.imgur.com/EOiLBrj.jpg)

## 人工智能的範疇
![](https://pic1.zhimg.com/80/v2-e358e127afbe5963f5b8622e2dd5b49f_hd.jpg)
* 專家系統
* 機器學習
* 進化計算
* 模糊邏輯
* 計算機視覺
* 自然語言處理
* 推薦系統等

## 機器學習
[William Mou's Github](https://github.com/William-Mou/Python-Machine-Learning)
[學習書籍：Python機器學習](http://www.open-open.com/doc/view/217bafe25fb4461391e7e2a3e98d6bf0)

### Python基礎套件教學
[SciPy Lecture Notes 中文版
](https://wizardforcel.gitbooks.io/scipy-lecture-notes/content/7.html)[numpy中文教程
](http://hoyoung.net/2016/12/16/numpy-tutorial/)
* 傳統算法
    * 決策樹
    * 聚類
    * 貝葉斯分類
    * 支持向量機
    * EM
    * Adaboost
    
[距离及相似度度量方法](http://blog.csdn.net/mingzai624/article/details/53814409)
* 學習方法的分類  
    * 半監督學習
    * 集成學習
    * 深度學習
    * 監督學習（如分類問題）
        * 分類法
            1. 訓練數據集中學習
            2. 回歸分析導出模型
            3. 對新數據做出預測
        * 回歸預測
            1. 預測變數+反映變數
            2. 發覺變數間的關係
            3. 找出變數的適合曲線 
    * 強化學習
        1. 與環境互動改善自身技能
        2. 透過測量函數回傳度量質
        3. 透過方式最大化獎勵：
            * 嘗試錯誤
            * 審議式規劃
    * 非監督學習（如聚類問題）
      沒有已知的結果和獎勵函數，透過探索數據本身的結構得到資訊
        1. 探索式數據分析技術
        2. 允許組織技術至有意義的「子族群」
        3. 使特徵有一定程度的相似性，發現特殊分群

### 深度學習，一種實現機器學習的技術
* 背景
    > 深度學習本來並不是一種獨立的學習方法，其本身也會用到有監督和無監督的學習方法來訓練深度神經網絡。但由於近幾年該領域發展迅猛，一些特有的學習手段相繼被提出（如殘差網絡），因此越來越多的人將其單獨看作一種學習的方法。

    > 最初的深度學習是利用深度神經網絡來解決特徵表達的一種學習過程。深度神經網絡本身並不是一個全新的概念，可大致理解為包含多個隱含層的神經網絡結構。為了提高深層神經網絡的訓練效果，人們對神經元的連接方法和激活函數等方面做出相應的調整。

* 缺點

    1. 深度學習模型需要大量的訓練數據，才能展現出神奇的效果，但現實生活中往往會遇到小樣本問題，此時深度學習方法無法入手，傳統的機器學習方法就可以處理。
  
    2. 有些領域，採用傳統的簡單的機器學習方法，可以很好地解決了，沒必要非得用複雜的深度學習方法。
  
    3. 深度學習的思想，來源於人腦的啟發，但絕不是人腦的模擬，舉個例子，給一個三四歲的小孩看一輛自行車之後，再見到哪怕外觀完全不同的自行車，小孩也十有八九能做出那是一輛自行車的判斷，也就是說，人類的學習過程往往不需要大規模的訓練數據，而現在的深度學習方法顯然不是對人腦的模擬。

* 理念
    >Science is NOT a battle, it is a collaboration. We all build on each other's ideas. Science is an act of love, not war. Love for the beauty in the world that surrounds us and love to share and build something together. That makes science a highly satisfying activity, emotionally speaking!
    >
    >這段話的大致意思是，科學不是戰爭而是合作，任何學科的發展從來都不是一條路走到黑，而是同行之間互相學習，互相借鑒，博採眾長，相得益彰，站在巨人的肩膀上不斷前行。機器學習的研究也是一樣，你死我活那是邪教，開放包容才是正道。

[介紹ppt](http://bigdata.lic.nkfust.edu.tw/ezfiles/141/1141/img/1900/809336811.pdf)




### AIJT梯度下降法手算範例講解
###### tags : `AI Junior Talk 人工智慧青年論壇`
> [name=牟展祐]  [time=2018,2,23] 


## 參考資料來源與出處：
 
[人工智能、机器学习和深度学习的区别？　作者：育心。](https://www.zhihu.com/question/57770020/answer/249708509)
[附資源與完整指導！帶你從零開始掌握 Python 機器學習](https://buzzorange.com/techorange/2017/08/18/learn-machine-learning-and-python-in-14-steps/)
[深度學習 Deep Learning：中文學習資源整理](https://jerrynest.io/deep-learning-resource/ "深度學習 Deep Learning：中文學習資源整理")
[Machine Learning: Python 機器學習：使用Python](https://machine-learning-python.kspax.io/Classification/ex5_Linear_and_Quadratic_Discriminant_Analysis_with_confidence_ellipsoid.html)
[Machine Learning: Python 機器學習：使用Python](https://www.gitbook.com/book/htygithub/machine-learning-python/details)
[資源速查表](https://itw01.com/ANEGODP.html)

## 書籍選購
[Python機器學習](http://www.books.com.tw/products/0010728558)
[Deep Learning：用Python進行深度學習的基礎理論實作](http://www.books.com.tw/products/0010761759)
[今天不學機器學習，明天就被機器取代：從Python入手+演算法](http://www.books.com.tw/products/0010737303)
[零起點Python機器學習快速入門](http://www.books.com.tw/products/CN11434263)
