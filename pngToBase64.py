import base64

# ฟังก์ชันสำหรับแปลงไฟล์ PNG เป็น Base64
def png_to_base64(png_file_path):
    with open(png_file_path, "rb") as png_file:
        # อ่านไฟล์ PNG
        png_data = png_file.read()
        # แปลงข้อมูลไฟล์ PNG เป็น Base64
        base64_encoded_data = base64.b64encode(png_data)
        # แปลง Base64 เป็น string เพื่อใช้งาน
        base64_string = base64_encoded_data.decode('utf-8')
        return base64_string

# ระบุพาธไฟล์ PNG ของคุณ
png_file_path = "C:/Users/ROG/Downloads/kazetachinu007.jpg"
base64_string = png_to_base64(png_file_path)

# แสดงผล Base64 string
print(base64_string)
