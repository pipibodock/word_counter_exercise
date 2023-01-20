Word Count
================================================

Web page for word count of a text.

Summary
------

- [Config: Environment](#config-environment)
- [Automated Tests](#automated-tests)
- [Manual Tests: EndPoints](#manual-tests-endpoints)

---


Config: Environment
--------------

1. Clone the repository

2. Create a virtual environment with virtualenv:

* Install
```bash
   [sudo] apt install python3.11-venv
```

* After installing, create your virtual environment:
```bash
   python3.11 -m venv /path/to/new/virtual/environment
```

* Activate your environment:
```bash
   source <name>/bin/activate
```

3. Install base requirements OR dev requiriments:
```bash
   pip install -r requirements/base.txt

   pip install -r requirements/dev.txt
```

Automated Tests
--------------

1. Para executar os testes:

``` bash
    src/pytest
```

Manual Tests: EndPoints
--------------

1. Up local server:

```bash
   src/python manage.py runserver
```

2. To count Words:

TODO