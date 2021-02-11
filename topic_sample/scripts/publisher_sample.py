#!/usr/bin/env python
# -*- coding: utf-8 -*-
#上記2行は必須構文のため、コメント文だと思って削除しないこと
#Python2.7用プログラム

#ROS関係ライブラリ
import rospy #ROSをpythonで使用するのに必要
from topic_sample.msg import message_file # メッセージファイルの読み込み（from パッケージ名.msg import 拡張子なしメッセージファイル名）
#その他のライブラリ
import sys #プログラム終了に使用



class Publisher(): #パブリッシャのクラス
    def __init__(self):
        self.message = message_file() #メッセージファイルのインスタンス生成
        self.publisher = rospy.Publisher('topic_name', message_file, queue_size=10) #パブリッシャのインスタンス生成
        self.count = 0 #カウントの宣言
        self.rate = rospy.Rate(1) # 1秒間に1回（1Hz)



    def make_msgs(self): #メッセージの作成
        self.message.count = self.count #メッセージ変数に代入



    def send_msgs(self): #メッセージの送信
        while not rospy.is_shutdown(): #エラー発生や強制終了がなければずっと繰り返す
            try:
                self.make_msgs() #メッセージの作成
                self.publisher.publish(self.message) #作成したメッセージの送信
                rospy.loginfo("メッセージの送信:{}".format(self.message.count)) #ログの表示
                self.count += 1 #カウントを1増やす
                self.rate.sleep() #待機

            except KeyboardInterrupt: #Ctrl+Cが押された場合
                sys.exit() #プログラムの終了



def main(): #メイン関数
    rospy.init_node('publisher_sample', anonymous=True) #ノードの初期化と名前の設定
    pub = Publisher() #クラスのインスタンス作成（クラス内の関数や変数を使えるようにする）
    pub.send_msgs() #メッセージの送信
    rospy.spin() #終了防止



if __name__ == "__main__": #Pythonファイル名（__name__）が実行ファイル名（__main__）である場合（このPythonファイルをモジュールとして使用せず、実行ファイルとして扱う場合）
    try: #エラーが発生しなかった場合
        main() #メイン関数の実行
    except rospy.ROSInterruptException: #エラーが発生した場合
        pass #処理の実行をパスする
