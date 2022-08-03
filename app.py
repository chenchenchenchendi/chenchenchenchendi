#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install flask


# In[1]:


from flask import Flask, request, render_template


# In[2]:


import joblib


# In[3]:


app= Flask(__name__)


# In[4]:


@app.route("/",methods = ["GET", "POST"])
def index():
    if request.method=="POST":
        rates = float(request.form.get("rate"))
        print(rates)
        model1=joblib.load("regression")
        r1=model1.predict([[rates]])
        model2=joblib.load("tree")
        r2=model2.predict([[rates]])
        return(render_template("index.html", result="OK",result2="OK"))
    else:
        return(render_template("index.html", result="Waiting",result2="Waiting"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




