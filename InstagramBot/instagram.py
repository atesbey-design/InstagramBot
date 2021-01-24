from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Instagram: #passsword.py dosyasından şifre ve kullanıcı adı çektim
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self): #instagramı açtırıp kullanıcı adı ve şifreyi atadım
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        
        usernameInput = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[2]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(8)

    def getFollowers(self, max): #istenilen kullanıcının profiline girip takip et butonuna tıklattım
        self.browser.get("https://www.instagram.com/{}/".format(self.username))
        time.sleep(2)
        self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(2)
        
        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        followerCount = len(dialog.find_elements_by_css_selector("li"))
        
        print("first count: {}".format(followerCount))

        action = webdriver.ActionChains(self.browser)

        while followerCount < max:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)

            newCount = len(dialog.find_elements_by_css_selector("li"))

            if followerCount != newCount:
                followerCount = newCount
                print("second count: {}".format(newCount))
                time.sleep(1)
            else:
                break
        
        followers = dialog.find_elements_by_css_selector("li")

        followerList = []
        i = 0
        for user in followers:
            link = user.find_element_by_css_selector("a").get_attribute("href")            
            followerList.append(link)            
            i += 1
            if i == max:
                break

        with open("followers.txt", "w",encoding="UTF-8") as file:
            for item in followerList:
                file.write(item + "\n")

    def followUserLocked(self, username):
        self.browser.get("https://www.instagram.com/"+ username)
        time.sleep(2)

        followButton = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button")
        if followButton.text != "Mesaj Gönder":
            followButton.click()
            time.sleep(2)
        else:
            # for i in range(1,2):
            #     browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            #     time.sleep(3)
            self.browser.find_elements_by_class_name("_9AhH0").click()
            
            time.sleep(2)

            
   
               
    def followUserUnlocked(self, username):
        self.browser.get("https://www.instagram.com/"+ username)
        time.sleep(2)

        followButton = self.browser.find_element_by_tag_name("button")
        if followButton.text != "Mesaj Gönder":
            followButton.click()
            time.sleep(2)
            print("çalıştı")
        else:
            print("çalışmadı")
            self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[3]/article/div/div/div/div[1]").click()
            
            time.sleep(5)
            self.browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button").click()
            time.sleep(2)
            browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            
            
        

    def unFollowUser(self, username):
        self.browser.get("https://www.instagram.com/"+ username)
        time.sleep(2)

        followButton = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button/div/span")
        if followButton.text != "Takibi Bırak":
            followButton.click()
            time.sleep(2)
            self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[1]").click()
        else:
            print("zaten takip etmiyorsunuz.")

    
    

instgrm = Instagram(username, password)
instgrm.signIn()
#instgrm.getFollowers(50)
#instgrm.followUserLocked("busenaz.tasdelen")
#instgrm.LikeImage()
instgrm.followUserUnlocked("tuncer_bostanci")
#instgrm.unFollowUser("tuncer_bostanci")

