import serial
import time

# 配置串行端口參數
serial_port = 'COM1'  # 替換為您的串行端口號
baud_rate = 9600
timeout = 1  # 設置讀取超時

# 生成帶有日期和時間的檔名
file_name = time.strftime("RS232_DataLog_%Y%m%d_%H%M%S.txt")

# 打開串行端口
ser = serial.Serial(serial_port, baud_rate, timeout=timeout)

# 打開一個文件以寫入數據
with open(file_name, 'w') as file:
    try:
        while True:
            # 從串行端口讀取數據
            data = ser.readline().decode('utf-8').strip()
            if data:
                # 將數據寫入文件
                file.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")}: {data}\n')
                file.flush()
                print(data)
    except KeyboardInterrupt:
        print("數據收集已停止")
    finally:
        ser.close()
