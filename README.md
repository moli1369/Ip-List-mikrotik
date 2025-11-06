زبان فارسی
 سلام همگی خب این اسکریپت در میکروتیک این عمل رو انجام میده
خب دیدیم بعضی مواقع نیاز داریم لیست ای پی در میکروتیک رو اپدیت کنیم و باید تمامی ای پی ها رو پیدا کنیم و توی میکروتیک اضافه کنیم 
در حقیقت این اسکریپت همین کار رو میکنه اما میاد لیست رو دانلود میکنه و خودکار در لیست ای پی ادرس های میکروتیک قرار میده 
این موضوع برای زمانی هست که میخوایم یک لیست ای پی رو فیلتر کنیم و یا ترافیک ها رو از هم جدا کنیم در این صورت باید لیست ای پی رو قرار بدیم 
این اسکریپت تمامی ای پی های رو دانلود میکنه و خودکار در لیست فایروال قرار میده و دیگه نیاز نیست دستی این عمل انجام بشه 
تایم فریم اپدیت این اسکریپت  1 هفته هست.
در ضمن این لیست تمام ای پی های ایران رو داخل خودش داره که میتونید شخصی سازیش کنید
نحوه راه اندازی در میکروتیک 
این مسیر رو بروید 
----------
Auf deutsch

Hallo zusammen, nun, dieses Skript in Mikrotik macht das
Nun, wir haben gesehen, dass wir manchmal die IP-Liste in Mikrotik aktualisieren und alle IPs finden und in Mikrotik hinzufügen müssen.
Tatsächlich macht dieses Skript dasselbe, lädt jedoch die Liste herunter und fügt Mikrotik-IP-Adressen automatisch in die Liste ein.
Dieses Problem tritt auf, wenn wir eine IP-Liste filtern oder den Datenverkehr trennen möchten. In diesem Fall müssen wir die IP-Liste einfügen.
Dieses Skript lädt alle IPs herunter und fügt sie automatisch in die Firewall-Liste ein, ohne dass dies manuell erfolgen muss.
Der Aktualisierungszeitraum dieses Skripts beträgt 1 Woche.
Darüber hinaus enthält diese Liste alle IPs des Iran, die Sie anpassen können
So richten Sie es in Mikrotik ein
Gehen Sie hier entlang
---------------------
script Mikrotik Mit Löschen Älter list und update nur nue list
```
:local listName "IP2Location"
 /tool fetch url="https://raw.githubusercontent.com/moli1369/Ip-List-mikrotik/refs/heads/main/Iran-mikrotik" mode=https dst-path=ip_list.rsc
/ip firewall address-list remove [find list=$listName]
/import file=ip_list.rsc
:log info ("Ip list ist update und kein problem.!!!")
```
Oder 
👇
keine Löschen address list aber nur update list ip 
```
:local listName "IP2Location"
 /tool fetch url="https://raw.githubusercontent.com/moli1369/Ip-List-mikrotik/refs/heads/main/Iran-mikrotik" mode=https dst-path=ip_list.rsc
/ip firewall address-list [find list=$listName]
/import file=ip_list.rsc
:log info ("Ip list ist update und kein problem.!!!")
```
and > next
```
/system/scheduler>
add name AutoUpdateIPList
interval 1d 00:00:00
on Event
UpdateIPList
```
