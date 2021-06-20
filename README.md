## これは何？

指定したディレクトリと、その配下の全てのサブディレクトリ内の.xlsx形式のファイルを探し出し、更新日時が新しい順に上位30個を表示するプログラムです。  
exeファイルを用意してあるので、Pythonがインストールされていなくても動きます。  
Windows向けです。

## 使い方
check_update.exeのファイルを、調べたいディレクトリに配置します。  
![directory](https://user-images.githubusercontent.com/32495711/122676964-33cdb000-d21b-11eb-952a-f188748e00eb.png)

例えば、上の図のように配置すると、exeファイルと同じ階層のディレクトリ(エクセル1.xlsxなど)とそのサブディレクトリ(Room1以下、Room2以下)に含まれる全ての.xlsx形式ファイルが対象です。  

サンプルとして、テスト用フォルダに空のエクセルファイルを複数配置してあるのでそこで試してみてください。  

結果は以下のように表示されます。
![image](https://user-images.githubusercontent.com/32495711/122677517-945dec80-d21d-11eb-8d40-204dd4bf53f6.png)

#### 参考
- [ファイルの更新日時でソートする](https://qiita.com/norioc/items/e5272e00f358ef692cc4)
- [Pythonのファイルをexe化する方法【初心者向け】](https://techacademy.jp/magazine/18963)

    補足：
    もしもローカルで、プログラムを書き換えて再度exeファイルにする場合は、
    pyinstallerというツールをインストールして`pyinstaller check_update.py --onefile`を走らせる必要があります。