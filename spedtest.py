#  Hussein kaplan - حسين قبلان
# --- برنامج بايثون لحساب سرعة الانترنت

import speedtest
# --- استدعاء المكتبة
test = speedtest.Speedtest()
print("تحميل قائمة السيرفرات...")
test.get_servers()
print("اختيار سيرفر...")

best = test.get_best_server()  # اختيار افضل سيرفر

print(f"وجد سيرفر: {best['host']} يعمل في {best['country']}")
print("فحص سرعة التحميل")
downloadres = test.download()
print("فحص سرعة الرفع")
uploadres = test.upload()
print("فحص البينك")
ping_resault = test.results.ping

# --- كلما كان سرعة التحميل اكثر كلما كان احسن
print(f"سرعة التحميل : {downloadres / 1024 / 1024:.2f} Mbit/s")
# --- كلما كان سرعة الرفع اكثر كلما كان احسن
print(f"سرعة الرفع : {uploadres / 1024 / 1024:.2f} Mbit/s")
# --- كلما كان رقم البنك اقل كلما كان افضل
print(f"البينك : {ping_resault:.2f} ms")