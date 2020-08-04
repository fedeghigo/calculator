import streamlit as st
import pandas as pd
import numpy as np



st.title("Evaluator")
document= st.text_input("how many documents?",value=0)
page=st.text_input("how many page?",value=0)
tables=st.text_input("how many tables?",value=0)

document=float(document)
page=float(page)
tables=float(tables)


st.sidebar.title("time needed for single doc")
minutixtab=st.sidebar.text_input("how long for import a table in min?",value=17)
ranget=st.sidebar.text_input("how long for make a range in min?",value=9)
struttura=st.sidebar.text_input("how long for make the structure in min?",value=7)
importt=st.sidebar.text_input("how long for import in day?",value=1)


minutixtab=(float(minutixtab)/60)/8
ranget=(float(ranget)/60)/8
struttura=(float(struttura)/60)/8
#importt=(float(importt)/60)/8
importt=float(importt)

timetablei=tables*minutixtab
rangetablei=ranget*tables
stutturafinali=page*struttura
giorniimporti=importt*document

timetable=st.write("giornate per tabelle:",tables*minutixtab)
#st.text(int(document)+int(page)+int(tables))
rangetable=st.write("giornate per range:",ranget*tables)
stutturafinal=st.write("giornate per struttura:",page*struttura)
giorniimport=st.write("giornate per import:",importt*document)


st.sidebar.title("Formazione")
amministratori=st.sidebar.text_input("number of group for admin?",value=2)

contributor=st.sidebar.text_input("number of group for contributor?",value=10)


amministratori=float(amministratori)
contributor=float(contributor)
ammtot=st.write("giornate per train admin:",amministratori*(0.5))
contributortot=st.write("giornate per train contrib:",contributor*(0.25))


array=pd.DataFrame([tables*minutixtab,ranget*tables,page*struttura,importt*document,(ammtot),(contributortot)], index=["table","range","struttura","import","train admin","train contrib"])




st.write("Totale:",timetablei+rangetablei+stutturafinali+giorniimporti+amministratori*(0.5)+contributor*(0.25))

st.bar_chart(array)
#st.pyplot(array)




