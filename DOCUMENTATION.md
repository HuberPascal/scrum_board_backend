# Scrum Board Backend - Dokumentation

## Einführung

Das Scrum Board Backend ist eine RESTful API, die als Backend für ein Kanban-Board dient. Es unterstützt die Verwaltung von Aufgaben, Benutzern und Kontakten. Diese Dokumentation richtet sich an Entwickler, die das Backend erweitern oder integrieren möchten.

## Systemarchitektur

Das Projekt basiert auf Django und dem Django REST Framework. Die Hauptkomponenten sind:

-   **Benutzermanagement** (`users`): Verwaltung von Benutzerkonten und Authentifizierung.
-   **Aufgabenmanagement** (`todolist`): Verwaltung von Aufgaben.
-   **Kontaktverwaltung** (`contacts`): Verwaltung von Kontakten, die den Aufgaben zugeordnet werden können.

### Authentifizierung

-   **POST /auth/login/**:
    -   **Beschreibung**: Authentifiziert einen Benutzer und gibt ein Token zurück.
    -   **Request Body**:
        ```json
        {
            "username": "exampleuser",
            "password": "examplepassword"
        }
        ```
    -   **Response**:
        ```json
        {
            "token": "abc123token",
            "user_id": 1,
            "email": "user@example.com",
            "first_name": "John"
        }
        ```

### Aufgabenmanagement

-   **GET /todos/**:
    -   **Beschreibung**: Gibt alle Aufgaben des angemeldeten Benutzers zurück.
    -   **Response**:
        ```json
        [
            {
                "id": 1,
                "title": "Erste Aufgabe",
                "description": "Beschreibung der Aufgabe",
                "tags": "blue",
                "taskType": "todo",
                "author": {
                    "id": 1,
                    "first_name": "John",
                    "last_name": "Doe",
                    "email": "john.doe@example.com"
                },
                "members": [
                    {
                        "id": 2,
                        "first_name": "Jane",
                        "last_name": "Doe",
                        "email": "jane.doe@example.com"
                    }
                ],
                "created_at": "2024-08-24T16:40:54.237736Z",
                "checked": false
            }
        ]
        ```

## Datenmodelle

### `TodoItem`

-   **title**: Der Titel der Aufgabe.
-   **description**: Eine optionale Beschreibung der Aufgabe.
-   **tags**: Ein Tag zur Kategorisierung der Aufgabe.
-   **taskType**: Der Typ der Aufgabe (z.B. `todo`, `doToday`, `inProgress`, `done`).
-   **author**: Der Benutzer, der die Aufgabe erstellt hat.
-   **members**: Eine Liste von Kontakten, die der Aufgabe zugewiesen sind.

## Tests

Die Teststrategie umfasst Unit-Tests für alle wichtigen Funktionen und Endpunkte der API. Um die Tests auszuführen, verwenden Sie:

```bash
python manage.py test
```
