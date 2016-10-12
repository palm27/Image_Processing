ตัวอย่างการใช้ OpenCV ทำ Shape Detection รูปแบบหนึ่ง



ขั้นตอนการทำ
```
1. โหลดรูป RGB
2. แปลงเป็น Grey
3. ตัด Threshold
4. นำภาพ Mask มา Inverse
5. หา Contours ของภาพ [จะได้ Contours มาเป็น List ตามจำนวนวัตถุ Mask]
6. นำ Contours มาวนทีละชิ้น
  - หา Moments
  - หา Center of mass
  - หา Approximation
  - วาดจุด และ ข้อความลงบนรูป
7. จะได้ Output Image ออกมา
```
![alt tag](https://lh6.googleusercontent.com/XhfktnCpnznhOJ1BDJSBxpsMX8KoLqXxFq82ppVDUbgUlpQ9DR3SnewT2YE8QBeqWvt8leWScRdQfFk=w1366-h638-rw)
