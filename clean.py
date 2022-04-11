import os
import shutil


os.remove("out/index.html")


dir_athletes = "out/athletes/"
athletes = os.listdir(dir_athletes)

for ath in athletes:
    if ath.endswith(".html"):
        os.remove(os.path.join(dir_athletes, ath))



dir_qA = "out/queryA/"
qA = os.listdir(dir_qA)
if os.path.exists(os.path.join(dir_qA, "queryA.html")):
    os.remove(os.path.join(dir_qA, "queryA.html"))
if os.path.exists(os.path.join(dir_qA, "dates/")):   
    try:
        shutil.rmtree(os.path.join(dir_qA, "dates/"))
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))



dir_qB = "out/queryB/"
if os.path.exists(os.path.join(dir_qB, "queryB.html")):
    os.remove(os.path.join(dir_qB, "queryB.html"))
if os.path.exists(os.path.join(dir_qB, "2019/")):   
    try:
        shutil.rmtree(os.path.join(dir_qB, "2019/"))
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
if os.path.exists(os.path.join(dir_qB, "2020/")):   
    try:
        shutil.rmtree(os.path.join(dir_qB, "2020/"))
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
if os.path.exists(os.path.join(dir_qB, "2021/")):   
    try:
        shutil.rmtree(os.path.join(dir_qB, "2021/"))
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))


dir_qC = "out/queryC/"
if os.path.exists(os.path.join(dir_qC, "queryC.html")):
    os.remove(os.path.join(dir_qC, "queryC.html"))
if os.path.exists(os.path.join(dir_qC, "2019/")):   
    try:
        shutil.rmtree(os.path.join(dir_qC, "2019/"))
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
if os.path.exists(os.path.join(dir_qC, "2020/")):   
    try:
        shutil.rmtree(os.path.join(dir_qC, "2020/"))
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
if os.path.exists(os.path.join(dir_qC, "2021/")):   
    try:
        shutil.rmtree(os.path.join(dir_qC, "2021/"))
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))



dir_qD = "out/queryD/"
if os.path.exists(os.path.join(dir_qD, "queryD.html")):
    os.remove(os.path.join(dir_qD, "queryD.html"))
if os.path.exists(os.path.join(dir_qD, "maiorIgual35/")):   
    try:
        shutil.rmtree(os.path.join(dir_qD, "maiorIgual35/"))
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
if os.path.exists(os.path.join(dir_qD, "menor35/")):   
    try:
        shutil.rmtree(os.path.join(dir_qD, "menor35/"))
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))



dir_qE = "out/queryE/"
if os.path.exists(os.path.join(dir_qE, "queryE.html")):
    os.remove(os.path.join(dir_qE, "queryE.html"))
if os.path.exists(os.path.join(dir_qE, "addresses/")):   
    try:
        shutil.rmtree(os.path.join(dir_qE, "addresses/"))
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))



dir_qF = "out/queryF/"
if os.path.exists(os.path.join(dir_qF, "queryF.html")):
    os.remove(os.path.join(dir_qF, "queryF.html"))
if os.path.exists(os.path.join(dir_qF, "2019/")):   
    try:
        shutil.rmtree(os.path.join(dir_qF, "2019/"))
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
if os.path.exists(os.path.join(dir_qF, "2020/")):   
    try:
        shutil.rmtree(os.path.join(dir_qF, "2020/"))
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
if os.path.exists(os.path.join(dir_qF, "2021/")):   
    try:
        shutil.rmtree(os.path.join(dir_qF, "2021/"))
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))



dir_qG = "out/queryG/"
if os.path.exists(os.path.join(dir_qG, "queryG.html")):
    os.remove(os.path.join(dir_qG, "queryG.html"))
if os.path.exists(os.path.join(dir_qG, "2019/")):   
    try:
        shutil.rmtree(os.path.join(dir_qG, "2019/"))
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
if os.path.exists(os.path.join(dir_qG, "2020/")):   
    try:
        shutil.rmtree(os.path.join(dir_qG, "2020/"))
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
if os.path.exists(os.path.join(dir_qG, "2021/")):   
    try:
        shutil.rmtree(os.path.join(dir_qG, "2021/"))
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))

