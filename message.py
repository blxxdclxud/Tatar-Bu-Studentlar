HELP_COMMAND = "Привет. Я тут, чтобы помочь. Если у тебя есть вопросы по квесту, то пиши [Mr Dextrу](https://t.me/amiros12345)"
BOT_DESC = """
👋Привет, детектив! Я СледоБот🕵️‍♂️, твой связной в мире тайн!  

Я предлагаю тебе решить уникальные детективные истории🧩️. Готов к захватывающему приключению? Тогда начнем! 🚀 
"""
quests = {
    "Вкусная Контрабанда 🍭": {
        "description": "❗️Важные новости❗️\n*РИА Новости* сообщило о успешном задержании контрабандистов нашей полицией👮‍♂️. Однако, полиция выражает недовольство результатами операции, так как главный товар ускользнул с преступниками, и до сих пор остается неизвестным. Это создает серьезную угрозу безопасности города💢.\n\nТем временем на улице Баумана наблюдается необычная активность✨. Все больше людей собирается здесь, пытаясь найти загадочный вкусный товар🍭, о котором ходят слухи",
        "offer_image": "https://static.pepper.ru/threads/raw/6dZQJ/392174_1/re/768x768/qt/60/392174_1.jpg",
        "offer": "🎉Ура!!!\n\nМы расшифровали текст! Теперь мы знаем, кто этот преступник и что за товар он поставлял. Это были запрещенные сладкие тапиоки🍬, вызывающие привыкание.\n\nТакже мы выяснили, что рост активности людей на Баумана был связан с желанием выпить боба-чай из этих тапиок. Надеемся, что люди и кофейня не пострадали. \n\nВ любом случае, благодарим тебя за успешное расследование👍. Также кофейня, ставшая жертвой этой схемы, выражает тебе свою признательность и предоставляет скидку 20% на все их напитки😁. \n\nДавай отдыхай, ждем тебя на следующем деле!",
        "free": True,
        "puzzles": [
            {"image": "https://img.tourister.ru/files/2/3/1/9/0/6/4/6/clones/870_653_fixedwidth.jpg",
             "description": "Привет, новобранец. Чтоб ты знал, я на тебя особых надежд не возлагаю. Мы уже 2 недели работаем над этим делом, и я сомневаюсь, что у тебя что-то получится! \n\nЗадание можешь прочитать на столе.\n\nЗадание 📋:_Наши информаторы доложили, что в последний раз люди видели подозрительного незнакомца возле фонтана с четырьмя жабами. Мы предполагаем, что это наш подозреваемый. Скорее всего, в этот день он остановился неподалеку. Очевидцы говорят, что на этаже, где он остановился, было 7 окон. Помогите нам узнать, в каком месте он остановился._```",
             "options": ["Дом Чак-чака 🏵", "Лабиринт Фета ⛓", "Дом вверх дном 🏠", "Вернисаж Ремесел ⚒"],
             "wait": 'Мы получили ваш ответ, скоро проверим...',
             "answer": "вернисаж ремесел ⚒",
             "exception": "🕵️‍♂️ По вашей наводке наши сыщики обыскали {answer}, однако никаких улик не нашли. Попробуйте другие варианты."},
            {"image": None,
             "description": "Наши следователи что-то докладывают...\n\nМЫ НАШЛИ ЗАПИСКУ 📝!!!\n\nВ записке преступник написал следующее: _Вечером на нулевом километре, туда куда смотрит *S*, долго ждать не буду_. \n\nЧто это значит? Найдите это место и доложите, что вы нашли",
             "options": [],
             "wait": 'Отправили запрос следователям, скоро проверят...',
             "answer": "дом книги",
             "exception": "Следователи ничего не нашли. Вы уверены, что указали все правильно 🤨? Попробуйте еще раз."},
            {"image": "https://s1.stc.all.kpcdn.net/putevoditel/projectid_379258/images/tild3430-6664-4639-b565-373563356665__edc48dc599feca9c544d.jpg",
             "description": "Отлично!\n\nСледователи обнаружили негодяев, проанализировав камеры и прослушав разговор подозреваемых. В записи упоминалась какая-то Екатерина и ступеньки. Кроме того, мы нашли зашифрованное письмо.\n\nЭх, что они вообще имели в виду? Если у тебя есть какие-то идеи (может быть ты найдешь шифр), дай нам знать скорее. 📦🌙\n\nНам нужно расшифровать этот шифр, чтобы выйти на след преступников.",
             "options": ["*️⃣⏺🔽➡️↘️↪️⬆️", "⏬⏹#️⃣5️⃣ℹ️⤵️🔀", "⏬⏹⏭6️⃣5️⃣⏹🔢", "⏬⏹#️⃣5️⃣↩️🔂🔡"],
             "wait": 'Пробуем расшифровать...',
             "answer": "⏬⏹#️⃣5️⃣ℹ️⤵️🔀",
             "exception": "🤔 Нет... Ничего не выходит. Посмотри, может ты еще что-то найдешь?"},
        ]
    },
    "Secret Place 🤫": {
        "description": "В центре города ходят слухи о ресторане, которого нет на карте. \n\nДжон Регис 👨🏻‍🍳, известный гурман и таинственная личность, посещал этот ресторан в тайне 🤫. Однажды он оставил за собой следы 👣 загадок, которые могут привести к этому тайному ресторану 🍖🍜.",
        "offer_image": "https://static.pepper.ru/threads/raw/6dZQJ/392174_1/re/768x768/qt/60/392174_1.jpg",
        "offer": None,
        "free": True,
        "puzzles": [
            {"image": "https://megotel.ru/images/places/760/61f97ed7b5a3bff9.jpg",
             "description": "Люди утверждают, что видели Джона Региса перед арабскими часами. Он часто напевал один куплет: _Словно золото оно обливается под солнечными лучами и зовет всех к себе_. \n\nЧто он имел ввиду?",
             "options": ["Отель Татарстан 🏨", "Колокольня 🔔", "Гум 🏬", "Кольцо 🛍"],
             "wait": 'Хммм...',
             "answer": "кольцо 🛍",
             "exception": "У нас не получается ничего найти, попробуйте другие варианты."},
            {"image": None,
             "description": "🎉🎉Ура🎉🎉\n\nМы нашли новый след, то есть подсказку: *_то, что ты ищешь на 3, или 4 этаже_*. Что на этом этаже?",
             "options": ["рестораны 🍬", "магазины одежды 👗", "магазины одежды 🛍", "продукты 🛒"],
             "wait": 'Тик, так, тик, так...',
             "answer": "рестораны 🍬",
             "exception": "На этаже что ты ищешь нет подобного"},
            {"image": "https://img.freepik.com/premium-photo/empty-white-long-rectangular-plate_172251-4.jpg",
             "description": "Воу!!!\n\nВот мы уже на финишной прямой, осталось последняя подсказка Региса: _вкусно бывает тогда, когда тарелка огромна, и полностью едой набита_. Где это может быть?",
             "options": ["Naruto 🏡", "Gagawa 🏛", "Akira 🏡", "Hoshiguma 🏡"],
             "wait": 'Ahahahaha',
             "answer": "gagawa 🏛",
             "exception": "нет( 😅🔫"},
        ]
    },
    "Тайна Шоколада 🤤": {
        "description": "🍫 У известного шоколатье, мистера Густава, украли рецепт его нового шоколада 'Провансаль'. Мистер Густав обещал хорошую награду тем, кто найдет преступника. Однако надо торопиться, так как это нужно сделать до того, как рецепт окажется у конкурентов. 🕵️‍♂️🚨",
        "offer_image": None,
        "offer": None,
        "free": False,
        "puzzles": [
            {"image": "https://images11.graziamagazine.ru/upload/img_cache/849/849355b9d2b7b18af1952946c626cb64_cropped_666x468.jpg",
             "description": "🍫 Сегодня тебе предстоит заняться очень странным делом. Утром наша служба безопасности обнаружила, что известный шоколатье, мистер Густав, обвиняет вора в краже его нового рецепта шоколада 'Провансаль'. Подозреваемый был замечен возле улицы 'Шоколадной Галереи'. Посмотрите вокруг и сообщите, если что-то обнаружите. 🕵️‍♂️🔍",
             "options": [],
             "wait": '',
             "answer": "записка",
             "exception": "🔍 Мы проверили твою улику, но к сожалению, ничего не нашли. Попробуй еще раз. 🤔"},
            {"image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSpyh46M1AL4dmyBCnqHZaKMFk5ibHSR-snCVQmGwyaFWJhisvEkS8L2YqthnQITrMflKs&usqp=CAU",
             "description": "🕵️‍♂️ Отлично, наши следователи проанализировали записку и расшифровали имя 'Мортез'.\n\n🔍 Мортез, Мортез... Хмм... Проверь магазин 'Шоколадные Изыски'. Хозяина этого ресторана зовут Дартаньян. Может быть, он что-то знает? 🤔🍫",
             "options": ["Пистолет", "Камень", "Бумага", "Варежку"],
             "wait": '',
             "answer": "бумага",
             "exception": "Ваши усилия помогли, но нам нужно еще больше информации. 📝🔍"},
            {"image": None,
             "description": "Теперь, когда мы знаем, кто такой 'Мортез', мы можем его поймать. Наш 'Мортез', или Артём, назначил встречу с директором 'Сладкой Жизни'. Я думаю, ты можешь представиться директором и выведать у него конфиденциальную информацию. Мы надеемся на тебя, больше у нас такого шанса может не быть. 🕵️‍♂️🔍",
             "options": [],
             "wait": '',
             "answer": "шоколадница",
             "exception": "Нет! Ваша информация была полезной, но нам нужно еще больше, чтобы поймать преступника. 🚨🔍"},
        ]
    },
}

responses = {
    "quests": "В нашем городе 🌆 царит видимая спокойная обстановка ☘️, но за этой идиллией скрываются тайны 😈 и незаконные сделки 💀...\n\nУ нас есть незаконченные дела 🧾, которые требуют вашего внимания.\nПогрузитесь в мир тайн и загадок, сможете ли вы раскрыть их тайны? ️",
    "congratulation": "Поздравляем, вы прошли квест!",
    "db_problem": "Похоже у нас проблемы, мы потеряли все ваши данные. Квест придется начать заново.",
    "so_whats_next": "Что дальше? \n\nМы рады, что вы уделили время нашему проекту! 🥰 Будем очень признательны, если поделитесь своими впечатлениями и предложениями о том, что вам понравилось и что можно улучшить. Вы можете оставить свой фидбэк по команде '👍Feedback👎. \n\nА еще у нас есть дополнительный, платный квест😄. Он похож на предыдущий по своей структуре, однако рассказывает другую историю. Вы можете ознакомиться с ним нажав '👽👂👣👹🔥☠️' на клавиатуре. Приключения ждут вас!",
    "user_results": ["Ваше нынешнее звание: Рядовой 🍐", "Ваше нынешнее звание: Младший лейтенант 🔸🔸.\n\nВы повышены за помощь в деле контробандистов"],
    "end_feedback": "Спасибо за feedback 🙏",
}
dop = '🥳😎😊🙏⚡️🔥✨⭐️🏆🎖🏅🎗🎊🎉❤️💖❤️‍🔥💯✅'