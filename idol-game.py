class Idol:
  def __init__(self, name):
    self.name = name
    self.vocal = 10
    self.dance = 10
    self.visual = 10
    self.stamina = 100
    self.turn = 1
    self.max_turns = 3
    
  def show_status(self):
    print(f"\n--- {self.name} のステータス ---")
    print(f"ボーカル：{self.vocal}")
    print(f"ダンス：{self.dance}")
    print(f"ビジュアル：{self.visual}")
    print(f"体力：{self.stamina}")
    print(f"残りターン：{self.max_turns - self.turn + 1}")
    
  def lesson(self, skill):
    if self.stamina < 20:
      print("体力が足りない！先に休憩しよう")
      return False
    if skill == "1":
      self.vocal += 5
      print("ボーカルレッスン！ボーカルが5上がった")
    elif skill == "2":
      self.dance += 5
      print("ダンスレッスン！ダンスが5上がった")
    elif skill == "3":
      self.visual += 5
      print("ビジュアルレッスン！ビジュアルが5上がった")
    else:
      print("無効な選択だよ")
      return False
    self.stamina -= 20
    return True
  
  def rest(self):
    before = self.stamina
    self.stamina = min(100, self.stamina + 30)
    print(f"休息した！体力が{self.stamina - before} 回復した")
    
  def live(self):
    score = self.vocal * 2 + self.dance * 2 + self.visual
    score = score * self.stamina // 100
    
    print("\n=== ライブ結果 ===")
    print(f"アイドル：{self.name}")
    print(f"ライブスコア：{score}")
    return score
  
def main():
  print("\n=== アイドル育成シミュレーター ===")
  name = input("アイドルの名前を入力してね：").strip()
  
  if not name:
    name = "ミライ"
    
  idol = Idol(name)
  
  while idol.turn <= idol.max_turns:
    idol.show_status()
    
    print("\n何をする？")
    print("1：ボーカルレッスン")
    print("2：ダンスレッスン")
    print("3：ビジュアルレッスン")
    print("4：休憩")
    
    choice = input("> ").strip()
    
    if choice == "4":
      idol.rest()
    elif choice in ("1", "2", "3"):
      success = idol.lesson(choice)
      if not success:
        continue
    else:
      print("1~4の数字を入力してね")
      continue
    
    idol.turn += 1
    
  idol.show_status()
  idol.live()
  print("\n育成終了！")
    
if __name__ == "__main__":
  main()