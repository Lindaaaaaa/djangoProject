# djangoProject

Instructions for running this program

Requirement
1)python3
2)django >=1.9
3)Django-tables2  
  could install it by simply open the terminal and type command 
  $pip install django-tables2
  Details is here https://django-tables2.readthedocs.io/en/latest/pages/installation.html

Once you meet the requirement

1) Open a terminal and type command $git clone 
   -- now you have clone the project
2) type command 
    $cd fhx
   then type command 
    $python manage.py runserver  (or python3 manager.py runserver  if python3 is not the default python to run)
3) open a browser and go to this url  http://localhost:8000/threats/
   you can try the dropdown filter and sorting the column by click the table header of each column
4) If you would like to test other json object,
   open the folder fhx you just copied, then go to djangoProject/fixtures  There is one file called data.json. 
   You could add other test data to the json file. But make sure that the date follows the date format and it is a valid date.
