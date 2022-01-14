
# Github Users Solution

The web application is developed in python 3.8+

### Frameworks Used
- flask
- pre-commit
- requests
- SQLAlchemy
- pytest
- PyMySQL
- Flake8
 
 For installation process a 'requirements.txt' has been provided. Running the application on local machine is as follows

 ```
 $: python3 -m venv venv
 $: source ./venv/bin/activate
 $: pip install -r requirements.txt

 $: export FLASK_APP main.py
 $: source venv/bin/activate
 $: flask db upgrade
 $: flask run

 ```

#### Seeding new data
optional parameters is included with -t <num> or --total <num>
Example.
```
python ./scripts/seed.py
python ./scripts/seed.py -t 80
```

#### Running unit test process
```
python -m pytest
```

