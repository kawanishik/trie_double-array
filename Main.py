import sys

class Tester:
    def __init__(self, num):
        self.num = num
        input_file = "s" + num + ".txt" # データセット作成に使用するファイル
        test_file = "t" + num + ".txt"  # テストに使用するファイル
        
        self.input_data = []            # データセット作成のファイルを読み込む
        with open(input_file, 'r', encoding='utf-8') as f_in:
            lines = f_in.read()
            for line in lines.split('\n'):
                if(len(line) != 0):
                    self.input_data.append(line)
        
        self.test_data = dict()         # テストに使用するファイルを読み込む
        with open(test_file, encoding='utf-8') as f_test:
            lines = f_test.readlines()
            for line in lines:
                key, exists = line.strip().split()
                self.test_data[key] = exists == '1'
    
    # テスト用の関数
    def test(self):
        check = True
        for key in self.test_data:
            check = self.contains(key)
            if not check:
                break
        if check:
            print("ok")
        else:
            print("failed...")

    # 辞書の作成
    def make_dic(self):
        # self.input_dataに辞書作成用のデータ
        # print(self.input_data)
        # self.test_dataにテスト用のデータ
        # print(self.test_data)
        pass
    
    # keyが辞書に含まれているのかを確かめる用の関数
    def contains(self, key):
        # t1.txtの内容を用いてテスト(s1.txtが辞書作成用のデータの場合)
        # keyが辞書に含まれている場合はTrue, 含まれていなければFalse
        # greenの場合 : True
        # cyanの場合  : False
        pass


if __name__ == '__main__':
    argv = sys.argv
    if(len(argv) == 1):
        print("not select file num")
        exit(0)
    else:
        test = Tester(argv[1])
        test.make_dic()
        test.test()


