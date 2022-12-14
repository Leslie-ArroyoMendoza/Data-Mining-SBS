# Data-Mining-SBS
Data mining of SBS webpage (Banking sector)

This repository extracts urls and downloads xls and xlsx files from the [SBS](https://www.sbs.gob.pe/estadisticas-y-publicaciones/estadisticas-/sistema-financiero_) webpage, which contains information of the financial institutions of Peru.

|**Language**| Functionality |
|------|------|
| Python| Web scraping |


## Inspection of SBS webpage

![alt text](https://github.com/Leslie-ArroyoMendoza/Data-Mining-SBS/blob/aa5eb67a60111066549cb0a63606857315227dca/SBS_main.png)

First is necessary to **know** the webpage we aim to inspect. Given that this webpage doesn't have fixed urls where we can extract data I used Selenium to navigate through the webpage until I reached the part where the urls are displayed. 

Second, find a fix url that is close to the data we are looking for.
Navigate inside the SBS webpage to find the Financial statements of the commercial banks in Peru
1. Go to the menu located on the rigth side and search for __Estadisticas__, click on it and then click on __Sistema Financiero__ .

![alt text](https://github.com/Leslie-ArroyoMendoza/Data-Mining-SBS/blob/aa5eb67a60111066549cb0a63606857315227dca/SBS_Estadisticas.png)

2. Scroll down until you find __Información por Tipo de Institución Financiera__, then click on __Banca Múltiple__ .

![alt text](https://github.com/Leslie-ArroyoMendoza/Data-Mining-SBS/blob/aa5eb67a60111066549cb0a63606857315227dca/SBS_BancaMultiple.png)

3. You have reached the Statistical Information of Commercial Banking of Peru. Copy the url of this page and save it because you will need it as an input for the driver "**browser**".

 ```python
 url1="https://www.sbs.gob.pe/app/stats_net/stats/EstadisticaBoletinEstadistico.aspx?p=1#"
# Open the url inside the driver 
browser.get(url1)
 ```
 
 ## Extraction of urls
 
 With the **Data_mining_SB.py** and the url of the previous step, you can run the python code to click on buttons and the find elements by an identificator. I used the library Selenium to click on some buttons to display the xls files I wanted to dowload. 
 * Click on __Estados Financieros por Empresa Bancaria__
   * Click on __Balance General y Estado de Ganancias y Pérdidas__
     * Click on arrow next to __Años anteriores__
 
Every element I had to click on have various way to be identified, one of the most reliables is the XPATH. Sometimes is more efficient to find the element by the TAG_NAME... it really depends on the html elements of the webpage.

I localized the XPATH of the elements I wanted to click and used them as an input for my code. Finally searched for all the elements that had as TAG_NAME "a" becuase they are followed by the urls of the xls files I wanted to download. 

 
