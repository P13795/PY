# -*- coding:utf-8 -*-
# 活动规则
from core.scripts import scripts_dict
from core.sub import Sub

march = scripts_dict.get("March_default")
last_word = scripts_dict.get("last_word")
card_boost = scripts_dict.get("card_boost")
Sub.start()
# 选关
last_word.stage = 4
card_boost.stage = 4
while True:
    card_boost.team = 4
    card_boost.run()
    march.start()
    last_word.team = 1
    last_word.run()
    march.start()
    last_word.team = 2
    last_word.run()
    march.start()
    last_word.team = 3
    last_word.run()
    march.start()
