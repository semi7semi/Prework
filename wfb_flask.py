from flask import Flask, request, render_template

app = Flask(__name__)


# OFF, STR, AP, RFX
WL = [5, 6, 3, 0]
FW = [5, 4, 1, 1]
SM = [6, 5, 2, 1]


def hit(off, defe, att, ref):
    if off > defe:
        test1 = att * (2 / 3 + ref / 6)
    else:
        test1 = att * (1 / 2 + ref / 6)
    return test1


@app.route("/warhammer", methods=["GET", "POST"])
def wfb():
    if request.method == "GET":
        return render_template("warhammer.html")
    else:
        DEF = int(request.form.get("defens"))
        ATT_1 = int(request.form.get("att_1"))
        ATT_2 = int(request.form.get("att_2"))
        HIT = [hit(WL[0], DEF, ATT_1, WL[3]), hit(FW[0], DEF, ATT_2, FW[3])]
        hit1 = round(HIT[0], 1)
        hit2 = round(HIT[1], 1)
        return render_template("wfb_tab.html", hit1=hit1, hit2=hit2)


if __name__ == "__main__":
    app.run(debug=True)