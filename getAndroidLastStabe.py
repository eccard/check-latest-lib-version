
# https://dl.google.com/dl/android/maven2/master-index.xml
# https://dl.google.com/dl/android/maven2/androidx/appcompat/group-index.xml


import requests

parameter = "androidx.constraintlayout:constraintlayout"
parameter = "androidx.test.espresso:espresso-core"
parameter = "androidx.appcompat:appcompat"
parameter = "androidx.core:core-ktx"
parameter = "androidx.cardview:cardview"
parameter = "androidx.constraintlayout:constraintlayout"
parameter = "androidx.legacy:legacy-support-v4"
parameter = "androidx.palette:palette"

indexDot = parameter.index(":")
libGroup = parameter[:indexDot]
libName = parameter[indexDot + 1:]

libGroup = libGroup.replace(".","/")
print("libGroup = " +libGroup)
print("libName  = " +libName)
r = requests.get("https://dl.google.com/dl/android/maven2/" + libGroup + "/group-index.xml")

from xml.dom import minidom

xmldoc = minidom.parseString(r.content)

for element in xmldoc.getElementsByTagName(libName):
    print(element.getAttribute("versions").replace(",","\n"))

# todo
# https://mvnrepository.com/artifact/org.jetbrains.kotlinx
