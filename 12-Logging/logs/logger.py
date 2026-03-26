import logging 

logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
   format='%(asctime)s- %(name)s- %(levelname)s - %(message)s',
    # %D - Date  
    # %d-day part in whole date in integre format 
    # [12/11/25 %d=12 
    # %D=12/11/2025]
   datefmt='%Y-%M-%d %H:%M:%S',
   force=True
)