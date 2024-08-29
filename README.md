# Scrum Board Backend

Dieses Projekt ist das Backend für eine Scrum Board Anwendung, die als Kanban-Board dient. Es ermöglicht die Verwaltung von Aufgaben, einschließlich der Zuordnung von Mitgliedern zu Aufgaben.

## Installation

1. Klone das Repository:

    ```bash
    git clone https://github.com/HuberPascal/scrum_board_backend
    ```

2. Wechsle in das Projektverzeichnis:

    ```bash
    cd repository
    ```

3. Erstelle und aktiviere eine virtuelle Umgebung:

    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

4. Installiere die Abhängigkeiten:

    ```bash
    pip install -r requirements.txt
    ```

5. Führe die Migrationen durch:

    ```bash
    python manage.py migrate
    ```

6. Starte den Entwicklungsserver:

    ```bash
    python manage.py runserver
    ```

## Verwendung

-   **Starten des Servers**: Nachdem der Entwicklungsserver gestartet wurde, ist das Backend unter `http://127.0.0.1:8000/` erreichbar.

-   **API-Endpunkte**:

    ### Aufgaben

    -   `GET /todos/`: Liste aller Aufgaben für den angemeldeten Benutzer.
    -   `POST /todos/`: Erstellen einer neuen Aufgabe.
    -   `GET /todos/<id>/`: Abrufen einer bestimmten Aufgabe.
    -   `PATCH /todos/<id>/`: Teilweises Aktualisieren einer Aufgabe.
    -   `PUT /todos/<id>/`: Vollständiges Aktualisieren einer Aufgabe.
    -   `DELETE /todos/<id>/`: Löschen einer Aufgabe.

    ### Benutzer

    -   `GET /users/`: Liste aller Benutzer.
    -   `GET /users/<id>/`: Abrufen eines bestimmten Benutzers.
    -   `POST /users/`: Erstellen eines neuen Benutzers.
    -   `PUT /users/<id>/`: Vollständiges Aktualisieren eines Benutzers.
    -   `DELETE /users/<id>/`: Löschen eines Benutzers.

    ### Authentifizierung

    -   `POST /auth/login/`: Einloggen eines Benutzers und Erhalt eines Authentifizierungstokens.
    -   `POST /auth/logout/`: Ausloggen eines Benutzers.
    -   `POST /auth/register/`: Registrierung eines neuen Benutzers.

-   **Authentifizierung**: Verwende das `Authorization`-Header mit dem Token, um authentifizierte Anfragen zu stellen.
