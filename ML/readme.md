## Часть проекта, содержащая данные об обучении предиктивной модели

Папка содержит следующие файлы:
1. [Исходный датасет](https://github.com/adtsvetkov/menstrual_cycle_calendar/blob/main/ML/menstrual_cycle_data.csv) ([[источник](https://epublications.marquette.edu/data_nfp/7/)])
2. [Отчет ydata_profiler](https://github.com/adtsvetkov/menstrual_cycle_calendar/blob/main/ML/data_profiler_report.html) по исходным данным
3. [Файл обученной модели](https://github.com/adtsvetkov/menstrual_cycle_calendar/blob/main/ML/best_model.pkl) для последующей загрузки на сервер и предсказаний
4. [Тетрадка с EDA и обучением](https://github.com/adtsvetkov/menstrual_cycle_calendar/blob/main/ML/team_project_ML.ipynb). Содержит в себе основные операции по очистке датасета, тюнингу моделей и выбору лучшей.

<details><summary> Данные во время обучения логировались с помощью среды ClearML. </summary>

В конфигурации задачи содержится информация о параметрах обучения модели.
<img width="989" alt="image" src="https://github.com/user-attachments/assets/1684f217-dcb2-40ee-b4e4-e17fe74c4ce8" />

Во вкладке "info" содержится информация о запуске эксперимента.

![image](https://github.com/user-attachments/assets/a8def546-769d-469e-8a17-229b5675c49b)

С помощью артефактов были сохранены файлы лучших моделей.
<img width="989" alt="image" src="https://github.com/user-attachments/assets/f2c62eea-ff4f-4cb5-aa99-5edc89feb69e" />

Во вкладке "scalars" сохранена информация об изменении скалярных метрик в зависимости от времени / номера триала. Например, ниже можно видеть изменение метрики MSE при подборе параметров с помощью optuna. Также ClearML самостоятельно ставит графики задействованных ресурсов от времени.
![image](https://github.com/user-attachments/assets/64eff1af-45f2-4b3b-b6a4-798bbd921495)

Во вкладке "plots" содержатся все графики, построенные по ходу выполнения работы.
![image](https://github.com/user-attachments/assets/efe52458-58bb-4a22-bbcc-ac226aec0ab2)

По ходу разработки решения были сохранены различные версии датасета: до предобработки и после.

![image](https://github.com/user-attachments/assets/2da5b4d2-9a84-4e36-971d-d0c571d9021a)

</details>
