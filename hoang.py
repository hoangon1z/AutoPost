import tkinter as tk
import webbrowser
class FacebookAutomationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SFOX TOOL AUTOMATIC FACEBOOK")
        self.root.geometry("600x470")  # Đặt kích thước cửa sổ
        self.root.iconbitmap("fox.ico")
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.create_widgets()

    def create_widgets(self):
        # Tạo các label và entry widgets trong khung
        self.create_input_widgets()
        self.create_save_buttons()
        self.create_start_button()
        self.create_author_label()

    def create_input_widgets(self):
        via_label = tk.Label(self.frame, text="Nhập Tài Khoản Theo Định Dạng a|a|a:")
        via_label.pack()

        self.via_entry = tk.Text(self.frame, height=4, wrap=tk.WORD)  # wrap=tk.WORD để cho phép xuống dòng
        self.via_entry.insert(tk.END, load_from_file('via.txt'))
        self.via_entry.pack(fill=tk.BOTH, padx=10, pady=(0, 10))

        status_label = tk.Label(self.frame, text="Nhập Status:")
        status_label.pack()

        self.status_entry = tk.Text(self.frame, height=6, wrap=tk.WORD)  # wrap=tk.WORD để cho phép xuống dòng
        self.status_entry.insert(tk.END, load_from_file('status.txt'))
        self.status_entry.pack(fill=tk.BOTH, padx=10, pady=(0, 10))

        sll_label = tk.Label(self.frame, text="Nhập Số Lượng Cửa Sổ:")
        sll_label.pack()

        self.sll_entry = tk.Entry(self.frame)
        self.sll_entry.insert(0, load_from_file('sll.txt'))
        self.sll_entry.pack(fill=tk.X, padx=10, pady=(0, 10))

        fanpage_label = tk.Label(self.frame, text="Nhập ID Fanpage:")
        fanpage_label.pack()

        self.fanpage_entry = tk.Text(self.frame, height=4, wrap=tk.WORD)  # wrap=tk.WORD để cho phép xuống dòng
        self.fanpage_entry.insert(tk.END, load_from_file('listfan.txt'))
        self.fanpage_entry.pack(fill=tk.BOTH, padx=10, pady=(0, 10))

    def create_save_buttons(self):
        # Không tạo nút lưu nữa
        pass

    def create_start_button(self):
        start_button = tk.Button(self.frame, text="Bắt Đầu", command=self.start_script, font=("Arial", 14), bg="red", fg="red")
        start_button.pack(fill=tk.X, padx=10, pady=(0, 10))

    def create_author_label(self):
        author_label = tk.Label(self.frame, text="HoangIT.GW.VN", fg="red")
        author_label.pack(anchor="nw")

        # Thêm đường liên kết vào chữ "HoangIT.GW.VN"
        link = tk.Label(self.frame, text="https://www.facebook.com/hoangtran1510", fg="blue", cursor="hand2")
        link.pack(anchor="nw")
        link.bind("<Button-1>", lambda event: webbrowser.open_new("https://www.facebook.com/hoangtran1510"))

    def save_to_file(self, filename, data):
        with open(filename, 'w') as file:
            file.write(data)
    def start_script(self):
        from concurrent.futures import ThreadPoolExecutor
        import requests
        import csv
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service as ChromeService
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        import time
        from selenium.common.exceptions import TimeoutException
        from selenium.common.exceptions import NoSuchElementException
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.chrome.service import Service as ChromeService
        from webdriver_manager.chrome import ChromeDriverManager
        import pyotp
        import os
        import re
                # Lưu dữ liệu trước khi bắt đầu tiến trình
        self.save_to_file('via.txt', self.via_entry.get("1.0", tk.END))
        self.save_to_file('status.txt', self.status_entry.get("1.0", tk.END))
        self.save_to_file('sll.txt', self.sll_entry.get())
        self.save_to_file('listfan.txt', self.fanpage_entry.get("1.0", tk.END))
        def login_via(subList, fanpage, status, stt):
            try:
                if stt <= 8:
                    stt = stt
                else:
                    stt = stt%8
                if stt >= 4 :
                    b = 500
                else:
                    b = 0
                if stt <=3 :
                    a = stt*500
                else:
                    a = (stt%4)*500
                NewlistVia = []
                with open('via.txt', 'r') as f:
                    reader = csv.reader(f, delimiter= '|', lineterminator = '\n')
                    for i in reader:
                        NewlistVia.append(i)
                options = ChromeOptions()
                options.add_argument('--disable-notifications')
                # chrome_service = ChromeService('./chromedriver')
                options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1')
                driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
                
                driver.set_window_rect(a,b,400,700)
                Taikhoan = subList[0]
                Matkhau = subList[1]
                
                FA = subList[2]
                
                totp = pyotp.TOTP(str(FA).replace(' ','')).now()
                driver.get('https://mbasic.facebook.com/login')
                time.sleep(1)
                try:
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[6]/div[1]/div/div[2]/div[4]/button[2]")))
                    driver.find_element((By.XPATH, "/html/body/div[1]/div/div[6]/div[1]/div/div[2]/div[4]/button[2]")).click()
                except:pass
                wait = WebDriverWait(driver, 1)  # Add this line
                men_menu = wait.until(EC.visibility_of_element_located((By.ID, "m_login_email")))
                driver.find_element(By.ID, 'm_login_email').send_keys(Taikhoan)
                time.sleep(1)
                wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/table/tbody/tr/td/div[2]/div/div[2]/form/ul/li[2]/div/input")))
                driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/table/tbody/tr/td/div[2]/div/div[2]/form/ul/li[2]/div/input').send_keys(Matkhau)
                time.sleep(1)
                driver.find_element(By.NAME, 'login').click()
                time.sleep(1)
                men_menu = wait.until(EC.visibility_of_element_located((By.ID, "approvals_code")))
                driver.find_element(By.ID, 'approvals_code').send_keys(totp)
                time.sleep(1)
                driver.find_element(By.ID, 'checkpointSubmitButton-actual-button').click()
                driver.find_element(By.ID, 'checkpointSubmitButton-actual-button').click()
                
                try:
                    driver.find_element(By.ID, 'checkpointSubmitButton-actual-button').click()
                    driver.find_element(By.ID, 'checkpointSubmitButton-actual-button').click()
                    driver.find_element(By.ID, 'checkpointSubmitButton-actual-button').click()
                except NoSuchElementException:
                    pass
                time.sleep(1
                           )

                fanpage_id = fanpage[0]

                driver.get(f'https://m.facebook.com/profile.php/?id={fanpage_id}')
                time.sleep(5)
                wait = WebDriverWait(driver, 10)  # Chờ tối đa 10 giây
                element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div[3]')))
                element.click()
                time.sleep(2)
                driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div/div/div/div[1]/div[4]').click()
                time.sleep(10)
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[5]/div/div[3]/div').click()
                time.sleep(2)
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[5]/div/div').click()
                time.sleep(2)
                
                status_text = status.strip()
                status_text = re.sub(r'\d{9,}', lambda m: f'@[{m.group(0)}:0]', status_text)
                wait = WebDriverWait(driver, 5)
                element = wait.until(EC.visibility_of_element_located((By.XPATH, f'/html/body/div[2]/div/div[2]/div[5]/div/div/div/textarea')))
                element.send_keys(status_text)
                time.sleep(5)
                element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[3]')
                driver.execute_script("arguments[0].click();", element)             
                time.sleep(2)
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[3]').click()
                time.sleep(5)

                driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[9]/div[1]/div').click()
                time.sleep(2)
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[3]/div/div[3]/div').click()
                time.sleep(2)
                driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/div[6]').click()
                time.sleep(2)
                status_text = status  # Sử dụng status được truyền vào hàm, không cần đọc từ tệp
                status_element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[6]/div[1]/textarea')
                status_element.clear()
                status_text = re.sub(r'\d{9,}', lambda m: f'@[{m.group(0)}:0]', status_text)
                status_element.send_keys(status_text)
                time.sleep (2)
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div[3]/div').click()
                time.sleep(10)
                driver.quit()
                try:
                    time.sleep(5)
                    driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/from/div/article/div[1]/table/tbody/tr/td/button').click()
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[3]/from/div/article/div[2]/table/tbody/tr/td[2]/button")))
                    driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/from/div/article/div[2]/table/tbody/tr/td[2]/button').click()
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[3]/from/div/article/div[1]/table/tbody/tr/td/button")))
                except:
                    pass
                WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/a")))
                driver.get('https://mbasic.facebook.com/login')
            except Exception as e:
                print(e)
            
        with open('sll.txt', 'r') as f:
            soluong = int(f.read().strip())

        list_via = []
        with open('via.txt', 'r') as f:
            reader = csv.reader(f, delimiter='|', lineterminator='\n')
            for i in reader:
                list_via.append(i)
        Newlist_via = [ele for ele in list_via if ele != []]

        list_fanpage = []
        with open('listfan.txt', 'r') as f:
            reader = csv.reader(f, delimiter='|', lineterminator='\n')
            for i in reader:
                list_fanpage.append(i)
        Newlist_fanpage = [ele for ele in list_fanpage if ele != []]

        list_status = []
        with open('status.txt', 'r') as f:
            list_status = f.read().split('---')
        Newlist_status = [status.strip() for status in list_status]

        List_stt = []
        for stt in range(len(Newlist_via)):
            List_stt.append(stt)

        with ThreadPoolExecutor(max_workers=soluong) as executor:
            executor.map(login_via, Newlist_via, Newlist_fanpage, Newlist_status, List_stt)
            executor.shutdown(wait=True)
        pass

def load_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return ""

if __name__ == "__main__":
    root = tk.Tk()
    app = FacebookAutomationApp(root)
    root.mainloop()
