
mkdir templates 
python3 scaffold.py user username email password phone country_id:references
python3 scaffold.py country name
python3 scaffold.py city name country_id:references
python3 scaffold.py sport name
python3 scaffold.py musicalinstrument name
python3 scaffold.py job name
python3 scaffold.py destination user_id:references city_id:references adventure_id:references
python3 scaffold.py usersport user_id:references sport_id:references adventure_id:references
python3 scaffold.py userjob user_id:references job_id:references adventure_id:references
python3 scaffold.py usermusicalinstrument user_id:references musicalinstrument_id:references adventure_id:references
python3 scaffold.py adventure title description pic:file
