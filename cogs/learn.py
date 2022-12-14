import random

import discord
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice


class learn(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot

  @app_commands.command(name = "nihongo", description = "Learn Hiragana/Katakana/Kanji")
  @app_commands.choices(subject=[Choice(name="Hiragana",value='hiragana'),Choice(name="Katakana",value='katakana'),Choice(name="Kanji",value='kanji')])
  async def nihongo(self, interaction: discord.Interaction, subject: str):

    # hiragana
    hiragana = {"あ":"a",
                "い":"i",
                "う": "u",
                "え": "e",
                "お": "o",
                "か": "ka",
                "き": "ki",
                "く": "ku",
                "け": "ke",
                "こ": "ko",
                "さ": "sa",
                "し": "shi",
                "す": "su",
                "せ": "se",
                "そ": "so",
                "た": "ta",
                "ち": "chi",
                "つ": "tsu",
                "て": "te",
                "と": "to",
                "な": "na",
                "に": "ni",
                "ぬ": "nu",
                "ね": "ne",
                "の": "no",
                "は": "ha",
                "ひ": "hi",
                "ふ": "fu",
                "へ": "he",
                "ほ": "ho",
                "ま": "ma",
                "み": "mi",
                "む": "mu",
                "め": "me",
                "も": "mo",
                "や": "ya",
                "ゆ": "yu",
                "よ": "yo",
                "ら": "ra",
                "り": "ri",
                "る": "ru",
                "れ": "re",
                "ろ": "ro",
                "わ": "wa",
                "を": "wo",
                "が": "ga",
                "ぎ": "gi",
                "ぐ": "gu",
                "げ": "ge",
                "ご": "go",
                "ざ": "za",
                "じ": "ji",
                "ず": "zu",
                "ぜ": "ze",
                "ぞ": "zo",
                "だ": "da",
                "ぢ": "ji",
                "づ": "zu",
                "で": "de",
                "ど": "do",
                "ば": "ba",
                "び": "bi",
                "ぶ": "bu",
                "べ": "be",
                "ぼ": "bo",
                "ぱ": "pa",
                "ぴ": "pi",
                "ぷ": "pu",
                "ぺ": "pe",
                "ぽ": "po",
                "ん": "n",
                "きゃ": "kya",
                "きゅ": "kyu",
                "きょ": "kyo",
                "しゃ": "sha",
                "しゅ": "shu",
                "しょ": "sho",
                "ちゃ": "cha",
                "ちゅ": "chu",
                "ちょ": "cho",
                "にゃ": "nya",
                "にゅ": "nyu",
                "にょ": "nyo",
                "ひゃ": "hya",
                "ひゅ": "hyu",
                "ひょ": "hyo",
                "みゃ": "mya",
                "みゅ": "myu",
                "みょ": "myo",
                "りゃ": "rya",
                "りゅ": "ryu",
                "りょ": "ryo",
                "ぎゃ": "gya",
                "ぎゅ": "gyu",
                "ぎょ": "gyo",
                "じゃ": "ja",
                "じゅ": "ju",
                "じょ": "jo",
                "ぢゃ": "ja",
                "ぢゅ": "ju",
                "ぢょ": "jo",
                "びゃ": "bya",
                "びゅ": "byu",
                "びょ": "byo",
                "ぴゃ": "pya",
                "ぴゅ": "pyu",
                "ぴょ": "pyo"
               }
    if subject == 'hiragana':
      h, eng = random.choice(list(hiragana.items()))
      
      await interaction.response.send_message(f"What sound is ``{h}``?")
      reply = await self.bot.wait_for('message', check=None)
      if str(reply.content.lower()) == eng:
         await interaction.followup.send("Correct!")
      else:
         await interaction.followup.send(f"Incorrect. Answer: {eng}")

    # katakana
    katakana = {"ア":"a",
                "イ": "i",
                "ウ": "u",
                "エ": "e",
                "オ": "o",
                "カ": "ka",
                "キ": "ki",
                "ク": "ku",
                "ケ": "ke",
                "コ": "ko",
                "サ": "sa",
                "シ": "shi",
                "ス": "su",
                "セ": "se",
                "ソ": "so",
                "タ": "ta",
                "チ": "chi",
                "ツ": "tsu",
                "テ": "te",
                "ト": "to",
                "ナ": "na",
                "ニ": "ni",
                "ヌ": "nu",
                "ネ": "ne",
                "ノ": "no",
                "ハ": "ha",
                "ヒ": "hi",
                "フ": "fu",
                "ヘ": "he",
                "ホ": "ho",
                "マ": "ma",
                "ミ": "mi",
                "ム": "mu",
                "メ": "me",
                "モ": "mo",
                "ヤ": "ya",
                "ユ": "yu",
                "ヨ": "yo",
                "ラ": "ra",
                "リ": "ri",
                "ル": "ru",
                "レ": "re",
                "ロ": "ro",
                "ワ": "wa",
                "ヲ": "wo",
                "ン": "n",
                "ガ": "ga",
                "ギ": "gi",
                "グ": "gu",
                "ゲ": "ge",
                "ゴ": "go",
                "ザ": "za",
                "ジ": "ji",
                "ズ": "zu",
                "ゼ": "ze",
                "ゾ": "zo",
                "ダ": "da",
                "ヂ": "ji",
                "ヅ": "zu",
                "デ": "de",
                "ド": "do",
                "バ": "ba",
                "ビ": "bi",
                "ブ": "bu",
                "ベ": "be",
                "ボ": "bo",
                "パ": "pa",
                "ピ": "pi",
                "プ": "pu",
                "ペ": "pe",
                "ポ": "po",
                "キャ": "kya",
                "キュ": "kyu",
                "キョ": "kyo",
                "シャ": "sha",
                "シュ": "shu",
                "ショ": "sho",
                "チャ": "cha",
                "チュ": "chu",
                "チョ": "cho",
                "ニャ": "nya",
                "ニュ": "nyu",
                "ニョ": "nyo",
                "ヒャ": "hya",
                "ヒュ": "hyu",
                "ヒョ": "hyo",
                "ミャ": "mya",
                "ミュ": "myu",
                "ミョ": "myo",
                "リャ": "rya",
                "リュ": "ryu",
                "リョ": "ryo",
                "ギャ": "gya",
                "ギュ": "gyu",
                "ギョ": "gyo",
                "ジャ": "ja",
                "ジュ": "ju",
                "ジョ": "jo",
                "ヂャ": "ja",
                "ヂュ": "ju",
                "ヂョ": "jo",
                "ビャ": "bya",
                "ビュ": "byu",
                "ビョ": "byo",
                "ピャ": "pya",
                "ピュ": "pyu",
                "ピョ": "pyo"
               }
    if subject == 'katakana':
      h, eng = random.choice(list(katakana.items()))
      
      await interaction.response.send_message(f"What sound is ``{h}``?")
      reply = await self.bot.wait_for('message', check=None)
      if str(reply.content.lower()) == eng:
         await interaction.followup.send("Correct!")
      else:
         await interaction.followup.send(f"Incorrect. Answer: {eng}")
        
    # kanji
    kanji = {"水 / Mizu":"water",
             "明 / Akira": "bright",
             "行": "go",
             "極 / Kyoku": "extreme",
             "度 / Do": "degree",
             "輸": "transport",
             "雄 / Osu": "masculine",
             "熊 / Kuma": "bear",
             "子 / Ko": "child",
             "清": "clear",
             "京 / Kyō": "capital",
             "兵 / Hei": "soldier",
             " / Tsuyo": "strong",
             "出口 / Deguchi": "exit",
             "改札口 / Kaisatsu kuchi": "ticket gate",
             "駅 / Eki": "station",
             "電車 / Densha": "train",
             "地下鉄 / Chikatetsu": "subway",
             "営業中 / Eigyōchū": "open",
             "お湯 / Oyu": "hot water",
             "お手洗い / O tearai": "toilet",
             "辛い / Tsurai": "spicy",
             "料金 / Ryōkin": "fee",
             "無料 / Muryō": "free",
             "入場料 / Nyūjō-ryō": "entrance fee",
             "価格 / Kakaku": "price",
             "半額 / Hangaku": "half price",
             "女 / On'na": "female",
             "男 / Otoko": "male",
             "右 / Migi": "right",
             "左 / Hidari": "left",
             "非常口 / Hijō": "emergency exit",
             "禁止 / Kinshi": "prohibited",
             "注意 / Chūi": "caution",
             "薬 / Kusuri": "medicine",
             "拉麺 / Rāmen": "ramen",
             "寿司 / Sushi": "sushi",
             "日 / Hi": "sun",
             "年 / Toshi": "year",
             "国 / Kuni": "country",
             "人 / Hito": "people",
             "生 / Nama": "life",
             "分 / Bun": "minute",
             "時 / Toki": "time",
             "市 / Ichi": "city",
             "米 / Amerika": "rice",
             "円 / Yen": "yen",
             "内 / Uchi": "inside",
             "者 / Mono": "person",
             "学 / Gaku": "study",
             "対 / Tai": "opposite",
             "小 / Ko": "small",
             "全 / Zen": "whole",
             "北 / Kita": "north",
             "問 / Toi": "question",
             "県 / Ken": "prefecture",
             "野 / No": "field",
             "山 / Yama": "mountain",
             "実 / Mi": "fruit",
             "場 / Ba": "place",
             "心 / Kokoro": "heart",
             "食 / Shoku": "food",
             "飲 / In": "drink",
             "歩く / Aruku": "walk",
             "大学 / Daigaku": "university",
             "音楽 / Ongaku": "music",
             "写真 / Shashin": "photo",
             "走る / Hashiru": "run",
             "偽 / Nise": "false",
             "前方 / Zenpō": "forward",
             "止まる / Tomaru": "stop",
             "緊急 / Kinkyū": "emergency",
             "漢字 / Kanji": "kanji",
             "寝る / Neru": "sleep",
             "春 / Haru": "spring",
             "秋 / Aki": "autumn",
             "冬 / Fuyu": "winter",
             "夏 / Natsu": "summer",
             "旅人 / Tabibito": "tourist",
             "茶店 / Chamise": "teahouse",
             "空 / Sora": "sky"
             ""
            }
    if subject == 'kanji':
      h, eng = random.choice(list(kanji.items()))
      
      await interaction.response.send_message(f"What does ``{h}`` mean?")
      reply = await self.bot.wait_for('message', check=None)
      if str(reply.content.lower()) == eng:
         await interaction.followup.send("Correct!")
      else:
         await interaction.followup.send(f"Incorrect. Answer: {eng}")


# cog setup

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(
    learn(bot),
    guilds = [discord.Object(id = 489331089341415454), discord.Object(id = 1040458176123916318)])