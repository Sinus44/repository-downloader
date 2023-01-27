import requests

# Settings ======================================
user = input("Введите имя пользователя: ") or "Sinus44"
repos = input("Введите название репозитория: ") or "Console-Engine"
branch = input("Введите имя ветви репозитория (или оставьте пустым для main): ") or "main"
#  ==============================================

link = f"https://github.com/{user}/{repos}/archive/refs/heads/{branch}.zip"

file = open("archive.zip", "wb")
rawData = requests.get(link)

for chunk in rawData:
	file.write(chunk)

file.close()