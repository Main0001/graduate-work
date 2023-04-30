# Интерактивный Веб-сайт Хатынь

Интерактивный веб-сайт Хатынь - это онлайн ресурс, посвященный памятному месту Хатынь в Беларуси, которое было сожжено нацистскими войсками во время Второй мировой войны.

Сайт представляет собой виртуальную экскурсию по месту памяти, позволяющую посетителям узнать о истории Хатыни и о трагических событиях, связанных с этим местом. Он содержит интерактивные элементы, такие как 3D-модели, видео-экскурсии, фотогалереи, исторические документы и аудио-материалы.

На сайте также можно найти информацию о музее-заповеднике Хатынь, организовывающем мероприятия, посвященные памяти жертв. Посетители могут получить информацию о расписании экскурсий, выставках и других событиях, связанных с Хатынью.

Основная цель этого веб-сайта - сохранить и передать память о трагических событиях Хатыни, чтобы в будущем люди могли узнать о происходившем там горе, чтить память погибших и помнить о необходимости мира и солидарности.

# Installation

1. Open the terminal and navigate to the directory where you want to create your project using the cd command. For example, if you want to create your project in a directory called "myproject" located in the Documents folder, you can use the command:

```bash
cd graduate-project
```

2. Create a virtual environment for your project by typing the following command in the terminal:

```bash
python3.10 -m venv venv
```

This will create a new directory called "venv" in your project directory, which will contain a Python virtual environment.

3. Activate the virtual environment by typing the following command in the terminal:

```bash
source venv/bin/activate
```

You should see the name of your virtual environment in the terminal prompt, indicating that it is active.

4. Install the required packages for your project by typing the following command in the terminal:

```bash
pip install -r req.txt
```

Make sure you have a req.txt file that contains a list of required packages and their versions.

5. Run the development server by typing the following command in the terminal:

```bash
python manage.py runserver
```

This will start the Django development server and you should be able to see your project by visiting http://localhost:8000/ in your web browser.
