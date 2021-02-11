#!/usr/bin/env python
# -*- coding: utf-8 -*-
#上記2行は必須構文のため、コメント文だと思って削除しないこと
#Python2.7用プログラム

#ROS関係ライブラリ
import rospy #ROSをpythonで使用するのに必要
from topic_sample.msg import message_file # メッセージファイルの読み込み（from パッケージ名.msg import 拡張子なしメッセージファイル名）



class Subscriber(): #サブスクライバのクラス
    def __init__(self):
        self.subscriber = rospy.Subscriber('topic_name', message_file, self.callback) #サブスクライバのインスタンス生成



    def callback(self, message): #トピックからメッセージを受信するたびに呼び出されるコールバック関数
        rospy.loginfo("メッセージの受信:{}".format(message.count)) #ログの表示



def main(): #メイン関数
    rospy.init_node('subscriber_sample', anonymous=True) #ノードの初期化と名前の設定
    sub = Subscriber() #クラスのインスタンス作成（クラス内の関数や変数を使えるようにする）
    rospy.spin() #終了防止



if __name__ == "__main__": #Pythonファイル名（__name__）が実行ファイル名（__main__）である場合（このPythonファイルをモジュールとして使用せず、実行ファイルとして扱う場合）
    try: #エラーが発生しなかった場合
        main() #メイン関数の実行
    except rospy.ROSInterruptException: #エラーが発生した場合
        pass #処理の実行をパスする
