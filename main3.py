from pyscript import document

def displayPlayers(event=None):
    players = [
        'Max Ancheta',
        'Alonso Asuncion',
        'Enzo Battung',
        'Victor Buenvenida',
        'Kayla Casul',
        'Athena Catapang',
        'Cade Chua',
        'Zyan Eusebio',
        'Radhika Evangelio',
        'Mara Fado',
        'Kleiser Fermocil',
        'Curt Fernando',
        'Ethan Francia',
        'Sophia Jimenez',
        'Javi Mabilog',
        'AC Mactal',
        'Soleil Magday',
        'Yanna Moya',
        'Zoe Mutia',
        'Luis Nazareno',
        'Ara Quinto',
        'Inigo Romero',
        'Kyler Santos',
        'Jaedin Sarao',
        'Briana Sy',
        'Charlotte Sy',
        'Jared Udono',
        'KC Vida'
    ]

    output = ""
    for name in players:
        output += name + "\n"

    document.getElementById("player").innerText = output
