#!/usr/bin/env python3
# encoding: utf-8
import requests, datetime
from flask import Flask, redirect, url_for, abort, request
"""from twilio.twiml import Response as Twiml"""

app = Flask(__name__)

@app.route("/")
def latest():
    z = requests.get("http://lo01.pl/staszic/zastepstwa/api.php?method=lista").json()
    if z.get("status",None) == "success":
        return redirect("http://lo01.pl/staszic/?subpage=zastepstwa&data="+z["data"][0], 302)
    abort(418)

@app.route("/<int:klasa>/<litera>")
def latest_klasa(klasa, litera):
    z = requests.get("http://lo01.pl/staszic/zastepstwa/api.php?method=lista").json()
    if z.get("status",None) == "success":
        return redirect("http://lo01.pl/staszic/?subpage=zastepstwa&klasa=%s %s&data="%(klasa,litera)+z["data"][0], 302)
    abort(418)

"""@app.route("/twilio")
def twilio_start():
    r = Twiml()
    with r.gather(numDigits=2, action=url_for("twilio_finale"), method="GET") as g:
        g.say("Podaj rocznik od 1 do 3 i profil od 1 czyli A do 8 czyli H.", language="pl-PL")
    return str(r)

@app.route("/twilio/finale")
def twilio_finale():
    r = Twiml()
    z = requests.get("http://lo01.pl/staszic/zastepstwa/api.php?method=zastepstwa&klasa=%s %s"%(request.values.get("Digits","99")[0]," abcdefgh"[int(request.values.get("Digits","99")[1])])).json()
    if z.get("status",None) == "success":
        ls = []
        for teachday in z["data"]["lista"]:
            for zast in teachday["zastepstwa"]:
                zast["nauczyciel"] = teachday["nauczyciel"]
                if datetime.datetime.strptime(zast["data"],"%Y-%m-%d").date() >= datetime.date.today():
                    ls.append(zast)
        if len(ls) > 0:
            ls.sort(key=lambda x: (x["data"],x["nauczyciel"],x["lekcja"]))
            for i in ls:
                r.say("%s lekcja %i, %s, %s" % (i["data"],i["lekcja"],i["nauczyciel"],i["opis"]), language="pl-PL")
                if i["zastepca"]: r.say("zastępca "+i["zastepca"], language="pl-PL")
                if i["uwagi"]: r.say(i["uwagi"], language="pl-PL")
        else:
            r.say("Nie znaleziono żadnych zastępstw", language="pl-PL")
    else:
        r.say("Błąd serwera. Strona szkoły się psuje albo twoja klasa nie istnieje.", language='pl-PL')
    return str(r)"""

if __name__ == "__main__": app.run(debug=True, port=5006)
