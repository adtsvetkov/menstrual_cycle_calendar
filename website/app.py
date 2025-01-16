from flask import Flask, request, render_template, redirect, url_for, session
from flask_swagger_ui import get_swaggerui_blueprint
import pickle
import numpy as np

# Инициализация Flask App
app = Flask(__name__)
app.secret_key = 'my_secret_key'

# Корректные логин и пароль для доступа в систему
USER_CREDENTIALS = {
    "admin": "admin",  # Логин: пароль
}


# Задаем функцию для входа в систему
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # По нажатию кнопки достаем из полей логин и пароль, которые ввел юзер
        username = request.form.get("username")
        password = request.form.get("password")

        # Проверка логина и пароля
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            session["authenticated"] = True
            return redirect(url_for("form"))
        else:
            # Если не прошел проверку, вернуть ошибку авторизации
            return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")


# Загружаем в оперативную память модель
with open('best_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Инициализируем swagger. Из html будем к нему обращаться по кнопке
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={
    'app_name': "Flask ML Auth Menstrual Cycle Predictor"
})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


# задаем функцию, управляющую формой ввода данных
@app.route("/form", methods=["GET", "POST"])
def form():
    # если юзер перешел на страницу, не залогинившись, выкидываем его
    if not session.get("authenticated"):
        return redirect(url_for("login"))

    # если нажали кнопку "submit"
    if request.method == "POST":
        # забираем информацию из заполненных полей
        data = [
            # если вдруг в CycleNumber ничего нет, прокидываем значение 25 и тд
            int(request.form.get("CycleNumber", 25)),
            int(request.form.get("Group", 1)),
            int(request.form.get("CycleWithPeakorNot", 0)),
            int(request.form.get("ReproductiveCategory", 0)),
            int(request.form.get("EstimatedDayOfOvulation", 15)),
            int(request.form.get("LengthOfLuteralPhase", 25)),
            int(request.form.get("FirstDayofHigh", 18)),
            int(request.form.get("TotalNumberofHighDays", 15)),
            int(request.form.get("TotalHighPostPeak", 4)),
            int(request.form.get("TotalNumberofPeakDays", 10)),
            int(request.form.get("TotalDaysofFertility", 15)),
            int(request.form.get("TotalFertilityFormula", 25)),
            int(request.form.get("LengthofMenses", 5)),
            int(request.form.get("MensesScoreDayOne", 1)),
            int(request.form.get("MensesScoreDayTwo", 1)),
            int(request.form.get("MensesScoreDayThree", 1)),
            int(request.form.get("MensesScoreDayFour", 1)),
            int(request.form.get("MensesScoreDayFive", 1)),
            int(request.form.get("TotalMensesScore", 15)),
            int(request.form.get("IntercourseInFertileWindow", 0)),
            int(request.form.get("NumberofDaysofIntercourse", 10)),
            int(request.form.get("UnusualBleeding", 0))
        ]

        # преобразуем данные в вектор
        data_vector = np.array(data).reshape(1, -1)
        # закидываем вектор в модель RandomForestRegressor, получаем численный ответ
        prediction = model.predict(data_vector)[0]
        return render_template("result.html", prediction=prediction)

    return render_template("form.html")


# задаем функцию для нажатия на кнопку "logout"
@app.route("/logout", methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for("login"))


# задаем фунцию для нажатия на кнопку "назад" со страницы с предсказаниями
@app.route('/back', methods=['GET'])
def back():
    # если юзер не авторизован, выкидываем его на логин,
    # в противном случае возвращаемся на ввод данных
    if not session.get("authenticated"):
        return redirect(url_for("login"))
    return redirect(url_for('form'))

# запуск сервера. параметры прописаны для amvera
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
